# PCART-LLM

Language / 语言: [中文](README_zh.md) | **English**

This directory brings together the PCART-LLM code changes, evaluation dataset, ground-truth data, experiment outputs, and evaluation scripts.

## Directory Overview

```text
PCART-LLM/
├── PCART-LLM-Code/
├── PCART-LLM-Evaluation/
├── PCBench-LLM-Distilled/
├── PCBench-LLM-Distilled-groundTruth/
└── PCBench-LLM-Distilled-Result/
```

## Subdirectory Description

- [PCART-LLM-Code](./PCART-LLM-Code/): stores the side-by-side snapshots of the original `PCART` implementation and the locally modified implementation. It contains `PCART-original/`, `PCART-modified/`, and `patches/`, showing the LLM-based `findDiffer` changes, batch experiment support, and patches relative to the original implementation.
- [PCBench-LLM-Distilled](./PCBench-LLM-Distilled/): stores the API-level test set for evaluating the capabilities of parameter-change methods. The current `Benchmark/` directory contains 284 retained samples from 29 libraries, together with the sample manifest and scripts for environment download and JSON configuration generation.
- [PCBench-LLM-Distilled-groundTruth](./PCBench-LLM-Distilled-groundTruth/): stores the `DictOnly` ground truth for `PCBench-LLM-Distilled`. It organizes 284 expected-result JSON files by the `library / api@version_range / sample` hierarchy and is used for strict ordered comparison against experiment outputs.
- [PCBench-LLM-Distilled-Result](./PCBench-LLM-Distilled-Result/): stores result files produced by different models or baselines on the `PCBench-LLM-Distilled` dataset. It includes result groups such as `claude/`, `deepseek/`, `gemini/`, `minimax/`, `qwen/`, and `default/`, together with the corresponding semantic split reports.
- [PCART-LLM-Evaluation](./PCART-LLM-Evaluation/): stores standalone evaluation helper scripts, including the result JSON cleanup script and the semantic-related / semantic-unrelated split comparison report generator.
