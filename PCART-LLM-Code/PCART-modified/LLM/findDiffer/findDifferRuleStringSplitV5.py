## @package findDifferRuleStringSpilt
#  Pure LLM-based difference analysis for API parameter changes, enhanced with docstring context
#
#  String/docstring 上下文版本：与 findDifferRuleNullSpilitV5 对齐（OpenAI SDK + 提示内 JSON Schema），
#  不使用 LangChain；在 Null 版本基础上将 docstring 信息加入 prompt，
#  让 LLM 能够参考文档字符串来更准确地理解参数语义。
#
#  V5Plus: 将原来的单次 LLM 请求拆分为 4 步串联请求，
#  分别对应：按名匹配 → 处理未匹配位置参数 → 处理未匹配关键字参数 → 处理剩余新参数。

import os
import re
import json
import traceback
from openai import OpenAI

from Change.changeAnalyze import para2Obj, isDifferType, Update
from Tool.tool import getFileName, removeParameter

# ============================================================
# JSON Schemas — one per step
# ============================================================

step1_schema = {
    "title": "Step1NameMatchResult",
    "description": "Step 1: Parameters matched by name between old and new versions.",
    "type": "object",
    "properties": {
        "changes": {
            "type": "array",
            "description": (
                "Old parameters that have a name match in the new version, with detected changes. "
                "Allowed change fields: posChange, typeChange, pos2key, key2pos."
            ),
            "items": {
                "type": "object",
                "properties": {
                    "param_name": {
                        "type": "string",
                        "description": "Old parameter name",
                    },
                    "position": {
                        "type": "integer",
                        "description": "Old position index (0-based, excluding self/cls)",
                    },
                    "posChange": {
                        "type": "integer",
                        "description": "New position index if position changed (positional params only)",
                    },
                    "typeChange": {
                        "type": "string",
                        "description": "New type annotation string if the type changed",
                    },
                    "pos2key": {
                        "type": "string",
                        "description": "Parameter name if it changed from positional to keyword",
                    },
                    "key2pos": {
                        "type": "string",
                        "description": "Parameter name if it changed from keyword to positional",
                    },
                },
                "required": ["param_name", "position"],
            },
        }
    },
    "required": ["changes"],
}

step2_schema = {
    "title": "Step2PositionalResult",
    "description": "Step 2: Rename or delete for unmatched old positional parameters.",
    "type": "object",
    "properties": {
        "changes": {
            "type": "array",
            "description": "Each unmatched old positional parameter, marked as renamed or deleted.",
            "items": {
                "type": "object",
                "properties": {
                    "param_name": {
                        "type": "string",
                        "description": "Old parameter name",
                    },
                    "position": {
                        "type": "integer",
                        "description": "Old position index (0-based, excluding self/cls)",
                    },
                    "rename": {
                        "type": "string",
                        "description": "New name if the parameter was renamed",
                    },
                    "delete": {
                        "type": "boolean",
                        "description": "true if the parameter was deleted",
                    },
                },
                "required": ["param_name", "position"],
            },
        }
    },
    "required": ["changes"],
}

step3_schema = {
    "title": "Step3KeywordResult",
    "description": "Step 3: Rename or delete for unmatched old keyword parameters.",
    "type": "object",
    "properties": {
        "changes": {
            "type": "array",
            "description": "Each unmatched old keyword parameter, marked as renamed or deleted.",
            "items": {
                "type": "object",
                "properties": {
                    "param_name": {
                        "type": "string",
                        "description": "Old parameter name",
                    },
                    "position": {
                        "type": "integer",
                        "description": "Old position index (0-based, excluding self/cls)",
                    },
                    "rename": {
                        "type": "string",
                        "description": "New name if the parameter was renamed",
                    },
                    "delete": {
                        "type": "boolean",
                        "description": "true if the parameter was deleted",
                    },
                },
                "required": ["param_name", "position"],
            },
        }
    },
    "required": ["changes"],
}

