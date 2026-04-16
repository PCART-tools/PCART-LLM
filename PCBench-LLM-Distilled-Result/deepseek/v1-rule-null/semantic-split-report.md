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
| 语义相关 | 171 | 89 | 82 | 52.05% |
| 语义不相关 | 113 | 11 | 102 | 9.73% |
| 合并后 | 284 | 100 | 184 | 35.21% |

## 语义相关

| 指标 | 数值 |
| --- | ---: |
| 样例数 | 171 |
| 正确 | 89 |
| 错误 | 82 |
| 正确率 | 52.05% |

### 错误样例

| 序号 | 样例路径 | 错误类型 | 差异说明 |
| --- | --- | --- | --- |
| 1 | `aiohttp/aiohttp.BaseConnector@0.8.1-0.8.2/aiohttp.BaseConnector#1YY/aiohttp.BaseConnector__@0.8.1-0.8.2_L2_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(keepalive_timeout, 2)'], gt_only=[] |
| 2 | `aiohttp/aiohttp.ClientSession@1.3.5-2.0.0/aiohttp.ClientSession#1YY/aiohttp.ClientSession__@1.3.5-2.0.0_L18_tempLst1.json` | mismatch | item 0 field (conn_timeout, 16) mismatch: pred={'addKey': 'conn_timeout'}, gt={'addKey': 'conn_timeout=None'} |
| 3 | `aiohttp/aiohttp.TCPConnector@2.3.10-3.0.0/aiohttp.TCPConnector#1YY/aiohttp.TCPConnector__@2.3.10-3.0.0_L9_tempLst1.json` | mismatch | item 0 field (enable_cleanup_closed, 14) mismatch: pred={'posChange': 14}, gt={} |
| 4 | `click/click.secho@6.7-7.0/click.secho#1YY/click.secho__Hello__Click___@6.7-7.0_L2_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(message, 0)'], gt_only=[] |
| 5 | `dask/dask.dataframe.read_parquet@2022.4.1-2022.4.2/dask.dataframe.read_parquet#1YY/dd.read_parquet__._example.parquet__@2022.4.1-2022.4.2_L2_tempLst1.json` | mismatch | item 0 field (gather_statistics, 7) mismatch: pred={'delete': 1, 'replace': 'calculate_divisions'}, gt={'rename': 'calculate_divisions'} |
| 6 | `gensim/gensim.models.doc2vec.Doc2Vec.similarity_unseen_docs@4.0.1-4.1.0/gensim.models.doc2vec.Doc2Vec.similarity_unseen_docs#1YY/model.similarity_unseen_docs_doc_words1__doc_words2_@4.0.1-4.1.0_L7_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(epochs, 4)'], gt_only=[] |
| 7 | `gensim/gensim.models.fasttext.FastText@3.8.3-4.0.0/gensim.models.fasttext.FastText#1YY/FastText__@3.8.3-4.0.0_L2_tempLst1.json` | mismatch | item 0 field (compatible_hash, 27) mismatch: pred={'delete': 1, 'replace': 'max_final_vocab'}, gt={'delete': 1, 'replace': 'max_final_vocab=None'} |
| 8 | `gensim/gensim.models.hdpmodel.HdpModel.print_topics@0.13.1-0.13.2/gensim.models.hdpmodel.HdpModel.print_topics#1YY/hdp.print_topics__@0.13.1-0.13.2_L7_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(num_topics, 0)', '(num_words, 1)'], gt_only=[] |
| 9 | `httpx/URL@0.13.3-0.14.0/URL#1YY/httpx.URL_url_str_@0.13.3-0.14.0_L4_tempLst1.json` | mismatch | item 0 field (params, 2) mismatch: pred={'typeChange': "Union[ForwardRef('QueryParams'),Mapping[str,Union[str,int,float,, gt={'posChange': 1} |
| 10 | `httpx/client.send@0.19.0-0.20.0/client.send#1YY/client.send_request_@0.19.0-0.20.0_L6_tempLst1.json` | mismatch | item 0 field (allow_redirects, 4) mismatch: pred={'delete': 1, 'rename': 'follow_redirects'}, gt={'rename': 'follow_redirects'} |
| 11 | `httpx/httpx.AsyncClient@0.11.1-0.12.0/httpx.AsyncClient#1YY/httpx.AsyncClient__@0.11.1-0.12.0_L3_tempLst1.json` | mismatch | item 0 field (trust_env, 16) mismatch: pred={'posChange': 15}, gt={} |
| 12 | `httpx/httpx.delete@0.7.4-0.7.5/httpx.delete#1YY/delete__https___example.com_resource__@0.7.4-0.7.5_L2_tempLst1.json` | mismatch | item 0 field (allow_redirects, 10) mismatch: pred={'posChange': 7}, gt={} |
| 13 | `jax/jax.experimental.jax2tf.convert@0.4.12-0.4.13/jax.experimental.jax2tf.convert#1YY/jax2tf.convert_sum_of_squares_@0.4.12-0.4.13_L7_tempLst1.json` | mismatch | item 0 field (enable_xla, 4) mismatch: pred={'typeChange': 'bool'}, gt={} |
| 14 | `keras/ReduceLROnPlateau@2.1.5-2.1.6/ReduceLROnPlateau#1YY/ReduceLROnPlateau__@2.1.5-2.1.6_L9_tempLst1.json` | mismatch | item 0 field (epsilon, 5) mismatch: pred={'delete': 1, 'replace': 'min_delta'}, gt={'rename': 'min_delta'} |
| 15 | `loguru/loguru.logger.configure@0.3.2-0.4.0/loguru.logger.configure#1YY/logger.configure__@0.3.2-0.4.0_L2_tempLst1.json` | mismatch | item 0 field (patch, 4) mismatch: pred={'delete': 1, 'rename': 'patcher'}, gt={'rename': 'patcher'} |
| 16 | `matplotlib/matplotlib.collections.AsteriskPolygonCollection.set_offset_transform@3.5.3-3.6.0/matplotlib.collections.AsteriskPolygonCollection.set_offset_transform#1YY/collection.set_offset_transform_transOffset___plt.gca__.transData_@3.5.3-3.6.0_L5_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(offset_transform, 0)'], gt_only=[] |
| 17 | `networkx/average_clustering@1.5-1.6/average_clustering#1YY/nx.average_clustering_G_@1.5-1.6_L4_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(nodes, 1)'], gt_only=[] |
| 18 | `networkx/average_neighbor_degree@1.5-1.6/average_neighbor_degree#1YY/nx.average_neighbor_degree_G_@1.5-1.6_L4_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(source, 1)', '(target, 2)'], gt_only=['(weight, 4)'] |
| 19 | `networkx/average_shortest_path_length@1.4-1.5/average_shortest_path_length#1YY/nx.average_shortest_path_length_G_@1.4-1.5_L4_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(weight, 1)'], gt_only=[] |
| 20 | `networkx/betweenness_centrality_source@1.4-1.5/betweenness_centrality_source#1YY/nx.betweenness_centrality_source_G_@1.4-1.5_L4_tempLst1.json` | mismatch | item 0 field (weighted_edges, 2) mismatch: pred={'delete': 1, 'replace': 'weight'}, gt={'rename': 'weight'} |
| 21 | `networkx/closeness_vitality@1.4-1.5/closeness_vitality#1YY/nx.closeness_vitality_G_@1.4-1.5_L4_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(weight, 2)'], gt_only=[] |
| 22 | `networkx/clustering@1.5-1.6/clustering#1YY/nx.clustering_G_@1.5-1.6_L4_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(weight, 2)'], gt_only=[] |
| 23 | `networkx/degree@1.5-1.6/degree#1YY/G.degree__@1.5-1.6_L4_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(weight, 1)'], gt_only=[] |
| 24 | `networkx/edge_betweenness_centrality_subset@1.4-1.5/edge_betweenness_centrality_subset#1YY/nx.edge_betweenness_centrality_subset_G__sources__targets_@1.4-1.5_L6_tempLst1.json` | mismatch | item 0 field (weighted_edges, 4) mismatch: pred={'delete': 1, 'replace': 'weight=None'}, gt={'rename': 'weight'} |
| 25 | `networkx/geographical_threshold_graph@2.0-2.1/geographical_threshold_graph#1YY/nx.geographical_threshold_graph_10__0.1_@2.0-2.1_L2_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(p_dist, 6)'], gt_only=[] |
| 26 | `networkx/is_isomorphic@1.5-1.6/is_isomorphic#1YY/nx.is_isomorphic_G1__G2_@1.5-1.6_L6_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(edge_match, 3)', '(node_match, 2)'], gt_only=[] |
| 27 | `networkx/networkx.betweenness_centrality@1.4-1.5/networkx.betweenness_centrality#1YY/nx.betweenness_centrality_G_@1.4-1.5_L3_tempLst1.json` | mismatch | item 0 field (weighted_edges, 2) mismatch: pred={'delete': 1, 'replace': 'weight=None'}, gt={'rename': 'weight'} |
| 28 | `networkx/networkx.closeness_centrality@1.4-1.5/networkx.closeness_centrality#1YY/nx.closeness_centrality_G_@1.4-1.5_L3_tempLst1.json` | mismatch | item 0 field (weighted_edges, 2) mismatch: pred={'delete': 1, 'replace': 'distance'}, gt={'delete': 1, 'replace': 'distance=None'} |
| 29 | `networkx/shortest_path@1.4-1.5/shortest_path#1YY/nx.shortest_path_G_@1.4-1.5_L4_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(weight, 3)'], gt_only=[] |
| 30 | `networkx/shortest_path_length@1.4-1.5/shortest_path_length#1YY/nx.shortest_path_length_G_@1.4-1.5_L4_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(weight, 3)'], gt_only=[] |
| 31 | `networkx/spectral_layout@1.5-1.6/spectral_layout#1YY/nx.spectral_layout_G_@1.5-1.6_L4_tempLst1.json` | mismatch | item 0 field (weighted, 2) mismatch: pred={'delete': 1, 'replace': 'weight'}, gt={'delete': 1, 'replace': "weight='weight'"} |
| 32 | `numpy/numpy.fix@1.12.1-1.13.0/numpy.fix#1YY/np.fix_x_@1.12.1-1.13.0_L6_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(out, 1)'], gt_only=[] |
| 33 | `numpy/numpy.genfromtxt@1.9.3-1.10.0/numpy.genfromtxt#1YY/np.genfromtxt_f_@1.9.3-1.10.0_L4_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(max_rows, 21)'], gt_only=[] |
| 34 | `numpy/numpy.histogram2d@1.23.5-1.24.0/numpy.histogram2d#1YY/np.histogram2d_x__y_@1.23.5-1.24.0_L4_tempLst1.json` | mismatch | item 0 field (normed, 4) mismatch: pred={'delete': 1, 'replace': 'density'}, gt={'delete': 1} |
| 35 | `numpy/numpy.histogram@1.23.5-1.24.0/numpy.histogram#1YY/np.histogram_a_@1.23.5-1.24.0_L8_tempLst1.json` | mismatch | item 0 field (weights, 4) mismatch: pred={'posChange': 4}, gt={} |
| 36 | `numpy/numpy.isneginf@1.12.1-1.13.0/numpy.isneginf#1YY/np.isneginf_x_@1.12.1-1.13.0_L6_tempLst1.json` | mismatch | item 0 field (y, 1) mismatch: pred={'delete': 1, 'replace': 'out'}, gt={'rename': 'out'} |
| 37 | `numpy/numpy.isposinf@1.12.1-1.13.0/numpy.isposinf#1YY/np.isposinf_x_@1.12.1-1.13.0_L6_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(out, 1)'], gt_only=[] |
| 38 | `pandas/DataFrame.between_time@1.5.3-2.0.0/DataFrame.between_time#1YY/ts.between_time__0_15____0_45__@1.5.3-2.0.0_L4_tempLst1.json` | mismatch | item 0 field (axis, 5) mismatch: pred={'typeChange': "'Axis\|None'", 'posChange': 3}, gt={'posChange': 3} |
| 39 | `pandas/DataFrame.groupby@1.5.3-2.0.0/DataFrame.groupby#1YY/df.groupby___Animal___@1.5.3-2.0.0_L3_tempLst1.json` | mismatch | item 0 field (group_keys, 5) mismatch: pred={'typeChange': "'bool'"}, gt={'typeChange': 'bool'} |
| 40 | `pandas/DataFrame.set_axis@1.5.3-2.0.0/DataFrame.set_axis#1YY/df.set_axis___a____b____c___@1.5.3-2.0.0_L3_tempLst1.json` | mismatch | item 0 field (copy, 4) mismatch: pred={'typeChange': "'bool\|None'", 'posChange': 3}, gt={'typeChange': 'bool\|None'} |
| 41 | `pandas/DataFrame.take@1.5.3-2.0.0/DataFrame.take#1YY/df.take__0__3__@1.5.3-2.0.0_L4_tempLst1.json` | mismatch | item 0 field (axis, 1) mismatch: pred={'typeChange': "'Axis'"}, gt={} |
| 42 | `pandas/DataFrame.to_excel@1.5.3-2.0.0/DataFrame.to_excel#1YY/df1.to_excel__._output.xlsx__@1.5.3-2.0.0_L3_tempLst1.json` | mismatch | item 0 field (encoding, 12) mismatch: pred={'delete': 1, 'replace': 'inf_rep'}, gt={'delete': 1} |
| 43 | `pandas/Series.groupby@1.5.3-2.0.0/Series.groupby#1YY/ser.groupby___a____b____a____b___@1.5.3-2.0.0_L3_tempLst1.json` | mismatch | item 0 field (group_keys, 5) mismatch: pred={'typeChange': "'bool'"}, gt={'typeChange': 'bool'} |
| 44 | `pandas/Series.set_axis@1.5.3-2.0.0/Series.set_axis#1YY/s.set_axis___a____b____c___@1.5.3-2.0.0_L3_tempLst1.json` | mismatch | item 0 field (copy, 4) mismatch: pred={'typeChange': "'bool\|None'", 'posChange': 3}, gt={'typeChange': 'bool\|None'} |
| 45 | `pandas/Timestamp@1.5.3-2.0.0/Timestamp#1YY/pd.Timestamp__2017-01-01T12__@1.5.3-2.0.0_L2_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(nanosecond, 10)', '(tz, 11)', '(unit, 12)'], gt_only=[] |
| 46 | `pandas/bdate_range@1.5.3-2.0.0/bdate_range#1YY/pd.bdate_range__1_1_2018____1_08_2018__@1.5.3-2.0.0_L2_tempLst1.json` | mismatch | item 0 field (freq, 3) mismatch: pred={'typeChange': "'Frequency'"}, gt={} |
| 47 | `pandas/date_range@1.5.3-2.0.0/date_range#1YY/pd.date_range__1_1_2018____1_08_2018__@1.5.3-2.0.0_L2_tempLst1.json` | mismatch | item 0 field (closed, 7) mismatch: pred={'delete': 1, 'replace': 'inclusive'}, gt={'delete': 1} |
| 48 | `pandas/pandas.DataFrame.resample@1.5.3-2.0.0/pandas.DataFrame.resample#1YY/DataFrame.resample__3T__@1.5.3-2.0.0_L4_tempLst1.json` | mismatch | item 0 field (group_keys, 12) mismatch: pred={'typeChange': "'bool'", 'posChange': 10}, gt={'typeChange': 'bool', 'posChange': 10} |
| 49 | `pandas/pandas.Series.resample@1.5.3-2.0.0/pandas.Series.resample#1YY/series.resample__3T__@1.5.3-2.0.0_L4_tempLst1.json` | mismatch | item 0 field (group_keys, 12) mismatch: pred={'typeChange': "'bool'", 'posChange': 10}, gt={'typeChange': 'bool', 'posChange': 10} |
| 50 | `pandas/read_csv@1.5.3-2.0.0/read_csv#1YY/pd.read_csv__._dev.csv__@1.5.3-2.0.0_L2_tempLst1.json` | mismatch | item 0 field (cache_dates, 30) mismatch: pred={'posChange': 28}, gt={} |
| 51 | `pandas/testing.assert_extension_array_equal@1.5.3-2.0.0/testing.assert_extension_array_equal#1YY/tm.assert_extension_array_equal_b__c_@1.5.3-2.0.0_L5_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(obj, 7)'], gt_only=[] |
| 52 | `pandas/testing.assert_frame_equal@1.5.3-2.0.0/testing.assert_frame_equal#1YY/assert_frame_equal_df1__df1_@1.5.3-2.0.0_L5_tempLst1.json` | mismatch | item 0 field (atol, 16) mismatch: pred={'typeChange': "'float'", 'posChange': 15}, gt={'posChange': 15} |
| 53 | `pandas/testing.assert_index_equal@1.5.3-2.0.0/testing.assert_index_equal#1YY/tm.assert_index_equal_a__b_@1.5.3-2.0.0_L5_tempLst1.json` | mismatch | item 0 field (check_less_precise, 4) mismatch: pred={'delete': 1, 'replace': 'check_exact'}, gt={'delete': 1} |
| 54 | `pandas/testing.assert_series_equal@1.5.3-2.0.0/testing.assert_series_equal#1YY/tm.assert_series_equal_a__b_@1.5.3-2.0.0_L5_tempLst1.json` | mismatch | item 0 field (atol, 14) mismatch: pred={'typeChange': "'float'", 'posChange': 13}, gt={'posChange': 13} |
| 55 | `polars/polars.DataFrame.drop@0.14.17-0.14.18/polars.DataFrame.drop#1YY/df.drop__B__@0.14.17-0.14.18_L3_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(columns, 0)'], gt_only=[] |
| 56 | `polars/polars.DataFrame.fill_nan@0.16.18-0.17.0/polars.DataFrame.fill_nan#1YY/df.fill_nan_99_@0.16.18-0.17.0_L3_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(value, 0)'], gt_only=[] |
| 57 | `polars/polars.DataFrame.sample@0.16.18-0.17.0/polars.DataFrame.sample#1YY/df.sample__@0.16.18-0.17.0_L3_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(fraction, 2)'], gt_only=[] |
| 58 | `polars/polars.Expr.map_dict@0.16.18-0.17.0/polars.Expr.map_dict#1YY/pl.col__country_code__.map_dict_country_code_dict_@0.16.18-0.17.0_L4_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(return_dtype, 3)'], gt_only=[] |
| 59 | `polars/polars.Expr.reshape@0.16.18-0.17.0/polars.Expr.reshape#1YY/pl.col__foo__.reshape__3__3__@0.16.18-0.17.0_L2_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(dimensions, 0)'], gt_only=[] |
| 60 | `polars/polars.Expr.str.contains@0.16.18-0.17.0/polars.Expr.str.contains#1YY/a.str.contains__AA__@0.16.18-0.17.0_L3_tempLst1.json` | mismatch | item 3 keys mismatch: pred_only=['(literal, 0)'], gt_only=[] |
| 61 | `polars/polars.Expr.str.ends_with@0.16.18-0.17.0/polars.Expr.str.ends_with#1YY/a.str.ends_with__go__@0.16.18-0.17.0_L3_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(suffix, 0)'], gt_only=[] |
| 62 | `polars/polars.Expr.str.strip@0.16.18-0.17.0/polars.Expr.str.strip#1YY/context.str.strip__@0.16.18-0.17.0_L4_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(characters, 0)'], gt_only=[] |
| 63 | `polars/polars.expr.str.strptime@0.17.15-0.18.0/polars.expr.str.strptime#1YY/a.str.strptime_pl.Date_@0.17.15-0.18.0_L4_tempLst1.json` | mismatch | item 0 field (utc, 6) mismatch: pred={'typeChange': 'bool\|None'}, gt={} |
| 64 | `rich/rich.syntax.Syntax@10.16.2-11.0.0/rich.syntax.Syntax#1YY/Syntax__print__hello_world______python__@10.16.2-11.0.0_L2_tempLst1.json` | mismatch | item 0 field (lexer_name, 1) mismatch: pred={'delete': 1, 'replace': 'lexer'}, gt={'rename': 'lexer'} |
| 65 | `rich/traceback.install@7.0.0-7.1.0/traceback.install#1YY/install__@7.0.0-7.1.0_L3_tempLst1.json` | mismatch | item 0 field (extra_lines, 4) mismatch: pred={'posChange': 3}, gt={} |
| 66 | `scipy/scipy.linalg.solve_banded@1.8.1-1.9.0/scipy.linalg.solve_banded#1YY/solve_banded_l_and_u__ab__b_@1.8.1-1.9.0_L6_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(check_finite, 5)'], gt_only=['(check_finite, 6)'] |
| 67 | `scipy/scipy.sparse.linalg.minres@0.19.1-1.0.0/scipy.sparse.linalg.minres#1YY/minres_A__b_@0.19.1-1.0.0_L6_tempLst1.json` | mismatch | item 0 field (xtype, 6) mismatch: pred={'delete': 1, 'replace': 'M'}, gt={'delete': 1} |
| 68 | `scipy/scipy.sparse.linalg.qmr@0.19.1-1.0.0/scipy.sparse.linalg.qmr#1YY/qmr_A__b_@0.19.1-1.0.0_L6_tempLst1.json` | mismatch | item 0 field (xtype, 5) mismatch: pred={'delete': 1, 'replace': 'M1'}, gt={'delete': 1} |
| 69 | `scipy/scipy.stats.rv_discrete.expect@0.16.1-0.17.0/scipy.stats.rv_discrete.expect#1YY/custom_distribution.expect__@0.16.1-0.17.0_L6_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(maxcount, 6)'], gt_only=[] |
| 70 | `sklearn/ensemble.GradientBoostingRegressor@0.23.2-0.24.0/ensemble.GradientBoostingRegressor#1YY/GradientBoostingRegressor__@0.23.2-0.24.0_L6_tempLst1.json` | mismatch | item 0 field (ccp_alpha, 23) mismatch: pred={'posChange': 22}, gt={} |
| 71 | `sklearn/linear_model.LinearRegression@1.1.3-1.2.0/linear_model.LinearRegression#1YY/LinearRegression__@1.1.3-1.2.0_L5_tempLst1.json` | mismatch | item 0 field (copy_X, 3) mismatch: pred={'posChange': 2}, gt={} |
| 72 | `sklearn/linear_model.lasso_path@0.15.2-0.16.0/linear_model.lasso_path#1YY/lasso_path_X__y_@0.15.2-0.16.0_L5_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(positive, 11)', '(return_n_iter, 10)'], gt_only=[] |
| 73 | `sklearn/sklearn.feature_selection.RFECV@0.17.1-0.18/sklearn.feature_selection.RFECV#1YY/RFECV_estimator_@0.17.1-0.18_L6_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(n_jobs, 5)'], gt_only=[] |
| 74 | `sympy/sympy.itermonomials@1.2-1.3/sympy.itermonomials#1NY/itermonomials__x__y___2_@1.2-1.3_L3_tempLst1.json` | mismatch | item 0 field (degree, 1) mismatch: pred={'delete': 1, 'replace': 'max_degree'}, gt={'rename': 'max_degree'} |
| 75 | `tensorflow/tf.contrib.data.make_csv_dataset@1.10.1-1.11.0/tf.contrib.data.make_csv_dataset#1NN/tf.contrib.data.make_csv_dataset__._dev.csv___1__None__None__None__None_______True______True__None__True__10000__None__1__1__2__False__1_@1.10.1-1.11.0_L2_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(compression_type, 18)'], gt_only=[] |
| 76 | `tensorflow/tf.contrib.data.make_csv_dataset@1.8.0-1.9.0/tf.contrib.data.make_csv_dataset#1NN/tf.contrib.data.make_csv_dataset__._dev.csv___1__None__None__None_______True______True__None__None__True__1__None__1__1__2__False__tf.float32__1_@1.8.0-1.9.0_L2_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(select_columns, 5)'], gt_only=[] |
| 77 | `torch/torch.btrifact@1.0.1-1.1.0/torch.btrifact#1YY/torch.btrifact_A_@1.0.1-1.1.0_L3_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(out, 2)'], gt_only=[] |
| 78 | `tornado/tornado.autoreload.start@4.5.3-5.0/tornado.autoreload.start#1YY/tornado.autoreload.start__@4.5.3-5.0_L3_tempLst1.json` | mismatch | item 0 field (io_loop, 0) mismatch: pred={'delete': 1, 'replace': 'check_time'}, gt={'delete': 1} |
| 79 | `tornado/tornado.httpclient.AsyncHTTPClient.fetch@5.1.1-6.0/tornado.httpclient.AsyncHTTPClient.fetch#1YY/http_client.fetch__http___example.com__@5.1.1-6.0_L6_tempLst1.json` | mismatch | item 0 field (callback, 1) mismatch: pred={'delete': 1, 'replace': 'raise_error'}, gt={'delete': 1} |
| 80 | `tornado/tornado.iostream.BaseIOStream.read_bytes@5.1.1-6.0/tornado.iostream.BaseIOStream.read_bytes#1YY/stream.read_bytes_10_@5.1.1-6.0_L11_tempLst1.json` | mismatch | item 0 field (num_bytes, 0) mismatch: pred={'typeChange': 'int'}, gt={} |
| 81 | `tornado/tornado.tcpserver.TCPServer@4.5.3-5.0/tornado.tcpserver.TCPServer#1YY/tornado.tcpserver.TCPServer__@4.5.3-5.0_L3_tempLst1.json` | mismatch | item 0 field (io_loop, 0) mismatch: pred={'delete': 1, 'replace': 'ssl_options'}, gt={'delete': 1} |
| 82 | `transformers/transformers.modeling_albert.AlbertForPreTraining.forward@2.11.0-3.0.0/transformers.modeling_albert.AlbertForPreTraining.forward#1YY/model.forward_input_ids_@2.11.0-3.0.0_L11_tempLst1.json` | mismatch | item 0 field (output_attentions, 8) mismatch: pred={'addPos': 'output_attentions'}, gt={'addPos': 'output_attentions=None'} |

