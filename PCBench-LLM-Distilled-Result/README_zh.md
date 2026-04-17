# Result

语言 / Language: **中文** | [English](README.md)

这个目录保存了不同模型在 `PCBench-LLM-Distilled` 数据集上的结果文件，以及对应的语义切分报告。

## 目录说明

- `claude/`、`deepseek/`、`gemini/`、`minimax/`、`qwen/`、`default/`：不同模型或基线的结果目录。
- 每个二级目录对应一个实验版本，例如 `v1-rule-null`、`v4-hybrid-string`、`v5-hybrid-code`。
- 每个实验目录下通常包含：
  - `PCBench-LLM-Distilled/`：该实验版本对应的数据集结果目录。
  - `semantic-split-report.md`：语义相关 / 语义不相关切分统计报告。

## 当前命名约定

- 报告文件统一命名为 `semantic-split-report.md`
- 数据集目录统一命名为 `PCBench-LLM-Distilled`
- 报告标题统一使用 `PCBench-LLM-Distilled 语义切分对比报告`
- 报告说明中不再保留绝对路径
- `Benchmark/**/*.json` 中的 `config` 字段已同步更新为 `PCBench-LLM-Distilled/...`

## 当前规模

- 共有 27 份 `semantic-split-report.md`
- 共有 27 个 `PCBench-LLM-Distilled` 实验结果目录

## 使用建议

- 若继续批量重命名或替换内容，优先保持报告名、数据集目录名和 `config` 字段路径一致。
- 若后续新增实验版本，建议沿用现有目录层级与命名风格，方便横向比较和批量处理。