step4_schema = {
    "title": "Step4NewParamsResult",
    "description": "Step 4: Handle remaining new parameters (replace / addPos / addKey).",
    "type": "object",
    "properties": {
        "changes": {
            "type": "array",
            "description": "Entries for remaining new parameters.",
            "items": {
                "type": "object",
                "properties": {
                    "param_name": {
                        "type": "string",
                        "description": (
                            "For replace: old parameter name at that position. "
                            "For addPos/addKey: new parameter name."
                        ),
                    },
                    "position": {
                        "type": "integer",
                        "description": (
                            "For replace: old parameter position. "
                            "For addPos/addKey: new parameter position."
                        ),
                    },
                    "replace": {
                        "type": "string",
                        "description": "'name' or 'name=default_value' for replacement",
                    },
                    "addPos": {
                        "type": "string",
                        "description": "'name' or 'name=default_value' for newly added positional parameter",
                    },
                    "addKey": {
                        "type": "string",
                        "description": "'name' or 'name=default_value' for newly added keyword parameter",
                    },
                },
                "required": ["param_name", "position"],
            },
        }
    },
    "required": ["changes"],
}

# ============================================================
# System prompts — one per step
# ============================================================

STEP1_SYSTEM_PROMPT = """You are an API parameter change analysis assistant.

<task>
Compare the old and new API parameter lists. For each old parameter (both positional and keyword), check if a parameter with the **same name** exists in the new version. Output ONLY parameters that were matched by name. Use the provided docstrings to better understand the semantics of each parameter.
</task>

<analysis_rules>
For each old parameter, check if a parameter with the **same name** exists in the new version:
- If found among the same type (positional→positional or keyword→keyword):
  - Check if the **position** changed (only for **parameter_type:positional**). If so, record `posChange` = new position.
  - Check if the **type annotation** (data_type) changed (see type compatibility rules). If so, record `typeChange` = new type string.
  - If the parameter has NO changes at all, you still MUST include it with no change fields set.
- If an old **positional** parameter name is found in the new **keyword** parameters: record `pos2key` = parameter name (and also check typeChange).
- If an old **keyword** parameter name is found in the new **positional** parameters: record `key2pos` = parameter name (and also check typeChange).
- If an old parameter name is NOT found anywhere in the new version, do NOT include it.
</analysis_rules>

<type_compatibility>
Two types are considered compatible (no type change) if:
- They are identical strings
- Either one is empty/missing
- The old type is a subset of the new type (e.g., `int` is compatible with `Union[int, float]`)
</type_compatibility>

<important_notes>
- `**kwargs` type parameters should be excluded from keyword parameter lists.
- When recording `typeChange`, use the full new type annotation string.
- The output should be sorted by position.
</important_notes>
"""

STEP2_SYSTEM_PROMPT = """You are an API parameter change analysis assistant.

<task>
Determine whether each unmatched old positional parameter has been renamed or deleted in the new version. Use the provided docstrings to better understand the semantics of each parameter.
</task>

<analysis_rules>
For each unmatched old positional parameter:
- If a new positional parameter exists at the **same position** with a **compatible type** (including when either type is empty), and based on the docstrings and parameter semantics, the new parameter is semantically the same parameter with a name change, or the new parameter extends the functionality of the old one with full backward compatibility, consider it a **rename**. Record `rename` = new parameter name.
- Otherwise, mark the old parameter as **deleted** (`delete` = true).
Each parameter must be either renamed or deleted — no other outcome.
</analysis_rules>

<type_compatibility>
Two types are considered compatible (no type change) if:
- They are identical strings
- Either one is empty/missing
- The old type is a subset of the new type (e.g., `int` is compatible with `Union[int, float]`)
</type_compatibility>

<important_notes>
- `rename` and `delete` are mutually exclusive — pick exactly one per parameter.
- The output should be sorted by position.
- Use the docstrings to understand parameter semantics when deciding renames vs deletes.
</important_notes>
"""

