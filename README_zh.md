# PCART-LLM

语言 / Language: **中文** | [English](README.md)

本目录汇总了 PCART-LLM 相关的代码改动、评估数据集、期望结果、实验输出以及评估脚本。

## 目录总览

```text
PCART-LLM/
├── PCART-LLM-Code/
├── PCART-LLM-Evaluation/
├── PCBench-LLM-Distilled/
├── PCBench-LLM-Distilled-groundTruth/
└── PCBench-LLM-Distilled-Result/
```

## 子目录说明

- [PCART-LLM-Code](./PCART-LLM-Code/)：保存 `PCART` 原始实现与本地改动实现的对照版本。该目录包含 `PCART-original/`、`PCART-modified/` 和 `patches/`，用于展示基于 LLM 的 `findDiffer` 改动、批量实验支持以及相对原始实现的补丁。
- [PCBench-LLM-Distilled](./PCBench-LLM-Distilled/)：保存用于评估参数变更方法能力的API级测试集。当前 `Benchmark/` 目录包含 29 个库的 284 个保留样例，并附带样例清单与环境、配置生成脚本。
- [PCBench-LLM-Distilled-groundTruth](./PCBench-LLM-Distilled-groundTruth/)：保存 `PCBench-LLM-Distilled` 的 `DictOnly` 版本 ground truth。该目录按 `library / api@version_range / sample` 层级组织 284 个 JSON 期望结果，用于与实验输出进行严格顺序比对。
- [PCBench-LLM-Distilled-Result](./PCBench-LLM-Distilled-Result/)：保存不同模型或基线在 `PCBench-LLM-Distilled` 数据集上的实验结果。目录中包含 `claude/`、`deepseek/`、`gemini/`、`minimax/`、`qwen/` 和 `default/` 等结果分组，以及对应的语义切分报告。
- [PCART-LLM-Evaluation](./PCART-LLM-Evaluation/)：保存独立运行的评估辅助脚本，包括结果 JSON 清理脚本和语义相关 / 语义不相关切分比对报告生成脚本。


## 许可证

PCART-LLM 采用 GNU Affero 通用公共许可证 v3.0 授权。详情请参见 [LICENSE](./LICENSE)。
