# map.diff 说明

语言 / Language: **中文** | [English](README.md)

本目录中的补丁文件是 [map.diff](./map.diff)。它描述的是 [PCART-original/Map/map.py](../../PCART-original/Map/map.py) 到 [PCART-modified/Map/map.py](../../PCART-modified/Map/map.py) 的差异。

## 补丁覆盖内容

- 在动态匹配成功后，把 `dynamicMatch.py` 产生的 `docstring` 与 `sourceCode` 一并写回匹配结果字典。
- 调整带语义信息的 LLM 路径的数据来源，使其优先直接使用当前匹配结果中的语义字段，而不是再次从 `_dynamicMatch.json` 读取。

## 补丁意义

- 保证旧版本和新版本的 `docstring`、`sourceCode` 不会互相串写。
- 让后续 LLM 分析看到的语义材料与当前版本严格对应。
