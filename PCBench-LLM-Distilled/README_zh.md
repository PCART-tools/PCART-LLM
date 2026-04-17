# PCBench-LLM-Distilled

语言 / Language: **中文** | [English](README.md)

用于评估 LLM Python API 兼容性检测能力的精简基准测试集。

## 数据来源

基于 `PCART-tools/PCBench@db6b54b`提取。

原始数据先按 `#1[YN][YN]` 规则为每个 API 抽取首个样例，再经过多轮清洗与筛选，得到当前目录中的处理后数据集。

## 数据集处理流程

本数据集的筛选过程如下：

1. 从原始 PCBench 中抽取得到 844 个首样例。
2. 去除 6 个因运行环境或外部依赖问题无法作为有效测试样例使用的样例，剩余 838 个。
3. 再去除 2 个无法通过动态和静态方式获取 API 信息的无效样例，剩余 836 个。
4. 在这 836 个可用样例中，只有 284 个样例在初期兼容性检查后仍需进入 `findDiffer` 处理并产出目标 JSON；其余 552 个样例在初期兼容性检查阶段即判定兼容，没有进入 `findDiffer`，因此不纳入当前处理后的数据集。

最终可以概括为：

`PCBench（抽取首样例 844） -> 838 -> 836 -> 284`

其中，当前 `Benchmark/` 目录保存的就是最终保留的 284 个样例；处理清单保存在 `PCBench-LLM-Distilled_valid_samples_and_target_jsons.json` 中。

## 当前数据集

`Benchmark/` 目录当前包含 29 个库的 284 个样例。这些样例均满足以下条件：

- 已通过前两轮无效样例剔除
- 在初期兼容性检查后确实进入了 `findDiffer`
- 在处理日志中能够对应到保留的 `target_jsons`

### 目录结构

```text
PCBench-LLM-Distilled/
├── README.md
├── README_en.md
├── Benchmark/
│   ├── <library>/                    # 如 numpy, pandas, scipy
│   │   ├── <api>@<version_range>/    # 如 numpy.array@1.20.0-1.21.0
│   │   │   └── <api>#1<label>/       # 如 numpy.array#1YY
│   │   │       ├── <api><label>.py   # 测试脚本
│   │   │       └── <target_json>.json
│   │   └── ...
│   └── ...
├── PCBench-LLM-Distilled_valid_samples_and_target_jsons.json
└── script/
    ├── download_envs.py
    └── generate_json.py
```

### 统计信息

| 库 | 样例数 | | 库 | 样例数 |
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

*完整统计: 29 个库, 284 个样例*

## 已排除的样例

### 运行环境或外部依赖导致无效的样例（6）

| 库 | 目录 | 原因 |
|----|------|------|
| gensim | `#gensim.models.wrappers.fasttext.FastText.train@2.2.0-2.3.0` | CPU 指令不兼容 (SIGILL) |
| redis | `#redis.commands.core.SortedSetCommands.zrank@4.5.5-4.6.0` | 需要 Redis 服务 |
| redis | `#zrevrank@4.5.4-4.5.5` | 需要 Redis 服务 |
| sklearn | `#sklearn.datasets.fetch_20newsgroups@0.21.3-0.22` | SSL 证书问题 |
| sklearn | `#sklearn.datasets.fetch_20newsgroups_vectorized@0.21.3-0.22` | SSL 证书问题 |
| torch | `#torch.cuda.synchronize@1.0.1-1.1.0` | 需要 NVIDIA GPU |

### 动态和静态方式获取 API 均失败的无效样例（2）

| 库 | 目录 | 原因 |
|----|------|------|
| tensorflow | `#tf.data.experimental.choose_from_datasets@2.5.3-2.6.0` | 动态和静态方式获取 API 均失败，传入 `findDiffer` 的 API 内容为空，为无效样例，所以删除 |
| tensorflow | `#tf.data.experimental.sample_from_datasets@2.5.3-2.6.0` | 动态和静态方式获取 API 均失败，传入 `findDiffer` 的 API 内容为空，为无效样例，所以删除 |

### 未进入 `findDiffer` 的样例（552）

其余未保留的样例均通过了初期兼容性检查阶段，并没有进入 `findDiffer` 进行处理，因此视为不属于当前处理后的数据集，统一排除，不再逐项列出。

## 脚本

### `script/generate_json.py`

为 `Benchmark/` 目录中的每个样例生成 JSON 配置文件。

```bash
python script/generate_json.py
```

运行时会提示输入 conda 环境目录路径，用于配置 `currentEnv` 和 `targetEnv` 字段。

### `script/download_envs.py`

从南航云盘下载预配置环境压缩包，并自动解压到指定安装路径。

支持两种模式：

- 批量下载：选择一个或多个文件夹，下载其中全部压缩包
- 选择性下载：先进入某个文件夹，再选择指定压缩包下载

```bash
python script/download_envs.py
```

运行时会提示选择下载模式、目标文件夹或文件，以及安装路径；下载完成后会自动解压，并输出成功、失败、跳过和总耗时统计。