## 语义不相关

| 指标 | 数值 |
| --- | ---: |
| 样例数 | 113 |
| 正确 | 11 |
| 错误 | 102 |
| 正确率 | 9.73% |

### 错误样例

| 序号 | 样例路径 | 错误类型 | 差异说明 |
| --- | --- | --- | --- |
| 1 | `click/click.Command@7.0-7.1/click.Command#1YY/click.Command__my_command__@7.0-7.1_L2_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(no_args_is_help, 9)'], gt_only=[] |
| 2 | `dask/dask.dataframe.core.drop@2.2.0-2.3.0/dask.dataframe.core.drop#1YY/ddf.drop__B___1_@2.2.0-2.3.0_L5_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(columns, 2)'], gt_only=[] |
| 3 | `dask/dask.dataframe.drop_duplicates@2.4.0-2.5.0/dask.dataframe.drop_duplicates#1YY/ddf.drop_duplicates__@2.4.0-2.5.0_L5_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(subset, 0)'], gt_only=[] |
| 4 | `dask/dask.dataframe.repartition@1.2.2-2.0.0/dask.dataframe.repartition#1YY/ddf.repartition_None__10_@1.2.2-2.0.0_L5_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(partition_size, 2)'], gt_only=[] |
| 5 | `dask/dask.dataframe.utils.assert_eq@2022.5.2-2022.6.0/dask.dataframe.utils.assert_eq#1YY/assert_eq_ddf_result__pdf_result_@2022.5.2-2022.6.0_L8_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(sort_results, 6)'], gt_only=[] |
| 6 | `django/models.Index@1.11.29-2.0/models.Index#1NN/models.Index___question_text____pub_date___@1.11.29-2.0_L2_tempLst1.json` | mismatch | item 0 field (db_tablespace, 3) mismatch: pred={'addKey': 'db_tablespace'}, gt={'addKey': 'db_tablespace=None'} |
| 7 | `flask/from_file@2.2.5-2.3.0/from_file#1YY/app.config.from_file__._test.json___json.load_@2.2.5-2.3.0_L4_tempLst1.json` | mismatch | item 0 field (filename, 0) mismatch: pred={'typeChange': "'str'"}, gt={} |
| 8 | `gensim/gensim.models.base_any2vec.BaseWordEmbeddingsModel@3.4.0-3.5.0/gensim.models.base_any2vec.BaseWordEmbeddingsModel#1YY/BaseWordEmbeddingsModel__@3.4.0-3.5.0_L2_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(ns_exponent, 13)'], gt_only=[] |
| 9 | `gensim/gensim.models.coherencemodel.CoherenceModel@0.13.1-0.13.2/gensim.models.coherencemodel.CoherenceModel#1NN/CoherenceModel_lda_model__documents_@0.13.1-0.13.2_L8_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(topics, 1)'], gt_only=[] |
| 10 | `gensim/gensim.models.doc2vec.Doc2Vec@3.5.0-3.6.0/gensim.models.doc2vec.Doc2Vec#1YY/Doc2Vec__@3.5.0-3.6.0_L3_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(corpus_file, 1)'], gt_only=[] |
| 11 | `gensim/gensim.models.ldamodel.LdaModel.diff@2.3.0-3.0.0/gensim.models.ldamodel.LdaModel.diff#1YY/lda1.diff_lda2_@2.3.0-3.0.0_L9_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(diagonal, 4)'], gt_only=[] |
| 12 | `gensim/gensim.models.word2vec.Word2Vec.intersect_word2vec_format@0.13.1-0.13.2/gensim.models.word2vec.Word2Vec.intersect_word2vec_format#1YY/model.intersect_word2vec_format_fname_@0.13.1-0.13.2_L7_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(lockf, 1)'], gt_only=[] |
| 13 | `gensim/gensim.models.word2vec.Word2Vec.train@1.0.1-2.0.0/gensim.models.word2vec.Word2Vec.train#1NN/model.train_sentences_@1.0.1-2.0.0_L5_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(end_alpha, 5)', '(epochs, 3)', '(start_alpha, 4)'], gt_only=[] |
| 14 | `keras/Conv2DTranspose@2.2.2-2.2.3/Conv2DTranspose#1YY/Conv2DTranspose_64___3__3__@2.2.2-2.2.3_L4_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(dilation_rate, 6)'], gt_only=[] |
| 15 | `keras/DepthwiseConv2D@2.2.4-2.2.5/DepthwiseConv2D#1YY/DepthwiseConv2D__3__3__@2.2.4-2.2.5_L4_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(dilation_rate, 5)'], gt_only=[] |
| 16 | `keras/keras.preprocessing.image.ImageDataGenerator@2.1.4-2.1.5/keras.preprocessing.image.ImageDataGenerator#1YY/ImageDataGenerator__@2.1.4-2.1.5_L2_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(brightness_range, 9)'], gt_only=[] |
| 17 | `matplotlib/matplotlib.axes.Axes.imshow@3.4.3-3.5.0/matplotlib.axes.Axes.imshow#1YY/plt.imshow_X_@3.4.3-3.5.0_L4_tempLst1.json` | mismatch | item 0 field (interpolation_stage, 11) mismatch: pred={'addKey': 'interpolation_stage'}, gt={'addKey': 'interpolation_stage=None'} |
| 18 | `matplotlib/matplotlib.gridspec.GridSpec@2.1.2-2.2.0/matplotlib.gridspec.GridSpec#1YY/gridspec.GridSpec_2__2_@2.1.2-2.2.0_L3_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(figure, 2)'], gt_only=[] |
| 19 | `networkx/betweenness_centrality@1.5-1.6/betweenness_centrality#1YY/nx.betweenness_centrality_G_@1.5-1.6_L4_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(k, 1)'], gt_only=[] |
| 20 | `networkx/networkx.linalg.graphmatrix.adjacency_matrix@2.5.1-2.6/networkx.linalg.graphmatrix.adjacency_matrix#1YY/nx.adjacency_matrix_G_@2.5.1-2.6_L4_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(dtype, 2)'], gt_only=[] |
| 21 | `numpy/numpy.ma.argsort@1.12.1-1.13.0/numpy.ma.argsort#1YY/np.ma.argsort_data_@1.12.1-1.13.0_L5_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(endwith, 4)'], gt_only=[] |
| 22 | `numpy/numpy.percentile@1.21.6-1.22.0/numpy.percentile#1YY/np.percentile_a___25__50__75__@1.21.6-1.22.0_L3_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(interpolation, 8)'], gt_only=[] |
| 23 | `numpy/numpy.quantile@1.21.6-1.22.0/numpy.quantile#1YY/np.quantile_a__q_@1.21.6-1.22.0_L9_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(interpolation, 8)'], gt_only=[] |
| 24 | `pandas/DataFrame.ewm@1.3.5-1.4.0/DataFrame.ewm#1YY/df.ewm_0.5_@1.3.5-1.4.0_L4_tempLst1.json` | mismatch | item 0 field (times, 8) mismatch: pred={'typeChange': "'str\|np.ndarray\|DataFrame\|Series\|None'"}, gt={'typeChange': 'str\|np.ndarray\|DataFrame\|Series\|None'} |
| 25 | `pandas/DataFrame.reset_index@1.4.4-1.5.0/DataFrame.reset_index#1YY/df.reset_index__@1.4.4-1.5.0_L4_tempLst1.json` | mismatch | item 0 field (level, 0) mismatch: pred={'typeChange': "'IndexLabel'"}, gt={'typeChange': 'IndexLabel'} |
| 26 | `pandas/DataFrame.rolling@1.4.4-1.5.0/DataFrame.rolling#1YY/df.rolling_2_@1.4.4-1.5.0_L4_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(step, 7)'], gt_only=[] |
| 27 | `pandas/DataFrame.to_stata@1.3.5-1.4.0/DataFrame.to_stata#1YY/df.to_stata__animals.dta__@1.3.5-1.4.0_L3_tempLst1.json` | mismatch | item 0 field (path, 0) mismatch: pred={'typeChange': "'FilePath\|WriteBuffer[bytes]'"}, gt={'typeChange': 'FilePath\|WriteBuffer[bytes]'} |
| 28 | `pandas/Series.ewm@1.3.5-1.4.0/Series.ewm#1YY/df.ewm_0.5_@1.3.5-1.4.0_L4_tempLst1.json` | mismatch | item 0 field (times, 8) mismatch: pred={'typeChange': "'str\|np.ndarray\|DataFrame\|Series\|None'"}, gt={'typeChange': 'str\|np.ndarray\|DataFrame\|Series\|None'} |
| 29 | `pandas/Series.rolling@1.4.4-1.5.0/Series.rolling#1YY/df.rolling_2_@1.4.4-1.5.0_L4_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(step, 7)'], gt_only=[] |
| 30 | `pandas/Styler.background_gradient@1.2.5-1.3.0/Styler.background_gradient#1YY/df.style.background_gradient__@1.2.5-1.3.0_L13_tempLst1.json` | mismatch | item 0 field (axis, 3) mismatch: pred={'typeChange': "'Axis\|None'"}, gt={'typeChange': 'Axis\|None'} |
| 31 | `pandas/Styler.format@1.2.5-1.3.0/Styler.format#1YY/df.style.format____.2____@1.2.5-1.3.0_L4_tempLst1.json` | mismatch | item 0 field (decimal, 4) mismatch: pred={'addPos': 'decimal'}, gt={'addPos': "decimal='.'"} |
| 32 | `pandas/melt@1.0.5-1.1.0/melt#1YY/pd.melt_df_@1.0.5-1.1.0_L3_tempLst1.json` | mismatch | item 0 field (frame, 0) mismatch: pred={'typeChange': "'DataFrame'"}, gt={'typeChange': 'DataFrame'} |
| 33 | `pandas/read_csv@1.2.5-1.3.0/read_csv#1YY/pd.read_csv__._dev.csv__@1.2.5-1.3.0_L2_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(encoding_errors, 42)', '(on_bad_lines, 46)'], gt_only=[] |
| 34 | `pandas/testing.assert_frame_equal@1.0.5-1.1.0/testing.assert_frame_equal#1YY/assert_frame_equal_df1__df1_@1.0.5-1.1.0_L5_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(check_freq, 13)'], gt_only=[] |
| 35 | `pandas/testing.assert_series_equal@1.0.5-1.1.0/testing.assert_series_equal#1YY/assert_series_equal_df1__df1_@1.0.5-1.1.0_L5_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(check_freq, 11)'], gt_only=[] |
| 36 | `pandas/testing.assert_series_equal@1.1.5-1.2.0/testing.assert_series_equal#1YY/tm.assert_series_equal_a__b_@1.1.5-1.2.0_L5_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(check_flags, 12)'], gt_only=[] |
| 37 | `plotly/plotly.express.area@4.2.1-4.3.0/plotly.express.area#1YY/px.area__@4.2.1-4.3.0_L3_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(facet_col_wrap, 11)'], gt_only=[] |
| 38 | `plotly/plotly.express.bar@4.14.3-5.0.0/plotly.express.bar#1YY/px.bar__@4.14.3-5.0.0_L3_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(pattern_shape, 4)', '(pattern_shape_map, 27)', '(pattern_shape_sequence, 26)'], gt_only=[] |
| 39 | `plotly/plotly.express.bar@4.2.1-4.3.0/plotly.express.bar#1YY/px.bar__@4.2.1-4.3.0_L3_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(facet_col_wrap, 6)'], gt_only=[] |
| 40 | `plotly/plotly.express.bar@5.4.0-5.5.0/plotly.express.bar#1YY/px.bar__@5.4.0-5.5.0_L3_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(text_auto, 37)'], gt_only=[] |
| 41 | `plotly/plotly.express.bar_polar@4.14.3-5.0.0/plotly.express.bar_polar#1YY/px.bar_polar__@4.14.3-5.0.0_L3_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(pattern_shape, 4)', '(pattern_shape_map, 17)', '(pattern_shape_sequence, 16)'], gt_only=[] |
| 42 | `plotly/plotly.express.bar_polar@4.3.0-4.4.0/plotly.express.bar_polar#1YY/px.bar_polar__@4.3.0-4.4.0_L3_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(range_theta, 18)'], gt_only=[] |
| 43 | `plotly/plotly.express.box@4.2.1-4.3.0/plotly.express.box#1YY/px.box__@4.2.1-4.3.0_L3_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(facet_col_wrap, 6)'], gt_only=[] |
| 44 | `plotly/plotly.express.density_contour@4.2.1-4.3.0/plotly.express.density_contour#1YY/px.density_contour__@4.2.1-4.3.0_L3_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(facet_col_wrap, 7)'], gt_only=[] |
| 45 | `plotly/plotly.express.density_contour@5.1.0-5.2.1/plotly.express.density_contour#1YY/px.density_contour__@5.1.0-5.2.1_L3_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(trendline_options, 22)', '(trendline_scope, 24)'], gt_only=[] |
| 46 | `plotly/plotly.express.density_heatmap@4.2.1-4.3.0/plotly.express.density_heatmap#1YY/px.density_heatmap__@4.2.1-4.3.0_L3_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(facet_col_wrap, 6)'], gt_only=[] |
| 47 | `plotly/plotly.express.density_heatmap@5.4.0-5.5.0/plotly.express.density_heatmap#1YY/px.density_heatmap__@5.4.0-5.5.0_L3_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(text_auto, 30)'], gt_only=[] |
| 48 | `plotly/plotly.express.histogram@4.14.3-5.0.0/plotly.express.histogram#1YY/px.histogram__@4.14.3-5.0.0_L3_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(pattern_shape, 4)', '(pattern_shape_map, 19)', '(pattern_shape_sequence, 18)'], gt_only=[] |
| 49 | `plotly/plotly.express.histogram@4.2.1-4.3.0/plotly.express.histogram#1YY/px.histogram__@4.2.1-4.3.0_L3_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(facet_col_wrap, 6)'], gt_only=[] |
| 50 | `plotly/plotly.express.histogram@5.4.0-5.5.0/plotly.express.histogram#1YY/px.histogram__@5.4.0-5.5.0_L3_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(text_auto, 33)'], gt_only=[] |
| 51 | `plotly/plotly.express.imshow@4.13.0-4.14.0/plotly.express.imshow#1YY/px.imshow_img_rgb_@4.13.0-4.14.0_L4_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(animation_frame, 7)', '(facet_col, 8)', '(facet_col_spacing, 10)'], gt_only=[] |
| 52 | `plotly/plotly.express.line@4.2.1-4.3.0/plotly.express.line#1YY/px.line__@4.2.1-4.3.0_L3_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(facet_col_wrap, 12)'], gt_only=[] |
| 53 | `plotly/plotly.express.line@5.1.0-5.2.1/plotly.express.line#1YY/px.line__@5.1.0-5.2.1_L3_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(markers, 31)', '(symbol, 6)', '(symbol_map, 30)'], gt_only=[] |
| 54 | `plotly/plotly.express.line_3d@5.1.0-5.2.1/plotly.express.line_3d#1YY/px.line_3d__@5.1.0-5.2.1_L3_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(markers, 28)', '(symbol, 8)', '(symbol_map, 27)'], gt_only=[] |
| 55 | `plotly/plotly.express.line_geo@5.1.0-5.2.1/plotly.express.line_geo#1YY/px.line_geo__@5.1.0-5.2.1_L3_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(markers, 30)', '(symbol, 19)', '(symbol_map, 29)'], gt_only=[] |
| 56 | `plotly/plotly.express.line_mapbox@4.3.0-4.4.0/plotly.express.line_mapbox#1YY/px.line_mapbox_us_cities___lat____lon__@4.3.0-4.4.0_L5_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(center, 16)', '(mapbox_style, 17)'], gt_only=[] |
| 57 | `plotly/plotly.express.line_polar@4.3.0-4.4.0/plotly.express.line_polar#1YY/px.line_polar__@4.3.0-4.4.0_L3_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(range_theta, 24)'], gt_only=[] |
| 58 | `plotly/plotly.express.line_polar@5.1.0-5.2.1/plotly.express.line_polar#1YY/px.line_polar__@5.1.0-5.2.1_L3_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(markers, 21)', '(symbol, 10)', '(symbol_map, 20)'], gt_only=[] |
| 59 | `plotly/plotly.express.line_ternary@5.1.0-5.2.1/plotly.express.line_ternary#1YY/px.line_ternary__@5.1.0-5.2.1_L3_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(markers, 22)', '(symbol, 7)', '(symbol_map, 21)'], gt_only=[] |
| 60 | `plotly/plotly.express.scatter@4.2.1-4.3.0/plotly.express.scatter#1YY/px.scatter__@4.2.1-4.3.0_L3_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(facet_col_wrap, 12)'], gt_only=[] |
| 61 | `plotly/plotly.express.scatter@5.1.0-5.2.1/plotly.express.scatter#1YY/px.scatter__@5.1.0-5.2.1_L3_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(trendline_options, 36)', '(trendline_scope, 38)'], gt_only=[] |
| 62 | `plotly/plotly.express.scatter_mapbox@4.3.0-4.4.0/plotly.express.scatter_mapbox#1YY/px.scatter_mapbox_df___centroid_lat____centroid_lon__@4.3.0-4.4.0_L3_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(center, 21)', '(mapbox_style, 22)'], gt_only=[] |
| 63 | `plotly/plotly.express.scatter_polar@4.3.0-4.4.0/plotly.express.scatter_polar#1YY/px.scatter_polar__@4.3.0-4.4.0_L3_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(range_theta, 26)'], gt_only=[] |
| 64 | `plotly/plotly.express.strip@4.2.1-4.3.0/plotly.express.strip#1YY/px.strip__@4.2.1-4.3.0_L3_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(facet_col_wrap, 6)'], gt_only=[] |
| 65 | `plotly/plotly.express.sunburst@4.4.1-4.5.0/plotly.express.sunburst#1YY/px.sunburst__@4.4.1-4.5.0_L3_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(path, 4)'], gt_only=[] |
| 66 | `plotly/plotly.express.treemap@4.4.1-4.5.0/plotly.express.treemap#1YY/px.treemap__@4.4.1-4.5.0_L3_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(path, 5)'], gt_only=[] |
| 67 | `plotly/plotly.express.violin@4.2.1-4.3.0/plotly.express.violin#1YY/px.violin__@4.2.1-4.3.0_L3_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(facet_col_wrap, 6)'], gt_only=[] |
| 68 | `plotly/plotly.figure_factory.create_violin@2.0.8-2.0.9/plotly.figure_factory.create_violin#1YY/create_violin_data_list_@2.0.8-2.0.9_L5_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(sort, 7)'], gt_only=[] |
| 69 | `plotly/plotly.tools.FigureFactory.create_distplot@1.10.0-1.11.0/plotly.tools.FigureFactory.create_distplot#1YY/FF.create_distplot_hist_data__group_labels_@1.10.0-1.11.0_L9_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(histnorm, 6)'], gt_only=[] |
| 70 | `polars/polars.repeat@0.17.14-0.17.15/polars.repeat#1YY/pl.repeat__z___3_@0.17.14-0.17.15_L2_tempLst1.json` | mismatch | item 0 field (eager, 3) mismatch: pred={'posChange': 4}, gt={} |
| 71 | `rich/Columns@1.3.0-1.3.1/Columns#1YY/Columns_renderables_@1.3.0-1.3.1_L3_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(width, 2)'], gt_only=[] |
| 72 | `rich/Panel@2.3.1-3.0.0/Panel#1YY/Panel_None_@2.3.1-3.0.0_L2_tempLst1.json` | mismatch | item 0 field (box, 1) mismatch: pred={'typeChange': 'rich.box.Box'}, gt={} |
| 73 | `rich/Panel@3.1.0-3.2.0/Panel#1YY/Panel_renderable_@3.1.0-3.2.0_L6_tempLst1.json` | mismatch | item 0 field (padding, 7) mismatch: pred={'posChange': 8}, gt={} |
| 74 | `rich/install@12.5.1-12.6.0/install#1YY/pretty.install__@12.5.1-12.6.0_L2_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(max_depth, 6)'], gt_only=[] |
| 75 | `rich/rich.syntax.Syntax.from_path@11.0.0-11.1.0/rich.syntax.Syntax.from_path#1YY/Syntax.from_path__._example.py__@11.0.0-11.1.0_L2_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(lexer, 2)'], gt_only=[] |
| 76 | `scipy/scipy.stats.qmc.LatinHypercube@1.9.3-1.10.0/scipy.stats.qmc.LatinHypercube#1YY/qmc.LatinHypercube_d_@1.9.3-1.10.0_L7_tempLst1.json` | mismatch | item 0 field (optimization, 4) mismatch: pred={'typeChange': "Optional[Literal[('random-cd','lloyd')]]", 'posChange': 5}, gt={'typeChange': '"Optional[Literal[(\'random-cd\',\'lloyd\')]]"'} |
| 77 | `scipy/scipy.stats.ttest_ind@1.6.3-1.7.0/scipy.stats.ttest_ind#1YY/stats.ttest_ind_a__b_@1.6.3-1.7.0_L4_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(permutations, 5)'], gt_only=[] |
| 78 | `sklearn/calibration.CalibratedClassifierCV@1.1.3-1.2.0/calibration.CalibratedClassifierCV#1YY/CalibratedClassifierCV__@1.1.3-1.2.0_L6_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(estimator, 0)'], gt_only=[] |
| 79 | `sklearn/cluster.SpectralBiclustering@0.22.2-0.23.0/cluster.SpectralBiclustering#1YY/SpectralBiclustering_2_@0.22.2-0.23.0_L4_tempLst1.json` | mismatch | item 0 field (init, 7) mismatch: pred={'posChange': 8, 'pos2key': 'init'}, gt={'pos2key': 'init'} |
| 80 | `sklearn/cluster.SpectralCoclustering@0.22.2-0.23.0/cluster.SpectralCoclustering#1YY/SpectralCoclustering__@0.22.2-0.23.0_L4_tempLst1.json` | mismatch | item 0 field (init, 4) mismatch: pred={'posChange': 5, 'pos2key': 'init'}, gt={'pos2key': 'init'} |
| 81 | `sklearn/datasets.make_blobs@0.22.2-0.23.0/datasets.make_blobs#1YY/make_blobs__@0.22.2-0.23.0_L2_tempLst1.json` | mismatch | item 0 field (center_box, 4) mismatch: pred={'posChange': 5, 'pos2key': 'center_box'}, gt={'pos2key': 'center_box'} |
| 82 | `sklearn/ensemble.AdaBoostClassifier@1.1.3-1.2.0/ensemble.AdaBoostClassifier#1YY/AdaBoostClassifier__@1.1.3-1.2.0_L4_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(estimator, 0)'], gt_only=[] |
| 83 | `sklearn/ensemble.AdaBoostRegressor@1.1.3-1.2.0/ensemble.AdaBoostRegressor#1YY/AdaBoostRegressor__@1.1.3-1.2.0_L4_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(estimator, 0)'], gt_only=[] |
| 84 | `sklearn/ensemble.BaggingClassifier@1.1.3-1.2.0/ensemble.BaggingClassifier#1YY/BaggingClassifier__@1.1.3-1.2.0_L5_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(estimator, 0)'], gt_only=[] |
| 85 | `sklearn/ensemble.BaggingRegressor@1.1.3-1.2.0/ensemble.BaggingRegressor#1YY/BaggingRegressor__@1.1.3-1.2.0_L5_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(base_estimator, 12)', '(estimator, 0)'], gt_only=[] |
| 86 | `sklearn/ensemble.HistGradientBoostingRegressor@0.22.2-0.23.0/ensemble.HistGradientBoostingRegressor#1YY/HistGradientBoostingRegressor__@0.22.2-0.23.0_L5_tempLst1.json` | mismatch | item 0 field (early_stopping, 11) mismatch: pred={'addKey': 'early_stopping'}, gt={'addKey': "early_stopping='auto'"} |
| 87 | `sklearn/linear_model.Lars@0.22.2-0.23.0/linear_model.Lars#1YY/linear_model.Lars__@0.22.2-0.23.0_L2_tempLst1.json` | mismatch | item 0 field (jitter, 9) mismatch: pred={'addKey': 'jitter'}, gt={'addKey': 'jitter=None'} |
| 88 | `sklearn/linear_model.LassoLars@0.22.2-0.23.0/linear_model.LassoLars#1YY/linear_model.LassoLars__@0.22.2-0.23.0_L2_tempLst1.json` | mismatch | item 0 field (copy_X, 7) mismatch: pred={'posChange': 8, 'pos2key': 'copy_X'}, gt={'pos2key': 'copy_X'} |
| 89 | `sklearn/linear_model.RANSACRegressor@0.17.1-0.18/linear_model.RANSACRegressor#1YY/RANSACRegressor__@0.17.1-0.18_L2_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(loss, 10)'], gt_only=[] |
| 90 | `sklearn/linear_model.RANSACRegressor@1.0.2-1.1.0/linear_model.RANSACRegressor#1YY/RANSACRegressor__@1.0.2-1.1.0_L5_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(base_estimator, 13)', '(estimator, 0)'], gt_only=[] |
| 91 | `sklearn/sklearn.cluster.SpectralClustering@0.21.3-0.22/sklearn.cluster.SpectralClustering#1YY/SpectralClustering_5_@0.21.3-0.22_L4_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(n_components, 2)'], gt_only=[] |
| 92 | `sklearn/sklearn.discriminant_analysis.QuadraticDiscriminantAnalysis@0.18.1-0.19.0/sklearn.discriminant_analysis.QuadraticDiscriminantAnalysis#1YY/QuadraticDiscriminantAnalysis__@0.18.1-0.19.0_L5_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(store_covariances, 4)'], gt_only=[] |
| 93 | `sklearn/sklearn.linear_model.BayesianRidge@0.21.3-0.22/sklearn.linear_model.BayesianRidge#1YY/linear_model.BayesianRidge__@0.21.3-0.22_L2_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(alpha_init, 6)', '(lambda_init, 7)'], gt_only=[] |
| 94 | `sklearn/sklearn.linear_model.PassiveAggressiveClassifier@0.18.1-0.19.0/sklearn.linear_model.PassiveAggressiveClassifier#1YY/PassiveAggressiveClassifier__@0.18.1-0.19.0_L2_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(n_iter, 12)', '(tol, 3)'], gt_only=[] |
| 95 | `sklearn/sklearn.svm.NuSVC@0.21.3-0.22/sklearn.svm.NuSVC#1YY/NuSVC__@0.21.3-0.22_L5_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(break_ties, 13)'], gt_only=[] |
| 96 | `sklearn/sklearn.svm.SVC@0.21.3-0.22/sklearn.svm.SVC#1YY/SVC__@0.21.3-0.22_L5_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(break_ties, 13)'], gt_only=[] |
| 97 | `sympy/sympy.physics.mechanics.PinJoint@1.11.1-1.12/sympy.physics.mechanics.PinJoint#1YY/PinJoint__PC___parent__child_@1.11.1-1.12_L4_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(child_joint_pos, 13)', '(parent_joint_pos, 12)'], gt_only=[] |
| 98 | `sympy/sympy.physics.mechanics.PrismaticJoint@1.11.1-1.12/sympy.physics.mechanics.PrismaticJoint#1YY/PrismaticJoint__PC___parent__child_@1.11.1-1.12_L4_tempLst1.json` | mismatch | item 0 field (child_joint_pos, 6) mismatch: pred={'rename': 'child_point', 'posChange': 13}, gt={'posChange': 13, 'replace': 'child_point=None'} |
| 99 | `tensorflow/tf.data.Dataset.random@2.11.1-2.12.0/tf.data.Dataset.random#1YY/tf.data.Dataset.random__@2.11.1-2.12.0_L2_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(rerandomize_each_iteration, 1)'], gt_only=[] |
| 100 | `tensorflow/tf.keras.losses.SparseCategoricalCrossentropy@2.9.3-2.10.0/tf.keras.losses.SparseCategoricalCrossentropy#1YY/tf.keras.losses.SparseCategoricalCrossentropy__@2.9.3-2.10.0_L2_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(ignore_class, 1)'], gt_only=[] |
| 101 | `tensorflow/tf.string_split@1.13.2-1.14.0/tf.string_split#1YY/tf.string_split_string_tensor_@1.13.2-1.14.0_L4_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(sep, 1)'], gt_only=[] |
| 102 | `tornado/tornado.httpclient.HTTPRequest@3.0.2-3.1/tornado.httpclient.HTTPRequest#1YY/tornado.httpclient.HTTPRequest__http___httpbin.org_get__@3.0.2-3.1_L2_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(auth_mode, 6)'], gt_only=[] |
