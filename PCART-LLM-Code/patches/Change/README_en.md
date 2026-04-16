# changeAnalyze.diff Notes

Language / 语言: [中文](README.md) | **English**

The patch file in this directory is [changeAnalyze.diff](./changeAnalyze.diff). It describes the differences from [PCART-original/Change/changeAnalyze.py](../../PCART-original/Change/changeAnalyze.py) to [PCART-modified/Change/changeAnalyze.py](../../PCART-modified/Change/changeAnalyze.py).

## Patch Coverage

- Adds a `context` parameter to `findDiffer()` and `isCompatible()` to support passing additional context.
- When `context` contains the fields required by the LLM, `findDiffer()` delegates to the `LLM/findDiffer/` module.
- Adds logic for persisting `repairLst`, recording `tempLst1` and `tempLst2` into `Log/findDiffer/`.
- Saves output paths under `Log/findDiffer/` by the subdirectory of the configuration file.

## Patch Significance

- Provides a unified route for the LLM version while preserving the original rule-analysis entry point.
- Preserves more intermediate results, making result collection, difference localization, and case replay easier.
