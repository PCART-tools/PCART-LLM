# batch.diff 说明

语言 / Language: **中文** | [English](README_en.md)

本目录中的补丁文件是 [batch.diff](./batch.diff)。它描述的是新增文件 [PCART-modified/Test/batch.py](../../PCART-modified/Test/batch.py) 的完整内容，因此补丁头会显示为从 `/dev/null` 新增。

## 补丁覆盖内容

- 新增 `init` 与 `run` 两类批量任务入口。
- 扫描 Benchmark 配置，生成 `batch_config.json` 与 `batch_progress.json`。
- 支持按进度续跑，而不是每次都从头重新执行。

## 补丁意义

- 提供了轻量、可续跑的批量实验入口。
- 与新增的日志分层保存配合后，更适合做大规模 Benchmark 验证。