STEP3_SYSTEM_PROMPT = """You are an API parameter change analysis assistant.

<task>
Determine whether each unmatched old keyword parameter has been renamed or deleted in the new version. Use the provided docstrings to better understand the semantics of each parameter.
</task>

<analysis_rules>
For each unmatched old keyword parameter:
- If a remaining new keyword parameter has the **same type**, and based on the docstrings and parameter semantics, the new parameter is semantically the same parameter with a name change, or the new parameter extends the functionality of the old one with full backward compatibility, consider it a **rename**. Record `rename` = new parameter name.
- Otherwise, mark the old parameter as **deleted** (`delete` = true).
Each parameter must be either renamed or deleted — no other outcome.
</analysis_rules>

<type_compatibility>
Two types are considered compatible (no type change) if:
- They are identical strings
- Either one is empty/missing
- The old type is a subset of the new type (e.g., `int` is compatible with `Union[int, float]`)
</type_compatibility>

<important_notes>
- `rename` and `delete` are mutually exclusive — pick exactly one per parameter.
- The output should be sorted by position.
- Use the docstrings to understand parameter semantics when deciding renames vs deletes.
</important_notes>
"""

STEP4_SYSTEM_PROMPT = """You are an API parameter change analysis assistant.

<task>
Handle remaining new parameters that were not matched or consumed in previous steps. Determine whether each is a replacement for a freed old position or a newly added parameter.
</task>

<analysis_rules>
For remaining new **positional** parameters:
- If its position index is within the range [0, old_positional_count - 1] AND there is a freed old positional parameter at that position (listed in the freed positions context), it is a **replacement**. Record `replace` on the old parameter's entry (use the OLD parameter's `param_name` and `position`). Format: "name" or "name=default_value".
- Otherwise (position >= old_positional_count, or no freed old param at that position), it is a newly **added positional** parameter. Create an entry with `addPos` = "name" or "name=default_value" (use the NEW parameter's name and position).
- `replace` and `addPos` are mutually exclusive.

For remaining new **keyword** parameters:
- They are newly **added keyword** parameters. Create an entry with `addKey` = "name" or "name=default_value" (use the NEW parameter's name and position).
</analysis_rules>

<important_notes>
- When recording `replace`, `addPos`, or `addKey`, format as "name" or "name=default_value".
- The output should be sorted by position.
</important_notes>
"""

# ============================================================
# Human prompt templates — one per step
# ============================================================

STEP1_HUMAN_TEMPLATE = """<general_information>

### API call
{fullApiName}

### Library and version
- old：{oldVersion}
- new：{newVersion}

</general_information>

<old_parameters>

```json
{oldParamsJSON}
```

</old_parameters>

<new_parameters>

```json
{newParamsJSON}
```

</new_parameters>

<old_docstring>

```
{oldDocstring}
```

</old_docstring>

<new_docstring>

```
{newDocstring}
```

</new_docstring>

<output_format>
You MUST output ONLY a valid JSON object (no markdown, no explanation, no extra text) that strictly follows this schema:

```json
{outputSchema}
```

Only include change fields (posChange, typeChange, pos2key, key2pos) when they actually apply. For matched parameters with no changes, include only `param_name` and `position`.
Only include parameters whose name appears in the new version. If no parameters matched by name, output: {{"changes": []}}
</output_format>

Based on the analysis rules, identify all old parameters whose name appears in the new version and report any changes. Use the provided docstrings to better understand parameter semantics.
"""

STEP2_HUMAN_TEMPLATE = """<general_information>

### API call
{fullApiName}

### Library and version
- old：{oldVersion}
- new：{newVersion}

</general_information>

<unmatched_old_positional_parameters>

```json
{unmatchedOldPosJSON}
```

</unmatched_old_positional_parameters>

<unmatched_new_positional_parameters>

```json
{unmatchedNewPosJSON}
```

</unmatched_new_positional_parameters>

<old_docstring>

```
{oldDocstring}
```

</old_docstring>

<new_docstring>

```
{newDocstring}
```

</new_docstring>

<output_format>
You MUST output ONLY a valid JSON object (no markdown, no explanation, no extra text) that strictly follows this schema:

```json
{outputSchema}
```

Each old positional parameter must be marked with either `rename` or `delete` (mutually exclusive).
If the input list is empty, output: {{"changes": []}}
</output_format>

Based on the analysis rules, determine whether each unmatched old positional parameter was renamed or deleted. Consider parameter positions, types, docstrings, and your knowledge of the library.
"""

