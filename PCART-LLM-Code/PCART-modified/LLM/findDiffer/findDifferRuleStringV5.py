## @package findDifferRuleString
#  Pure LLM-based difference analysis for API parameter changes, enhanced with docstring context
#  使用纯 LLM 进行 API 参数变更差异分析，并引入 docstring 上下文
#
#  String/docstring 上下文版本：与 findDifferRuleNullV5 对齐（OpenAI SDK + 提示内 JSON Schema），
#  不使用 LangChain；在 Null 版本基础上将 docstring 信息加入 prompt，
#  让 LLM 能够参考文档字符串来更准确地理解参数语义。

import os
import re
import json
import traceback
from openai import OpenAI

from Change.changeAnalyze import para2Obj, isDifferType, Update
from Tool.tool import getFileName, removeParameter

all_parameter_changes_schema = {
    "title": "AllParameterChanges",
    "description": "Complete analysis result of parameter changes between two API versions.",
    "type": "object",
    "properties": {
        "changes": {
            "type": "array",
            "description": (
                "List of changes for ALL parameters (both old parameters that changed "
                "and newly added parameters). Allowed labels per entry: "
                "addKey, addPos, delete, key2pos, pos2key, posChange, rename, replace, typeChange."
            ),
            "items": {
                "type": "object",
                "properties": {
                    "param_name": {
                        "type": "string",
                        "description": (
                            "Name of the parameter (old name for existing/deleted parameters, "
                            "new name for newly added parameters)"
                        ),
                    },
                    "position": {
                        "type": "integer",
                        "description": (
                            "Position index (old position for existing/deleted parameters, "
                            "new position for newly added parameters. 0-based, excluding self/cls)"
                        ),
                    },
                    "delete": {
                        "type": "boolean",
                        "description": "true if the parameter was deleted in the new version",
                    },
                    "rename": {
                        "type": "string",
                        "description": "New name if the parameter was renamed",
                    },
                    "typeChange": {
                        "type": "string",
                        "description": "New type annotation string if the type changed",
                    },
                    "posChange": {
                        "type": "integer",
                        "description": "New position index if the position changed (positional params only)",
                    },
                    "pos2key": {
                        "type": "string",
                        "description": "Parameter name if it changed from positional to keyword",
                    },
                    "key2pos": {
                        "type": "string",
                        "description": "Parameter name if it changed from keyword to positional",
                    },
                    "replace": {
                        "type": "string",
                        "description": (
                            "Replacement parameter string (e.g. 'newname' or 'newname=defaultval') "
                            "if the parameter at this position was replaced by a completely different parameter"
                        ),
                    },
                    "addPos": {
                        "type": "string",
                        "description": "For newly added positional parameters: 'name' or 'name=default_value'",
                    },
                    "addKey": {
                        "type": "string",
                        "description": "For newly added keyword parameters: 'name' or 'name=default_value'",
                    },
                },
                "required": ["param_name", "position"],
            },
        }
    },
    "required": ["changes"],
}


