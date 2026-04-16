# PCBench-LLM-Distilled-groundTruth

语言 / Language: **中文** | [English](README_en.md)

这个目录保存 `PCBench-LLM-Distilled` ground-truth 数据， `DictOnly` 版本。

## 当前目录结构

### `PCBench-LLM-Distilled-groundTruth-DictOnly/`

主数据目录，按 `library / api@version_range / sample` 的层级组织。

当前统计：

- 29 个库目录
- 284 个 JSON 文件

每个 JSON 文件都是一个数组，数组中的每个元素是一个修复字典：

```json
[
  {
    "(param, idx)": { "...": "..." }
  }
]
```

## 使用方式

这个数据集适合只关心修复内容本身的场景。

对比规则：

- 直接按 JSON 数组顺序逐项比较
- 第 `i` 个元素对应第 `i` 个元素

也就是说，这个目录中的 ground truth 默认采用“按顺序比较”的方式。

## 附带文件

- `multi_entry_files.txt`
  记录了 8 个包含多个修复条目的样例，以及每个样例对应的条目数量。
- `Semantic-Related-contains_delete_or_rename.json`
  记录语义相关样例中命中 `delete` 或 `rename` 的统计与文件清单，可用于后续分组分析。

## 注意

本期望结果中，包含`aiohttp.ClientSession@1.3.5-2.0.0`，其中的这条表示变更为新增关键字参数，由于该参数默认值会发生变化，使用者要自行修复。

```json
    "(json_serialize, 7)": {
      "addKey": "json_serialize=<functiondumpsat0x7af4f31667b8>"
    },
```