STEP3_HUMAN_TEMPLATE = """<general_information>

### API call
{fullApiName}

### Library and version
- old：{oldVersion}
- new：{newVersion}

</general_information>

<unmatched_old_keyword_parameters>

```json
{unmatchedOldKeyJSON}
```

</unmatched_old_keyword_parameters>

<unmatched_new_keyword_parameters>

```json
{unmatchedNewKeyJSON}
```

</unmatched_new_keyword_parameters>

<old_docstring>

```
{oldDocstring}
```

</old_docstring>

<new_docstring>

```
{newDocstring}
```

</new_docstring>

<output_format>
You MUST output ONLY a valid JSON object (no markdown, no explanation, no extra text) that strictly follows this schema:

```json
{outputSchema}
```

Each old keyword parameter must be marked with either `rename` or `delete` (mutually exclusive).
If the input list is empty, output: {{"changes": []}}
</output_format>

Based on the analysis rules, determine whether each unmatched old keyword parameter was renamed or deleted. Consider parameter types, docstrings, and your knowledge of the library.
"""

STEP4_HUMAN_TEMPLATE = """<general_information>

### API call
{fullApiName}

### Library and version
- old：{oldVersion}
- new：{newVersion}

### Old positional parameter count
{oldPosParaNum}

</general_information>

<freed_old_positional_positions>
The following old positional parameters had their position freed (by delete or posChange in earlier steps). They are available for `replace`:

```json
{freedOldPosJSON}
```

</freed_old_positional_positions>

<remaining_new_positional_parameters>

```json
{remainingNewPosJSON}
```

</remaining_new_positional_parameters>

<remaining_new_keyword_parameters>

```json
{remainingNewKeyJSON}
```

</remaining_new_keyword_parameters>

<output_format>
You MUST output ONLY a valid JSON object (no markdown, no explanation, no extra text) that strictly follows this schema:

```json
{outputSchema}
```

For `replace` entries, use the OLD parameter's `param_name` and `position`. For `addPos`/`addKey` entries, use the NEW parameter's name and position.
If no parameters to process, output: {{"changes": []}}
</output_format>

Based on the analysis rules, determine whether each remaining new parameter is a replacement for a freed old position or a new addition.
"""

# ============================================================
# Utility helpers
# ============================================================


def _llm_debug_enabled():
    """环境变量 FIND_DIFFER_LLM_DEBUG=1 / true / yes / on 时开启 LLM 原始响应调试输出。"""
    v = os.environ.get("FIND_DIFFER_LLM_DEBUG", "").strip().lower()
    return v in ("1", "true", "yes", "on")


def _openai_response_to_dict(obj):
    """将 SDK 返回对象转为可 JSON 序列化的 dict（便于打印「原始」结构）。"""
    if obj is None:
        return None
    if hasattr(obj, "model_dump"):
        try:
            return obj.model_dump()
        except Exception:
            pass
    if hasattr(obj, "dict") and callable(getattr(obj, "dict")):
        try:
            return obj.dict()
        except Exception:
            pass
    return {"_fallback_repr": repr(obj)}


def print_llm_raw_response(response, label=""):
    """
    打印 chat.completions.create 返回的完整结构（与 HTTP 响应体字段一致，便于排查空 content 等）。
    仅当 FIND_DIFFER_LLM_DEBUG 开启时输出。
    """
    if not _llm_debug_enabled():
        return
    sep = "=" * 72
    print(f"\n{sep}\n[FIND_DIFFER_LLM_DEBUG] {label}\n{sep}")
    try:
        data = _openai_response_to_dict(response)
        print(json.dumps(data, ensure_ascii=False, indent=2, default=str))
    except Exception as e:
        print(f"(序列化失败: {e})")
        traceback.print_exc()
        print(repr(response))
    print(f"{sep}\n")


def _extract_json_from_text(text):
    """
    从可能包含 <think>...</think> 和 markdown 代码块的文本中提取 JSON。
    适配 MiniMax 等思维链模型：它们会在 content 里混入推理过程和 markdown 格式。
    """
    stripped = re.sub(r"<think>[\s\S]*?</think>", "", text)
    stripped = re.sub(r"<think>[\s\S]*$", "", stripped)
    stripped = stripped.strip()

    m = re.search(r"```(?:json)?\s*\n([\s\S]*?)```", stripped)
    if m:
        stripped = m.group(1).strip()

    return json.loads(stripped)


