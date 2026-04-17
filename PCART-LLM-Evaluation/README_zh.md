# PCART-LLM-Evaluation

语言 / Language: **中文** | [English](README_en.md)

该目录用于存放 PCART-LLM 实验评估过程中可独立运行的辅助脚本。

## 目录结构

```text
PCART-LLM-Evaluation/
├── README.md
├── README_en.md
└── Scripts/
    ├── clean_result_jsons.py
    └── compare_with_groundtruth.py
```

## 脚本说明

### clean_result_jsons.py

`clean_result_jsons.py` 用于根据 manifest 文件清理实验结果目录中的 JSON 文件。脚本会递归扫描目标目录，仅保留 manifest 中列出的目标 JSON 文件，并识别出多余 JSON 文件。脚本始终保留 `.txt` 文件，因此不会删除实验日志或文本说明。

默认情况下，脚本只执行 dry-run 预览，不会真正删除文件。确认输出统计无误后，可添加 `--apply` 参数执行实际清理。

预览将被清理的文件：

```bash
python Scripts/clean_result_jsons.py <要清理的结果目录> <manifest.json>
```

实际删除多余 JSON 文件：

```bash
python Scripts/clean_result_jsons.py <要清理的结果目录> <manifest.json> --apply
```

当 manifest 中列出的部分 JSON 在结果目录中缺失，但仍确认需要删除多余 JSON 时：

```bash
python Scripts/clean_result_jsons.py <要清理的结果目录> <manifest.json> --allow-missing --apply
```

常用输出字段含义如下：

- `keep_listed`：manifest 中列出的应保留 JSON 数量
- `actual_json`：目标目录中实际参与统计的 JSON 数量
- `extra_json`：目标目录中未被 manifest 命中的多余 JSON 数量
- `missing_json`：manifest 中列出但目标目录中缺失的 JSON 数量
- `deleted_json`：实际删除的 JSON 数量
- `remaining_json`：清理后剩余的 JSON 数量
- `txt_count`：目标目录中的 TXT 文件数量

### compare_with_groundtruth.py

`compare_with_groundtruth.py` 用于生成 PCBench 结果的语义切分比对报告。脚本读取语义切分依据文件中的 `files.delete_or_rename` 字段，将命中的样例划分为“语义相关”样例，将未命中的预测 JSON 划分为“语义不相关”样例。随后，脚本分别将两个子集与 DictOnly ground truth 进行比对，并生成 Markdown 报告。

比对时，脚本会读取结果 JSON 中的 `repairLst[].repairDict` 作为预测结果，并与对应 ground truth JSON 中的期待修复结果进行严格一致性比较。最终报告会包含语义相关、语义不相关以及合并后的样例数、正确数、错误数和正确率，并列出错误样例及差异原因。

使用默认 ground truth 路径：

```bash
python Scripts/compare_with_groundtruth.py <结果目录> <语义切分依据.json> <输出报告.md>
```

显式指定 ground truth 目录：

```bash
python Scripts/compare_with_groundtruth.py <结果目录> <语义切分依据.json> <输出报告.md> --gt-root <groundtruth目录>
```

参数说明：

- `<结果目录>`：待比对的实验结果目录，可以是实验根目录，也可以直接是 `Benchmark` 目录
- `<语义切分依据.json>`：包含 `files.delete_or_rename` 字段的 manifest 文件，例如 `json_contains_delete_or_rename_report.json`
- `<输出报告.md>`：生成的 Markdown 报告路径
- `--gt-root`：可选参数，用于指定 DictOnly ground truth 目录；省略时使用脚本内置默认路径

## 使用建议

建议先使用 `clean_result_jsons.py` 对实验输出进行清理，确保结果目录中只保留需要统计的 JSON 文件；随后再使用 `compare_with_groundtruth.py` 生成语义切分比对报告。这样可以避免冗余结果文件影响统计口径，并保证最终报告中的样例集合与实验设置一致。

## 注意

注意，`compare_with_groundtruth.py`工具不能支持带有随机变化默认值的参数的变更的对比，需要使用者自行修复。
