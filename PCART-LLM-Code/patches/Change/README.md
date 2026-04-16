# changeAnalyze.diff 说明

语言 / Language: **中文** | [English](README_en.md)

本目录中的补丁文件是 [changeAnalyze.diff](./changeAnalyze.diff)。它描述的是 [PCART-original/Change/changeAnalyze.py](../../PCART-original/Change/changeAnalyze.py) 到 [PCART-modified/Change/changeAnalyze.py](../../PCART-modified/Change/changeAnalyze.py) 的差异。

## 补丁覆盖内容

- 为 `findDiffer()` 和 `isCompatible()` 增加 `context` 参数，支持额外上下文透传。
- 当 `context` 中包含 LLM 所需字段时，在 `findDiffer()` 内改为委托到 `LLM/findDiffer/` 模块。
- 增加 `repairLst` 落盘逻辑，把 `tempLst1` 和 `tempLst2` 记录到 `Log/findDiffer/`。
- 将 `Log/findDiffer/` 的输出路径按配置文件所在子目录分层保存。

## 补丁意义

- 保留原有规则分析入口的同时，为 LLM 版本提供统一路由。
- 保留更多中间结果，方便做结果采集、差异定位和案例回放。