def parseStructuredResponse(response):
    """
    Normalize OpenAI chat completion structured output to a plain dict.
    兼容标准 JSON 输出和包含 <think> / markdown 代码块的思维链模型输出。
    """
    message = response.choices[0].message
    content = message.content

    if _llm_debug_enabled():
        print(
            "\n[FIND_DIFFER_LLM_DEBUG] message 摘要:\n"
            f"  content 类型: {type(content).__name__}\n"
            f"  content 长度: {len(content) if isinstance(content, str) else 'N/A'}\n"
            f"  refusal: {getattr(message, 'refusal', None)!r}\n"
            f"  finish_reason: {getattr(response.choices[0], 'finish_reason', None)!r}\n"
        )

    if isinstance(content, str):
        if not content.strip():
            if _llm_debug_enabled():
                print(
                    "[FIND_DIFFER_LLM_DEBUG] 警告: message.content 为空或仅空白，"
                    "json.loads 将失败。完整对象见上一段 Raw API response。\n"
                )
            raise ValueError("LLM returned empty content")

        try:
            return json.loads(content)
        except json.JSONDecodeError:
            if _llm_debug_enabled():
                print(
                    "[FIND_DIFFER_LLM_DEBUG] json.loads 直接解析失败，"
                    "尝试提取 <think>/markdown 包裹的 JSON...\n"
                )
            return _extract_json_from_text(content)

    if isinstance(content, list):
        text_parts = []
        for item in content:
            if isinstance(item, dict) and item.get("type") == "text":
                text_parts.append(item.get("text", ""))
            elif hasattr(item, "type") and item.type == "text":
                text_parts.append(getattr(item, "text", ""))
        if text_parts:
            combined = "".join(text_parts)
            try:
                return json.loads(combined)
            except json.JSONDecodeError:
                return _extract_json_from_text(combined)

    raise TypeError(f"Unsupported structured output type: {type(content).__name__}")


## Convert parameter objects to JSON format for LLM
## 将参数对象转换为 LLM 所需的 JSON 格式
#
#  @param paraList List of Parameter objects
#  @param isPositional Whether these are positional parameters
#  @return jsonList List of dictionaries in JSON format
def convertParamsToJSON(paraList, isPositional=True):
    jsonList = []
    for para in paraList:
        paramDict = {
            "name": para.name,
            "position": para.position,
            "parameter_type": "positional" if isPositional else "keyword",
            "data_type": para.type if para.type else None,
        }
        if para.value:
            paramDict["default_value"] = para.value
        jsonList.append(paramDict)
    return jsonList


## Get docstring from match dictionary
## 从匹配字典中获取 docstring
#
#  @param matchDict The match dictionary (may contain docstring), can be None
#  @return docstring The docstring string, empty if not found
def getDocstring(matchDict):
    if isinstance(matchDict, dict) and 'docstring' in matchDict:
        return matchDict.get('docstring', '')
    return ''


LLM_SKIP_API_KEYWORDS = [
    "np.array",
]


def shouldSkipLLM(apiCall):
    apiCallLower = (apiCall or "").lower()
    return any(keyword.lower() in apiCallLower for keyword in LLM_SKIP_API_KEYWORDS)


# ============================================================
# Single-step LLM call helper
# ============================================================

def _call_llm_step(client, system_prompt, user_prompt, step_label, maxRetries=3):
    """Make one LLM call with retries. Returns parsed JSON dict."""
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt},
    ]

    print(
        f"--- Prompt Sent to LLM ({step_label}) ---\n"
        f"[system]\n{system_prompt}\n\n"
        f"[user]\n{user_prompt}\n"
        "---------------------------\n\n"
    )

    for attempt in range(1, maxRetries + 1):
        try:
            response = client.chat.completions.create(
                model="MiniMax-M2.7",
                messages=messages,
                temperature=0,
                max_tokens=8192,
            )
            print_llm_raw_response(response, f"{step_label} 原始返回 (attempt {attempt})")
            result = parseStructuredResponse(response)
            print(f"[{step_label}] Response: {result}")
            return result
        except Exception as e:
            if _llm_debug_enabled():
                print(f"\n[FIND_DIFFER_LLM_DEBUG] {step_label} 异常: {type(e).__name__}: {e}")
                traceback.print_exc()
            if attempt == maxRetries:
                print(f"Error during LLM invocation ({step_label}): {e}")
                return {"changes": []}
            print(f"[{step_label}] Attempt {attempt} failed: {e}. Retrying...")