SYSTEM_PROMPT_TEMPLATE = """You are an API parameter change analysis assistant. Your task is to analyze ALL parameter changes between different API versions and output a complete structured result.

<task>
Compare the old and new API parameter lists, and determine what happened to each old parameter and whether any new parameters were added. You must analyze ALL changes. Use the provided docstrings to better understand the semantics of each parameter.
</task>

<analysis_rules>

## Step 1: Match by Name
For each old parameter (both positional and keyword), check if a parameter with the **same name** exists in the new version:
- If found among the same type (positional→positional or keyword→keyword):
  - Check if the **position** changed (only for **parameter_type:positional**). If so, record `posChange` = new position.
  - Check if the **type annotation**(data_type) changed (see type compatibility rules). If so, record `typeChange` = new type string.
  - This parameter is matched; do NOT mark it as deleted or renamed.
  - If the parameter has NO changes at all, you still MUST include it with no change fields set.
- If an old **positional** parameter name is found in the new **keyword** parameters: record `pos2key` = parameter name (and also check typeChange).
- If an old **keyword** parameter name is found in the new **positional** parameters: record `key2pos` = parameter name (and also check typeChange).

## Step 2: Handle Remaining (Unmatched) Positional Parameters
For old positional parameters not matched in Step 1:
- If a new positional parameter exists at the **same position** with a **compatible type** (including when either type is empty), and based on the docstrings and parameter semantics, the new parameter is semantically the same parameter with a name change, or the new parameter extends the functionality of the old one with full backward compatibility, consider it a **rename**. Record `rename` = new parameter name.
- Otherwise, mark the old parameter as **deleted** (`delete` = 1).

## Step 3: Handle Remaining (Unmatched) Keyword Parameters
For old keyword parameters not matched in Step 1 or 2:
- If a remaining new keyword parameter has the **same type**, and based on the docstrings and parameter semantics, the new parameter is semantically the same parameter with a name change, or the new parameter extends the functionality of the old one with full backward compatibility, consider it a **rename**. Record `rename` = new parameter name.
- Otherwise, mark the old parameter as **deleted** (`delete` = 1).

## Step 4: Handle Remaining New Parameters
After all old parameters have been processed:
- For remaining new **positional** parameters:
  - IMPORTANT: If its position index is within the range [0, old_positional_count - 1], it is a **replacement** for the deleted old parameter at that position. Record `replace` on the corresponding old parameter's entry (the one marked as deleted at that position). Format: "name" or "name=default_value". Note that `replace` always follows `delete` or `posChange`.
  - Otherwise(which means that for the remaining new **positional** parameters, you must choose either `replace` or `addPos`; the two are mutually exclusive), it is a newly **added positional** parameter. Create a new entry with `addPos` = "name" or "name=default_value" (make sure to set `param_name` and `position` to this new parameter's name and position).
- For remaining new **keyword** parameters: they are newly **added keyword** parameters. Create a new entry with `addKey` = "name" or "name=default_value" (make sure to set `param_name` and `position` to this new parameter's name and position).

</analysis_rules>

<type_compatibility>
Two types are considered compatible (no type change) if:
- They are identical strings
- Either one is empty/missing
- The old type is a subset of the new type (e.g., `int` is compatible with `Union[int, float]`)
</type_compatibility>

<important_notes>
- Position indices start from 0 and exclude `self`/`cls`.
- Parameters before `*` are positional; parameters after `*` are keyword-only.
- `**kwargs` type parameters should be excluded from keyword parameter lists.
- When recording `typeChange`, use the full new type annotation string.
- When recording `replace`, `addPos`, or `addKey`, format as "name" or "name=default_value".
- The allowed change labels are ONLY: addKey, addPos, delete, key2pos, pos2key, posChange, rename, replace, typeChange.
- You MUST include ALL old parameters in the output, even those with no changes (they should have no change fields set), each parameter may appear only once.
- The output should be sorted by position.
- Use the docstrings to understand parameter semantics when deciding renames vs deletes.
</important_notes>
"""

HUMAN_PROMPT_TEMPLATE = """<general_information>

### API call
{fullApiName}

### Library and version
- old：{oldVersion}
- new：{newVersion}

### Old positional parameter count
{oldPosParaNum}

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

Only include a change field (delete, rename, typeChange, posChange, pos2key, key2pos, replace, addPos, addKey) when it actually applies. For unchanged parameters, include only `param_name` and `position`.

If no parameters changed at all, output: {{"changes": []}}
</output_format>

Based on the analysis rules, please analyze ALL parameter changes between the old and new API versions. Consider parameter names, positions, types, docstrings, and your knowledge of the library.
"""


def buildPromptMessages(apiCall, oldVersion, newVersion, oldPosParaNum,
                        oldParamsJSON, newParamsJSON,
                        oldDocstring, newDocstring):
    schema_str = json.dumps(all_parameter_changes_schema, indent=2, ensure_ascii=False)
    user_prompt = HUMAN_PROMPT_TEMPLATE.format(
        fullApiName=apiCall,
        oldVersion=oldVersion,
        newVersion=newVersion,
        oldPosParaNum=str(oldPosParaNum),
        oldParamsJSON=oldParamsJSON,
        newParamsJSON=newParamsJSON,
        oldDocstring=oldDocstring,
        newDocstring=newDocstring,
        outputSchema=schema_str,
    )
    return [
        {"role": "system", "content": SYSTEM_PROMPT_TEMPLATE},
        {"role": "user", "content": user_prompt},
    ]


def _llm_debug_enabled():
    # 当环境变量 FIND_DIFFER_LLM_DEBUG=1 / true / yes / on 时，开启 LLM 原始响应调试输出。
    v = os.environ.get("FIND_DIFFER_LLM_DEBUG", "").strip().lower()
    return v in ("1", "true", "yes", "on")


