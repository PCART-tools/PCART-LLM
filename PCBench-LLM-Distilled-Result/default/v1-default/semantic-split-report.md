# PCBench-LLM-Distilled 语义切分对比报告

## 说明

- 切分依据：`PCBench-LLM-Distilled-groundTruth/Semantic-Related-contains_delete_or_rename.json`
- 命中 `PCBench-LLM-Distilled-groundTruth/Semantic-Related-contains_delete_or_rename.json` 的样例记为“语义相关”
- 未命中的样例记为“语义不相关”
- 对比 ground truth：`PCBench-LLM-Distilled-groundTruth/PCBench-LLM-Distilled-groundTruth-DictOnly`
- 判定规则：结果 JSON 中的 `repairLst[].repairDict` 与对应 ground truth JSON 完全一致则记为“正确”，否则记为“错误”

## 总体统计

| 部分 | 样例数 | 正确 | 错误 | 正确率 |
| --- | ---: | ---: | ---: | ---: |
| 语义相关 | 171 | 159 | 12 | 92.98% |
| 语义不相关 | 113 | 113 | 0 | 100.00% |
| 合并后 | 284 | 272 | 12 | 95.77% |

## 语义相关

| 指标 | 数值 |
| --- | ---: |
| 样例数 | 171 |
| 正确 | 159 |
| 错误 | 12 |
| 正确率 | 92.98% |

### 错误样例

| 序号 | 样例路径 | 错误类型 | 差异说明 |
| --- | --- | --- | --- |
| 1 | `aiohttp/aiohttp.ClientSession@1.3.5-2.0.0/aiohttp.ClientSession#1YY/aiohttp.ClientSession__@1.3.5-2.0.0_L18_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=[], gt_only=['(json_serialize, 7)'] |
| 2 | `aiohttp/aiohttp.TCPConnector@2.3.10-3.0.0/aiohttp.TCPConnector#1YY/aiohttp.TCPConnector__@2.3.10-3.0.0_L9_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=[], gt_only=['(ssl, 7)'] |
| 3 | `gensim/gensim.models.fasttext.FastText@3.8.3-4.0.0/gensim.models.fasttext.FastText#1YY/FastText__@3.8.3-4.0.0_L2_tempLst1.json` | mismatch | item 0 field (compatible_hash, 27) mismatch: pred={'rename': 'max_final_vocab'}, gt={'delete': 1, 'replace': 'max_final_vocab=None'} |
| 4 | `networkx/average_clustering@1.5-1.6/average_clustering#1YY/nx.average_clustering_G_@1.5-1.6_L4_tempLst1.json` | mismatch | item 0 field (weighted, 1) mismatch: pred={'rename': 'nodes'}, gt={'delete': 1, 'replace': 'nodes=None'} |
| 5 | `networkx/average_neighbor_degree@1.5-1.6/average_neighbor_degree#1YY/nx.average_neighbor_degree_G_@1.5-1.6_L4_tempLst1.json` | mismatch | item 0 field (weighted, 2) mismatch: pred={'rename': 'target'}, gt={'delete': 1, 'replace': "target='out'"} |
| 6 | `networkx/clustering@1.5-1.6/clustering#1YY/nx.clustering_G_@1.5-1.6_L4_tempLst1.json` | mismatch | item 0 field (weighted, 2) mismatch: pred={'rename': 'weight'}, gt={'delete': 1, 'replace': 'weight=None'} |
| 7 | `networkx/degree@1.5-1.6/degree#1YY/G.degree__@1.5-1.6_L4_tempLst1.json` | mismatch | item 0 field (weighted, 1) mismatch: pred={'rename': 'weight'}, gt={'delete': 1, 'replace': 'weight=None'} |
| 8 | `networkx/is_isomorphic@1.5-1.6/is_isomorphic#1YY/nx.is_isomorphic_G1__G2_@1.5-1.6_L6_tempLst1.json` | mismatch | item 0 field (rtol, 3) mismatch: pred={'rename': 'edge_match'}, gt={'delete': 1, 'replace': 'edge_match=None'} |
| 9 | `networkx/networkx.closeness_centrality@1.4-1.5/networkx.closeness_centrality#1YY/nx.closeness_centrality_G_@1.4-1.5_L3_tempLst1.json` | mismatch | item 0 field (weighted_edges, 2) mismatch: pred={'rename': 'distance'}, gt={'delete': 1, 'replace': 'distance=None'} |
| 10 | `networkx/spectral_layout@1.5-1.6/spectral_layout#1YY/nx.spectral_layout_G_@1.5-1.6_L4_tempLst1.json` | mismatch | item 0 field (weighted, 2) mismatch: pred={'rename': 'weight'}, gt={'delete': 1, 'replace': "weight='weight'"} |
| 11 | `pydantic/pydantic.main.create_model@1.4-1.5/pydantic.main.create_model#1YY/create_model__DynamicModel__@1.4-1.5_L13_tempLst1.json` | mismatch | item 0 field (model_name, 0) mismatch: pred={'delete': 1, 'replace': '__model_name'}, gt={'typeChange': 'str', 'rename': '__model_name'} |
| 12 | `tensorflow/tf.data.experimental.service.DispatchServer@2.3.4-2.4.0/tf.data.experimental.service.DispatchServer#1NY/tf.data.experimental.service.DispatchServer_0_@2.3.4-2.4.0_L2_tempLst1.json` | mismatch | item 0 field (port, 0) mismatch: pred={'rename': 'config'}, gt={'delete': 1, 'replace': 'config=None'} |

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