# ============================================================
# Orchestrator — 4 sequential LLM calls
# ============================================================

## Call LLM to analyze all parameter changes using OpenAI official SDK
## 调用 LLM 分析所有参数变更（使用 OpenAI 官方 SDK；提示词内嵌 JSON Schema），带 docstring 上下文
#
#  将分析拆分为 4 步串联请求：
#    Step 1: 按名匹配 → posChange / typeChange / pos2key / key2pos
#    Step 2: 未匹配位置参数 → rename / delete
#    Step 3: 未匹配关键字参数 → rename / delete
#    Step 4: 剩余新参数 → replace / addPos / addKey
#
#  @param apiCall The full API call string (will be cleaned to remove parameters)
#  @param oldVersion The old library version
#  @param newVersion The new library version
#  @param oldPara The old parameter string
#  @param newPara The new parameter string
#  @param oldDocstring The old version docstring
#  @param newDocstring The new version docstring
#  @param maxRetries Maximum number of retry attempts (default: 3)
#  @return AllParameterChanges dict from LLM
def callLLM(apiCall, oldVersion, newVersion, oldPara, newPara,
            oldDocstring, newDocstring, maxRetries=3):
    if shouldSkipLLM(apiCall):
        print(f"[LLM-RuleString] Skip LLM invocation for API: {apiCall}")
        return {"changes": []}

    client = OpenAI()

    oldPos, oldKey = para2Obj(oldPara)
    newPos, newKey = para2Obj(newPara)
    oldPosParaNum = len(oldPos)

    oldPosJSON = convertParamsToJSON(oldPos, True)
    oldKeyJSON = convertParamsToJSON(oldKey, False)
    newPosJSON = convertParamsToJSON(newPos, True)
    newKeyJSON = convertParamsToJSON(newKey, False)

    allOldJSON = oldPosJSON + oldKeyJSON
    allNewJSON = newPosJSON + newKeyJSON

    all_changes = []

    if _llm_debug_enabled():
        print(
            "\n[FIND_DIFFER_LLM_DEBUG] 已开启 (4-step pipeline)。"
            "关闭: unset FIND_DIFFER_LLM_DEBUG\n"
        )

    # ── Step 1: Match by Name ──────────────────────────────────
    step1_user = STEP1_HUMAN_TEMPLATE.format(
        fullApiName=apiCall,
        oldVersion=oldVersion,
        newVersion=newVersion,
        oldParamsJSON=json.dumps(allOldJSON, indent=2, ensure_ascii=False),
        newParamsJSON=json.dumps(allNewJSON, indent=2, ensure_ascii=False),
        oldDocstring=oldDocstring,
        newDocstring=newDocstring,
        outputSchema=json.dumps(step1_schema, indent=2, ensure_ascii=False),
    )
    step1_result = _call_llm_step(
        client, STEP1_SYSTEM_PROMPT, step1_user, "Step1-NameMatch", maxRetries,
    )
    step1_changes = step1_result.get("changes", [])
    all_changes.extend(step1_changes)

    matched_old_names = {c["param_name"] for c in step1_changes}
    unmatched_old_pos = [p for p in oldPosJSON if p["name"] not in matched_old_names]
    unmatched_old_key = [p for p in oldKeyJSON if p["name"] not in matched_old_names]
    unmatched_new_pos = [p for p in newPosJSON if p["name"] not in matched_old_names]
    unmatched_new_key = [p for p in newKeyJSON if p["name"] not in matched_old_names]

    print(
        f"[Pipeline] After Step 1: "
        f"matched={len(step1_changes)}, "
        f"unmatched_old_pos={len(unmatched_old_pos)}, "
        f"unmatched_old_key={len(unmatched_old_key)}, "
        f"unmatched_new_pos={len(unmatched_new_pos)}, "
        f"unmatched_new_key={len(unmatched_new_key)}"
    )

    # ── Step 2: Handle Remaining Positional Parameters ─────────
    if unmatched_old_pos:
        step2_user = STEP2_HUMAN_TEMPLATE.format(
            fullApiName=apiCall,
            oldVersion=oldVersion,
            newVersion=newVersion,
            unmatchedOldPosJSON=json.dumps(unmatched_old_pos, indent=2, ensure_ascii=False),
            unmatchedNewPosJSON=json.dumps(unmatched_new_pos, indent=2, ensure_ascii=False),
            oldDocstring=oldDocstring,
            newDocstring=newDocstring,
            outputSchema=json.dumps(step2_schema, indent=2, ensure_ascii=False),
        )
        step2_result = _call_llm_step(
            client, STEP2_SYSTEM_PROMPT, step2_user, "Step2-Positional", maxRetries,
        )
    else:
        step2_result = {"changes": []}
        print("[Step2-Positional] No unmatched old positional parameters — skipped.")

    step2_changes = step2_result.get("changes", [])
    all_changes.extend(step2_changes)

    renamed_to_pos = {c["rename"] for c in step2_changes if c.get("rename")}
    remaining_new_pos = [p for p in unmatched_new_pos if p["name"] not in renamed_to_pos]

    freed_old_pos = []
    for c in step2_changes:
        if c.get("delete"):
            freed_old_pos.append({
                "param_name": c["param_name"],
                "position": c["position"],
                "reason": "delete",
            })
    for c in step1_changes:
        if c.get("posChange") is not None:
            freed_old_pos.append({
                "param_name": c["param_name"],
                "position": c["position"],
                "reason": "posChange",
            })

    # ── Step 3: Handle Remaining Keyword Parameters ────────────
    if unmatched_old_key:
        step3_user = STEP3_HUMAN_TEMPLATE.format(
            fullApiName=apiCall,
            oldVersion=oldVersion,
            newVersion=newVersion,
            unmatchedOldKeyJSON=json.dumps(unmatched_old_key, indent=2, ensure_ascii=False),
            unmatchedNewKeyJSON=json.dumps(unmatched_new_key, indent=2, ensure_ascii=False),
            oldDocstring=oldDocstring,
            newDocstring=newDocstring,
            outputSchema=json.dumps(step3_schema, indent=2, ensure_ascii=False),
        )
        step3_result = _call_llm_step(
            client, STEP3_SYSTEM_PROMPT, step3_user, "Step3-Keyword", maxRetries,
        )
    else:
        step3_result = {"changes": []}
        print("[Step3-Keyword] No unmatched old keyword parameters — skipped.")

    step3_changes = step3_result.get("changes", [])
    all_changes.extend(step3_changes)

    renamed_to_key = {c["rename"] for c in step3_changes if c.get("rename")}
    remaining_new_key = [p for p in unmatched_new_key if p["name"] not in renamed_to_key]

    # ── Step 4: Handle Remaining New Parameters ────────────────
    if remaining_new_pos or remaining_new_key:
        step4_user = STEP4_HUMAN_TEMPLATE.format(
            fullApiName=apiCall,
            oldVersion=oldVersion,
            newVersion=newVersion,
            oldPosParaNum=str(oldPosParaNum),
            freedOldPosJSON=json.dumps(freed_old_pos, indent=2, ensure_ascii=False),
            remainingNewPosJSON=json.dumps(remaining_new_pos, indent=2, ensure_ascii=False),
            remainingNewKeyJSON=json.dumps(remaining_new_key, indent=2, ensure_ascii=False),
            outputSchema=json.dumps(step4_schema, indent=2, ensure_ascii=False),
        )
        step4_result = _call_llm_step(
            client, STEP4_SYSTEM_PROMPT, step4_user, "Step4-NewParams", maxRetries,
        )
    else:
        step4_result = {"changes": []}
        print("[Step4-NewParams] No remaining new parameters — skipped.")

    step4_changes = step4_result.get("changes", [])
    all_changes.extend(step4_changes)

    # ── Merge entries that share the same (param_name, position) ──
    merged = {}
    for c in all_changes:
        key = (c["param_name"], c["position"])
        if key in merged:
            merged[key].update(c)
        else:
            merged[key] = dict(c)
    merged_changes = list(merged.values())

    print(f"[Pipeline] Final merged changes: {len(merged_changes)}")
    return {"changes": merged_changes}


