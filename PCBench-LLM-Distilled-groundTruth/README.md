# PCBench-LLM-Distilled-groundTruth

Language / 语言: [中文](README_zh.md) | **English**

This directory stores the `DictOnly` version of the `PCBench-LLM-Distilled` ground-truth data.

## Current Directory Structure

### `PCBench-LLM-Distilled-groundTruth-DictOnly/`

The main data directory, organized by the `library / api@version_range / sample` hierarchy.

Current statistics:

- 29 library directories
- 284 JSON files

Each JSON file is an array, and each element in the array is a repair dictionary:

```json
[
  {
    "(param, idx)": { "...": "..." }
  }
]
```

## Usage

This dataset is suitable for scenarios that only care about the repair content itself.

Comparison rules:

- Compare JSON arrays item by item in order.
- The `i`-th element corresponds to the `i`-th element.

In other words, the ground truth in this directory uses "ordered comparison" by default.

## Included Files

- `multi_entry_files.txt`
  Records 8 samples that contain multiple repair entries, together with the number of entries for each sample.
- `Semantic-Related-contains_delete_or_rename.json`
  Records statistics and the file list for semantic-related samples that hit `delete` or `rename`, which can be used for later grouped analysis.

## Note

This expected-result set includes `aiohttp.ClientSession@1.3.5-2.0.0`. The following entry represents a change that adds a keyword argument. Because the default value of this parameter changes randomly, users need to fix it manually.

```json
    "(json_serialize, 7)": {
      "addKey": "json_serialize=<functiondumpsat0x7af4f31667b8>"
    },
```
