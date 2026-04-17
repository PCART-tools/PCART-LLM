# PCBench-LLM-Distilled

Language / 语言: [中文](README.md) | **English**

A distilled benchmark dataset for evaluating LLM-based Python API compatibility detection.

## Data Source

Extracted from `PCART-tools/PCBench@db6b54b`.

The original data was first processed by extracting the first sample for each API according to the `#1[YN][YN]` rule. After multiple rounds of cleaning and filtering, the processed dataset in the current directory was obtained.

## Dataset Processing Workflow

The filtering process for this dataset is as follows:

1. Extracted 844 first samples from the original PCBench.
2. Removed 6 samples that could not be used as valid test samples because of runtime environment or external dependency issues, leaving 838 samples.
3. Removed another 2 invalid samples whose API information could not be obtained dynamically or statically, leaving 836 samples.
4. Among these 836 usable samples, only 284 still needed to enter `findDiffer` after the initial compatibility check and produced target JSON files. The remaining 552 samples were judged compatible during the initial compatibility check and did not enter `findDiffer`, so they are not included in the current processed dataset.

The final process can be summarized as:

`PCBench (844 extracted first samples) -> 838 -> 836 -> 284`

The current `Benchmark/` directory stores the final 284 retained samples. The processing list is stored in `PCBench-LLM-Distilled_valid_samples_and_target_jsons.json`.

## Current Dataset

The `Benchmark/` directory currently contains 284 samples from 29 libraries. These samples all satisfy the following conditions:

- They passed the first two rounds of invalid sample removal.
- They actually entered `findDiffer` after the initial compatibility check.
- They can be matched to retained `target_jsons` in the processing logs.

### Directory Structure

```text
PCBench-LLM-Distilled/
├── README.md
├── README_en.md
├── Benchmark/
│   ├── <library>/                    # e.g., numpy, pandas, scipy
│   │   ├── <api>@<version_range>/    # e.g., numpy.array@1.20.0-1.21.0
│   │   │   └── <api>#1<label>/       # e.g., numpy.array#1YY
│   │   │       ├── <api><label>.py   # test script
│   │   │       └── <target_json>.json
│   │   └── ...
│   └── ...
├── PCBench-LLM-Distilled_valid_samples_and_target_jsons.json
└── script/
    ├── download_envs.py
    └── generate_json.py
```

### Statistics

| Library | Samples | | Library | Samples |
|---|---:|---|---|---:|
| pandas | 46 | | plotly | 34 |
| sklearn | 26 | | polars | 25 |
| networkx | 23 | | scipy | 22 |
| matplotlib | 14 | | gensim | 12 |
| tornado | 12 | | numpy | 11 |
| rich | 10 | | sympy | 9 |
| httpx | 6 | | tensorflow | 6 |
| dask | 5 | | keras | 4 |
| aiohttp | 3 | | flask | 2 |
| click | 2 | | PIL | 2 |
| django | 2 | | xgboost | 1 |
| torch | 1 | | transformers | 1 |
| fastapi | 1 | | loguru | 1 |
| spacy | 1 | | jax | 1 |
| pydantic | 1 | |  |  |

*Full statistics: 29 libraries, 284 samples*

## Excluded Samples

### Invalid Samples Caused by Runtime Environment or External Dependencies (6)

| Library | Directory | Reason |
|----|------|------|
| gensim | `#gensim.models.wrappers.fasttext.FastText.train@2.2.0-2.3.0` | CPU instruction incompatibility (SIGILL) |
| redis | `#redis.commands.core.SortedSetCommands.zrank@4.5.5-4.6.0` | Redis service required |
| redis | `#zrevrank@4.5.4-4.5.5` | Redis service required |
| sklearn | `#sklearn.datasets.fetch_20newsgroups@0.21.3-0.22` | SSL certificate issue |
| sklearn | `#sklearn.datasets.fetch_20newsgroups_vectorized@0.21.3-0.22` | SSL certificate issue |
| torch | `#torch.cuda.synchronize@1.0.1-1.1.0` | NVIDIA GPU required |

### Invalid Samples Whose API Information Failed to Be Retrieved Both Dynamically and Statically (2)

| Library | Directory | Reason |
|----|------|------|
| tensorflow | `#tf.data.experimental.choose_from_datasets@2.5.3-2.6.0` | API information failed to be retrieved both dynamically and statically; the API content passed into `findDiffer` was empty, making it an invalid sample, so it was removed |
| tensorflow | `#tf.data.experimental.sample_from_datasets@2.5.3-2.6.0` | API information failed to be retrieved both dynamically and statically; the API content passed into `findDiffer` was empty, making it an invalid sample, so it was removed |

### Samples That Did Not Enter `findDiffer` (552)

The remaining unretained samples all passed the initial compatibility check and did not enter `findDiffer` for processing. Therefore, they are treated as outside the current processed dataset, excluded uniformly, and not listed one by one.

## Scripts

### `script/generate_json.py`

Generates JSON configuration files for each sample in the `Benchmark/` directory.

```bash
python script/generate_json.py
```

During execution, it prompts for the conda environment directory path, which is used to configure the `currentEnv` and `targetEnv` fields.

### `script/download_envs.py`

Downloads preconfigured environment archives from the NUAA cloud drive and automatically extracts them to the specified installation path.

Two modes are supported:

- Batch download: select one or more folders and download all archives inside them.
- Selective download: enter a folder first, then select specific archives to download.

```bash
python script/download_envs.py
```

During execution, it prompts for the download mode, target folder or file, and installation path. After downloading, it automatically extracts the archives and outputs statistics for successful, failed, skipped items, and total elapsed time.