## Convert LLM structured output to the standard ansDict format
## 将 LLM 的结构化输出转换为标准的 ansDict 格式
#
#  The ansDict format uses (param_name, position) tuples as keys
#  and change operation dicts as values, matching changeAnalyze.py output.
#  允许的标签: addKey, addPos, delete, key2pos, pos2key, posChange, rename, replace, typeChange
#
#  @param llmResult The LLM output dict (AllParameterChanges schema)
#  @return ansDict The standard answer dictionary sorted by position
def convertLLMResultToAnsDict(llmResult):
    """
    将 LLM 返回的结构化结果转换为与 changeAnalyze.findDiffer 一致的 ansDict 格式。
    """
    updateDict = {}

    for change in llmResult.get('changes', []):
        paramName = change.get('param_name')
        position = change.get('position')
        key = (paramName, position)

        changeDict = {}

        if change.get('delete'):
            changeDict['delete'] = 1
        if change.get('typeChange'):
            changeDict['typeChange'] = change['typeChange']
        if change.get('rename'):
            changeDict['rename'] = change['rename']
        if change.get('posChange') is not None:
            changeDict['posChange'] = change['posChange']
        if change.get('pos2key'):
            changeDict['pos2key'] = change['pos2key']
        if change.get('key2pos'):
            changeDict['key2pos'] = change['key2pos']
        if change.get('replace'):
            changeDict['replace'] = change['replace']
        if change.get('addPos'):
            changeDict['addPos'] = change['addPos']
        if change.get('addKey'):
            changeDict['addKey'] = change['addKey']

        updateDict[key] = changeDict

    ansDict = dict(sorted(updateDict.items(), key=lambda it: it[0][1]))
    return ansDict



