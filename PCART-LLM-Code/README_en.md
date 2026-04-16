# PCART-LLM Notes

Language / 语言: [中文](README.md) | **English**

This directory organizes the original `PCART` implementation and the locally modified implementation side by side, making later file-by-file comparison, supplementary documentation, and manual review easier.

## Baseline Information

- The current version is modified from `PCART-tools/PCART@defc6a4`.
- `PCART-original/` stores the extracted snapshot of the original implementation.
- `PCART-modified/` stores the modified implementation and the important modules added in this round.

## Code Change Overview

- Introduced the `LLM/findDiffer/` module outside the original `findDiffer` rule-analysis path, forming two categories of LLM-based difference analysis implementations: `Rule` and `Hybrid`. These are further divided into three semantic input modes: `Null`, `String`, and `Code`.
- Passed the invocation context of `findDiffer` from `main.py` into `Change/changeAnalyze.py`, allowing the default rule path and the LLM path to share a unified entry point.
- Collected `docstring` and `sourceCode` during the dynamic matching stage to provide input material for LLM versions that use semantic information.
- Added `findDiffer` result collection capabilities, including persisting `repairLst`, archiving logs by configuration directory, and saving additional reports, which helps debugging and batch experiments.
- Added `Test/batch.py` for batch initialization and execution of Benchmark configurations, with support for resuming progress.

## Directory Description

- [PCART-original](./PCART-original): snapshot of the original implementation, retaining only existing files that were actually modified in this round.
- [PCART-modified](./PCART-modified): snapshot of the modified implementation, containing modified files and important newly added files.
- [patches](./patches): patch directory corresponding to `PCART-modified`, using `.diff` files to show changes relative to the original implementation.
