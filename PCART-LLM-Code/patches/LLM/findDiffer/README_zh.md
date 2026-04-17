# LLM/findDiffer 说明

语言 / Language: **中文** | [English](README.md)

本目录保存的是本轮新增的基于 LLM 的 `findDiffer` 实现族对应的补丁文件，用于展示这些新增实现相对于“原始实现不存在该文件”这一基线的新增内容。由于这些文件在原始实现中不存在，所以对应的 `.diff` 文件补丁头会显示为从 `/dev/null` 新增。

## 命名规则

- `Rule`：表示“基于自然语言描述规则策略”的实现。核心思路是把原有规则逻辑描述成 prompt，让模型直接输出参数变更结果。
- `Hybrid`：表示“融合策略”的实现。核心思路是先走一轮硬规则预处理，再把剩余难点交给 LLM 判断。
- `Null`：表示不向 LLM 提供额外语义信息，只给参数列表。
- `String`：表示提供 `docstring` 作为语义信息。
- `Code`：表示提供 `source code` 作为语义信息。
- `V4`：表示使用 OpenAI Python SDK 的 `response_format` 接受 `json_schema`。
- `V5`：表示把字符串化后的 `json_schema` 直接放入 user prompt 中，让模型按文本约束输出。
- `Split`：表示把原来一次性完成的 LLM 请求拆分为多步串联请求，用更小的阶段逐步完成差异分析。

## 特殊文件

- [findDifferRuleNullSplitV5.diff](./findDifferRuleNullSplitV5.diff)：对应 `findDifferRuleNullSpilitV5.py` 的新增补丁。在 `findDifferRuleNullV5.py` 的基础上，把原来一次性完成的 prompt 和 `json_schema` 分成多步串联请求，用来降低单次请求的复杂度，并把分析拆成更清楚的阶段。
- [findDifferRuleStringSplitV5.diff](./findDifferRuleStringSplitV5.diff)：对应 `findDifferRuleStringSplitV5.py` 的新增补丁。在 `findDifferRuleStringV5.py` 的基础上加入多步串联请求流程，并继续提供 `docstring` 作为语义信息，用来让每一步在更聚焦的上下文中完成参数变更判断。

## 各文件特点

- [findDifferHybridNullV4.diff](./findDifferHybridNullV4.diff)：融合策略，不提供语义信息，使用 `response_format + json_schema`。
- [findDifferHybridNullV5.diff](./findDifferHybridNullV5.diff)：融合策略，不提供语义信息，使用 prompt 内嵌 schema。
- [findDifferHybridStringV4.diff](./findDifferHybridStringV4.diff)：融合策略，提供 `docstring`，使用 `response_format + json_schema`。
- [findDifferHybridStringV5.diff](./findDifferHybridStringV5.diff)：融合策略，提供 `docstring`，使用 prompt 内嵌 schema。
- [findDifferHybridCodeV4.diff](./findDifferHybridCodeV4.diff)：融合策略，提供 `source code`，使用 `response_format + json_schema`。
- [findDifferHybridCodeV5.diff](./findDifferHybridCodeV5.diff)：融合策略，提供 `source code`，使用 prompt 内嵌 schema。
- [findDifferRuleNullV4.diff](./findDifferRuleNullV4.diff)：规则策略，不提供语义信息，使用 `response_format + json_schema`。
- [findDifferRuleNullV5.diff](./findDifferRuleNullV5.diff)：规则策略，不提供语义信息，使用 prompt 内嵌 schema。
- [findDifferRuleStringV4.diff](./findDifferRuleStringV4.diff)：规则策略，提供 `docstring`，使用 `response_format + json_schema`。
- [findDifferRuleStringV5.diff](./findDifferRuleStringV5.diff)：规则策略，提供 `docstring`，使用 prompt 内嵌 schema。