## Pure LLM-based difference analysis with docstring context (RuleString mode)
## 纯 LLM 差异分析（规则+Docstring模式）
#
#  在 findDifferRule 的基础上，将 docstring 信息加入 prompt，
#  让 LLM 能够参考文档字符串来更准确地理解参数语义。
#
#  @param oldPara The old parameter string from current version
#  @param newPara The new parameter string from target version
#  @param context A dictionary containing all additional context for LLM analysis:
#         - apiCall: The API call name
#         - oldVersion: The old library version (e.g., "networkx@1.5")
#         - newVersion: The new library version (e.g., "networkx@1.6")
#         - jsonPrefix: The prefix path for JSON files (default: ".")
#         - oldMatchDict: The old version match dictionary (optional, may contain docstring)
#         - newMatchDict: The new version match dictionary (optional, may contain docstring)
#  @return ansDict The final answer dictionary
def findDifferRuleString(oldPara, newPara, context):
    apiCall = context.get('apiCall')
    print(f"\n[RuleString] Analyzing API: {apiCall}")
    oldVersion = context.get('oldVersion')
    newVersion = context.get('newVersion')
    oldMatchDict = context.get('oldMatchDict')
    newMatchDict = context.get('newMatchDict')

    oldDocstring = getDocstring(oldMatchDict)
    newDocstring = getDocstring(newMatchDict)
    print(f"[RuleString] Docstrings found (Old: {bool(oldDocstring)}, New: {bool(newDocstring)})")

    print(f"[RuleString] Sending parameters to LLM (4-step pipeline) with docstring context...")
    llmResult = callLLM(apiCall, oldVersion, newVersion, oldPara, newPara,
                        oldDocstring, newDocstring)

    ansDict = convertLLMResultToAnsDict(llmResult)
    print(f"[RuleString] Final answer built. Result keys: {list(ansDict.keys())}")

    return ansDict
