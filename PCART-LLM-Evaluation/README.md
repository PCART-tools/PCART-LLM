# PCART-LLM-Evaluation

Language / 语言: [中文](README.md) | **English**

This directory contains standalone helper scripts used during the PCART-LLM experiment evaluation process.

## Directory Structure

```text
PCART-LLM-Evaluation/
├── README.md
├── README_en.md
└── Scripts/
    ├── clean_result_jsons.py
    └── compare_with_groundtruth.py
```

## Scripts

### clean_result_jsons.py

`clean_result_jsons.py` cleans JSON files in an experiment result directory according to a manifest file. The script recursively scans the target directory, keeps only the target JSON files listed in the manifest, and identifies extra JSON files. It always preserves `.txt` files, so experiment logs and text notes will not be deleted.

By default, the script runs in dry-run mode and does not delete files. After confirming that the output statistics are correct, add the `--apply` option to perform the actual cleanup.

Preview the files that would be cleaned:

```bash
python Scripts/clean_result_jsons.py <result-directory-to-clean> <manifest.json>
```

Delete the extra JSON files:

```bash
python Scripts/clean_result_jsons.py <result-directory-to-clean> <manifest.json> --apply
```

When some JSON files listed in the manifest are missing from the result directory, but you still want to delete the extra JSON files:

```bash
python Scripts/clean_result_jsons.py <result-directory-to-clean> <manifest.json> --allow-missing --apply
```

Common output fields:

- `keep_listed`: number of JSON files listed in the manifest that should be kept
- `actual_json`: number of JSON files actually counted in the target directory
- `extra_json`: number of extra JSON files in the target directory that are not matched by the manifest
- `missing_json`: number of JSON files listed in the manifest but missing from the target directory
- `deleted_json`: number of JSON files actually deleted
- `remaining_json`: number of JSON files remaining after cleanup
- `txt_count`: number of TXT files in the target directory

### compare_with_groundtruth.py

`compare_with_groundtruth.py` generates a semantic split comparison report for PCBench results. The script reads the `files.delete_or_rename` field from the semantic split source file, classifies matched samples as "semantically related" samples, and classifies unmatched prediction JSON files as "semantically unrelated" samples. It then compares the two subsets separately against the DictOnly ground truth and generates a Markdown report.

During comparison, the script reads `repairLst[].repairDict` from each result JSON file as the prediction and strictly compares it with the expected repair result in the corresponding ground truth JSON file. The final report includes the sample count, correct count, error count, and accuracy for the semantically related subset, the semantically unrelated subset, and the merged result, and it lists the incorrect samples and reasons for each difference.

Use the default ground truth path:

```bash
python Scripts/compare_with_groundtruth.py <result-directory> <semantic-split-source.json> <output-report.md>
```

Specify the ground truth directory explicitly:

```bash
python Scripts/compare_with_groundtruth.py <result-directory> <semantic-split-source.json> <output-report.md> --gt-root <groundtruth-directory>
```

Arguments:

- `<result-directory>`: experiment result directory to compare; this can be either the experiment root directory or the `Benchmark` directory directly
- `<semantic-split-source.json>`: manifest file containing the `files.delete_or_rename` field, such as `json_contains_delete_or_rename_report.json`
- `<output-report.md>`: path of the generated Markdown report
- `--gt-root`: optional argument used to specify the DictOnly ground truth directory; when omitted, the built-in default path in the script is used

## Usage Recommendation

Use `clean_result_jsons.py` first to clean experiment outputs and make sure the result directory only keeps the JSON files that should be included in the statistics. Then use `compare_with_groundtruth.py` to generate the semantic split comparison report. This avoids redundant result files affecting the statistics and ensures that the sample set in the final report is consistent with the experiment setup.

## Note

Note that `compare_with_groundtruth.py` does not support comparing changes to parameters with randomly changing default values. Users need to fix those cases manually.
