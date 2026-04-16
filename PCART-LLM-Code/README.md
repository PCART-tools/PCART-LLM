# PCART-LLM 说明

语言 / Language: **中文** | [English](README_en.md)

本目录用于并排整理 `PCART` 原始实现与本地改动实现，方便后续逐文件对照、补充说明和人工审阅。

## 基线信息

- 当前版本修改自`PCART-tools/PCART@defc6a4`。
- `PCART-original/` 保存的是原始实现的抽取版本。
- `PCART-modified/` 保存的是改动后的实现，以及本轮新增的重要模块。

## 代码改动总览

- 在原有 `findDiffer` 规则分析链路之外，引入了 `LLM/findDiffer/` 模块，形成基于 LLM 的 `Rule` 与 `Hybrid` 两类差异分析实现，并进一步区分 `Null`、`String`、`Code` 三类语义输入方式。
- 将 `findDiffer` 的调用上下文从 `main.py` 透传到 `Change/changeAnalyze.py`，使默认规则路径和 LLM 路径可以共用统一入口。
- 在动态匹配阶段补采 `docstring` 与 `sourceCode`，为带语义信息的 LLM 版本提供输入材料。
- 增加了 `findDiffer` 结果采集能力，包括 `repairLst` 落盘、按配置目录归档日志、额外保存报告等，便于调试与批量实验。
- 新增 `Test/batch.py`，用于批量初始化与执行 Benchmark 配置，并支持进度续跑。

## 目录说明

- [PCART-original](./PCART-original): 原始实现快照，仅保留本轮确实被修改过的既有文件。
- [PCART-modified](./PCART-modified): 改动后实现快照，包含修改文件与重要新增文件。
- [patches](./patches): 与 `PCART-modified` 对应的补丁目录，使用 `.diff` 展示相对原始实现的改动。
