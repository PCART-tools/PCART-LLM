# Result

Language / 语言: [中文](README_zh.md) | **English**

This directory stores result files produced by different models on the `PCBench-LLM-Distilled` dataset, together with the corresponding semantic split reports.

## Directory Description

- `claude/`, `deepseek/`, `gemini/`, `minimax/`, `qwen/`, and `default/`: result directories for different models or baselines.
- Each second-level directory corresponds to an experiment version, such as `v1-rule-null`, `v4-hybrid-string`, or `v5-hybrid-code`.
- Each experiment directory usually contains:
  - `PCBench-LLM-Distilled/`: the dataset result directory for that experiment version.
  - `semantic-split-report.md`: the semantic-related / semantic-unrelated split statistics report.

## Derived CSV Files

- `exp_data.csv`: overall accuracy summary for the main experiment settings.
- `semantic_controlled_sample_data.csv`: sample-level data for the controlled semantic / non-semantic comparison. Each row records the sample group, combined accuracy, and three complexity features (`total_params`, `changed_params`, `change_ops`) across 25 experiment runs, excluding MiniMax `v1.1` and `v2.1`.
- `semantic_controlled_feature_combinations.csv`: aggregate results for the 13 feature combinations that appear in both semantic-related and non-semantic samples. This file is used for the controlled feature-combination comparison figure.

## Current Naming Conventions

- Report files are uniformly named `semantic-split-report.md`.
- Dataset directories are uniformly named `PCBench-LLM-Distilled`.
- Report titles uniformly use `PCBench-LLM-Distilled 语义切分对比报告`.
- Absolute paths are no longer kept in report descriptions.
- The `config` fields in `Benchmark/**/*.json` have been updated to `PCBench-LLM-Distilled/...`.

## Current Scale

- There are 27 `semantic-split-report.md` files.
- There are 27 `PCBench-LLM-Distilled` experiment result directories.

## Usage Recommendations

- If you continue batch renaming or replacing content, keep the report name, dataset directory name, and `config` field paths consistent.
- If new experiment versions are added later, follow the existing directory hierarchy and naming style to make cross-version comparison and batch processing easier.