def _openai_response_to_dict(obj):
    # 将 SDK 返回对象转为可 JSON 序列化的 dict，便于打印原始返回结构。
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
    # 打印 chat.completions.create 返回的完整结构，与 HTTP 响应体字段保持一致，便于排查空 content 等问题。
    # 仅当 FIND_DIFFER_LLM_DEBUG 开启时输出。
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
    # 从可能包含 <think>...</think> 和 markdown 代码块的文本中提取 JSON。
    # 适配 MiniMax 等思维链模型，它们会在 content 里混入推理过程和 markdown 格式。
    stripped = re.sub(r"<think>[\s\S]*?</think>", "", text)
    stripped = re.sub(r"<think>[\s\S]*$", "", stripped)
    stripped = stripped.strip()

    m = re.search(r"```(?:json)?\s*\n([\s\S]*?)```", stripped)
    if m:
        stripped = m.group(1).strip()

    return json.loads(stripped)


def parseStructuredResponse(response):
    # Normalize OpenAI chat completion structured output to a plain dict.
    # 兼容标准 JSON 输出和包含 <think> / markdown 代码块的思维链模型输出。
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


## Call LLM to analyze all parameter changes using OpenAI official SDK
## 调用 LLM 分析所有参数变更（使用 OpenAI 官方 SDK；提示词内嵌 JSON Schema），带 docstring 上下文
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
    # 调用 LLM 分析全部参数变更，并额外引入 docstring 上下文。
    # 与 hybrid 模式不同，这里会将全部参数一次性发送给 LLM 分析。
    if shouldSkipLLM(apiCall):
        print(f"[LLM-RuleString] Skip LLM invocation for API: {apiCall}")
        return {"changes": []}

    client = OpenAI(
        # api_key=apiKey,
        # base_url=baseUrl,
    )

    oldPos, oldKey = para2Obj(oldPara)
    newPos, newKey = para2Obj(newPara)
    oldPosParaNum = len(oldPos)

    oldParamsJSON = convertParamsToJSON(oldPos, True) + convertParamsToJSON(oldKey, False)
    newParamsJSON = convertParamsToJSON(newPos, True) + convertParamsToJSON(newKey, False)

    old_params_str = json.dumps(oldParamsJSON, indent=2, ensure_ascii=False)
    new_params_str = json.dumps(newParamsJSON, indent=2, ensure_ascii=False)

    messages = buildPromptMessages(
        apiCall,
        oldVersion,
        newVersion,
        oldPosParaNum,
        old_params_str,
        new_params_str,
        oldDocstring,
        newDocstring,
    )

    print(
        "--- Prompt Sent to LLM ---\n"
        f"[system]\n{SYSTEM_PROMPT_TEMPLATE}\n\n"
        f"[user]\n{messages[1]['content']}\n"
        "---------------------------\n\n"
    )

    if _llm_debug_enabled():
        print(
            "\n[FIND_DIFFER_LLM_DEBUG] 已开启：将打印每次 API 返回的完整结构化对象。"
            "关闭: unset FIND_DIFFER_LLM_DEBUG\n"
        )

    for attempt in range(1, maxRetries + 1):
        try:
            response = client.chat.completions.create(
                model="MiniMax-M2.7",
                messages=messages,
                temperature=0,
                max_tokens=8192,
            )
            print_llm_raw_response(response, f"chat.completions 原始返回 (attempt {attempt})")
            result = parseStructuredResponse(response)
            print(result)
            print(f"[LLM-RuleString] Response received: {result}")
            return result
        except Exception as e:
            if _llm_debug_enabled():
                print(f"\n[FIND_DIFFER_LLM_DEBUG] 本次异常: {type(e).__name__}: {e}")
                traceback.print_exc()
            if attempt == maxRetries:
                print(f"Error during LLM invocation: {e}")
                return {"changes": []}
            print(f"[LLM] Attempt {attempt} failed: {e}. Retrying...")


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
    # 将 LLM 返回的结构化结果转换为与 changeAnalyze.findDiffer 一致的 ansDict 格式。
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

    print(f"[RuleString] Sending all parameters to LLM for full analysis with docstring context...")
    llmResult = callLLM(apiCall, oldVersion, newVersion, oldPara, newPara,
                        oldDocstring, newDocstring)

    ansDict = convertLLMResultToAnsDict(llmResult)
    print(f"[RuleString] Final answer built. Result keys: {list(ansDict.keys())}")

    return ansDict
