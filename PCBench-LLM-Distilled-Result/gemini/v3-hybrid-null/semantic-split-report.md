# PCBench-LLM-Distilled 语义切分对比报告

## 说明

- 切分依据：`PCBench-LLM-Distilled-groundTruth/Semantic-Related-contains_delete_or_rename.json`
- 命中 `PCBench-LLM-Distilled-groundTruth/Semantic-Related-contains_delete_or_rename.json` 的样例记为“语义相关”
- 未命中的样例记为“语义不相关”
- 对比 ground truth：`PCBench-LLM-Distilled-groundTruth/PCBench-LLM-Distilled-groundTruth-DictOnly`
- 判定规则：结果 JSON 中的 `repairLst[].repairDict` 与对应 ground truth JSON 完全一致则记为“正确”，否则记为“错误”
- 本次修正：对 `aiohttp.ClientSession` 样例中的 `json_serialize=<function ... at 0x...>` 仅忽略运行时地址；除地址外仍需完全一致

## 总体统计

| 部分 | 样例数 | 正确 | 错误 | 正确率 |
| --- | ---: | ---: | ---: | ---: |
| 语义相关 | 171 | 167 | 4 | 97.66% |
| 语义不相关 | 113 | 113 | 0 | 100.00% |
| 合并后 | 284 | 280 | 4 | 98.59% |

## 语义相关

| 指标 | 数值 |
| --- | ---: |
| 样例数 | 171 |
| 正确 | 167 |
| 错误 | 4 |
| 正确率 | 97.66% |

### 错误样例

| 序号 | 样例路径 | 错误类型 | 差异说明 |
| --- | --- | --- | --- |
| 1 | `networkx/clustering@1.5-1.6/clustering#1YY/nx.clustering_G_@1.5-1.6_L4_tempLst1.json` | mismatch | item 0 field (weighted, 2) mismatch: pred={'rename': 'weight'}, gt={'delete': 1, 'replace': 'weight=None'} |
| 2 | `networkx/degree@1.5-1.6/degree#1YY/G.degree__@1.5-1.6_L4_tempLst1.json` | mismatch | item 0 field (weighted, 1) mismatch: pred={'rename': 'weight'}, gt={'delete': 1, 'replace': 'weight=None'} |
| 3 | `networkx/networkx.closeness_centrality@1.4-1.5/networkx.closeness_centrality#1YY/nx.closeness_centrality_G_@1.4-1.5_L3_tempLst1.json` | mismatch | item 0 field (weighted_edges, 2) mismatch: pred={'rename': 'distance'}, gt={'delete': 1, 'replace': 'distance=None'} |
| 4 | `networkx/spectral_layout@1.5-1.6/spectral_layout#1YY/nx.spectral_layout_G_@1.5-1.6_L4_tempLst1.json` | mismatch | item 0 field (weighted, 2) mismatch: pred={'rename': 'weight'}, gt={'delete': 1, 'replace': "weight='weight'"} |

## 语义不相关

| 指标 | 数值 |
| --- | ---: |
| 样例数 | 113 |
| 正确 | 113 |
| 错误 | 0 |
| 正确率 | 100.00% |

### 错误样例

| 序号 | 样例路径 | 错误类型 | 差异说明 |
| --- | --- | --- | --- |
| 1 | 无 | 无 | 本部分没有错误样例 |
