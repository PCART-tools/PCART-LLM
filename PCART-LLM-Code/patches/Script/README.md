# dynamicMatch.diff 说明

语言 / Language: **中文** | [English](README_en.md)

本目录中的补丁文件是 [dynamicMatch.diff](./dynamicMatch.diff)。它描述的是 [PCART-original/Script/dynamicMatch.py](../../PCART-original/Script/dynamicMatch.py) 到 [PCART-modified/Script/dynamicMatch.py](../../PCART-modified/Script/dynamicMatch.py) 的差异。

## 补丁覆盖内容

- 在动态匹配成功时，新增提取 `inspect.getdoc(eval(api))` 与 `inspect.getsource(eval(api))` 的逻辑。
- 将得到的 `docstring` 与 `sourceCode` 一并写入序列化后的 `matchDict`。

## 补丁意义

- 让动态匹配阶段同时产出签名信息和语义辅助材料。
- 为 `String` 与 `Code` 两类 LLM 差异分析实现提供稳定、近源的输入。
