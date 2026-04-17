# main.diff Notes

Language / 语言: [中文](README.md) | **English**

The patch file in the root of this directory is [main.diff](./main.diff). It describes the differences from [PCART-original/main.py](../PCART-original/main.py) to [PCART-modified/main.py](../PCART-modified/main.py).

## Patch Coverage

- Adds construction of `context` before calling `isCompatible()`, passing additional information such as `apiCall`, old and new version numbers, matching results, `jsonPrefix`, and configuration path.
- Extends report output from a single `Report/` directory to simultaneous archiving under `Log/Report/{subDir}/`.
- Extends error log output from a single `Report/{projName}_fixed_log.txt` file to also write into `Log/findDiffer/{subDir}/`.

## Patch Significance

- Makes `main.py` the unified entry point for both the default rule mode and the LLM mode.
- Saves results and error logs by configuration directory hierarchy, which is better suited for batch experiments and issue tracing.
