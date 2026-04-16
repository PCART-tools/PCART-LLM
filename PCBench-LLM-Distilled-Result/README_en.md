# Result

Language / 语言: [中文](README.md) | **English**

This directory stores result files produced by different models on the `PCBench-LLM-Distilled` dataset, together with the corresponding semantic split reports.

## Directory Description

- `claude/`, `deepseek/`, `gemini/`, `minimax/`, `qwen/`, and `default/`: result directories for different models or baselines.
- Each second-level directory corresponds to an experiment version, such as `v1-rule-null`, `v4-hybrid-string`, or `v5-hybrid-code`.
- Each experiment directory usually contains:
  - `PCBench-LLM-Distilled/`: the dataset result directory for that experiment version.
  - `semantic-split-report.md`: the semantic-related / semantic-unrelated split statistics report.

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
