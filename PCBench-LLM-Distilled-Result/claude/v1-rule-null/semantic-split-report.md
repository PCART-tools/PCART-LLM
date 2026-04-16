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
| 语义相关 | 171 | 102 | 69 | 59.65% |
| 语义不相关 | 113 | 33 | 80 | 29.20% |
| 合并后 | 284 | 135 | 149 | 47.54% |

## 语义相关

| 指标 | 数值 |
| --- | ---: |
| 样例数 | 171 |
| 正确 | 102 |
| 错误 | 69 |
| 正确率 | 59.65% |

### 错误样例

| 序号 | 样例路径 | 错误类型 | 差异说明 |
| --- | --- | --- | --- |
| 1 | `dask/dask.dataframe.read_parquet@2022.4.1-2022.4.2/dask.dataframe.read_parquet#1YY/dd.read_parquet__._example.parquet__@2022.4.1-2022.4.2_L2_tempLst1.json` | mismatch | item 0 field (gather_statistics, 7) mismatch: pred={'replace': 'calculate_divisions=None'}, gt={'rename': 'calculate_divisions'} |
| 2 | `fastapi/fastapi.encoders.jsonable_encoder@0.60.2-0.61.0/fastapi.encoders.jsonable_encoder#1YY/jsonable_encoder_item_@0.60.2-0.61.0_L14_tempLst1.json` | mismatch | item 0 field (skip_defaults, 4) mismatch: pred={'delete': 1, 'replace': 'exclude_unset=False'}, gt={'delete': 1} |
| 3 | `gensim/gensim.models.doc2vec.Doc2Vec.similarity_unseen_docs@4.0.1-4.1.0/gensim.models.doc2vec.Doc2Vec.similarity_unseen_docs#1YY/model.similarity_unseen_docs_doc_words1__doc_words2_@4.0.1-4.1.0_L7_tempLst1.json` | mismatch | item 0 field (steps, 4) mismatch: pred={'replace': 'epochs=None'}, gt={'rename': 'epochs'} |
| 4 | `gensim/gensim.models.fasttext.FastText@3.8.3-4.0.0/gensim.models.fasttext.FastText#1YY/FastText__@3.8.3-4.0.0_L2_tempLst1.json` | mismatch | item 0 field (iter, 18) mismatch: pred={'rename': 'epochs', 'replace': 'epochs=5'}, gt={'rename': 'epochs'} |
| 5 | `gensim/gensim.models.word2vec.Word2Vec.load_word2vec_format@0.12.3-0.12.4/gensim.models.word2vec.Word2Vec.load_word2vec_format#1YY/Word2Vec.load_word2vec_format_fname_@0.12.3-0.12.4_L3_tempLst1.json` | mismatch | item 0 field (norm_only, 3) mismatch: pred={'delete': 1, 'replace': 'encoding=utf8'}, gt={'delete': 1} |
| 6 | `httpx/URL@0.13.3-0.14.0/URL#1YY/httpx.URL_url_str_@0.13.3-0.14.0_L4_tempLst1.json` | mismatch | item 0 field (allow_relative, 1) mismatch: pred={'delete': 1, 'replace': 'params'}, gt={'delete': 1} |
| 7 | `jax/jax.experimental.jax2tf.convert@0.4.12-0.4.13/jax.experimental.jax2tf.convert#1YY/jax2tf.convert_sum_of_squares_@0.4.12-0.4.13_L7_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=[], gt_only=['(native_serialization_disabled_checks, 7)'] |
| 8 | `matplotlib/matplotlib.patheffects.SimplePatchShadow@1.4.3-1.5.0/matplotlib.patheffects.SimplePatchShadow#1YY/pe.SimplePatchShadow__@1.4.3-1.5.0_L5_tempLst1.json` | mismatch | item 0 field (patch_alpha, 3) mismatch: pred={'delete': 1, 'replace': 'rho=0.3'}, gt={'delete': 1} |
| 9 | `networkx/average_clustering@1.5-1.6/average_clustering#1YY/nx.average_clustering_G_@1.5-1.6_L4_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(nodes, 1)'], gt_only=[] |
| 10 | `networkx/average_neighbor_degree@1.5-1.6/average_neighbor_degree#1YY/nx.average_neighbor_degree_G_@1.5-1.6_L4_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(source, 1)'], gt_only=[] |
| 11 | `networkx/average_shortest_path_length@1.4-1.5/average_shortest_path_length#1YY/nx.average_shortest_path_length_G_@1.4-1.5_L4_tempLst1.json` | mismatch | item 0 field (weighted, 1) mismatch: pred={'replace': 'weight=None'}, gt={'rename': 'weight'} |
| 12 | `networkx/betweenness_centrality_source@1.4-1.5/betweenness_centrality_source#1YY/nx.betweenness_centrality_source_G_@1.4-1.5_L4_tempLst1.json` | mismatch | item 0 field (weighted_edges, 2) mismatch: pred={'replace': 'weight=None'}, gt={'rename': 'weight'} |
| 13 | `networkx/closeness_vitality@1.4-1.5/closeness_vitality#1YY/nx.closeness_vitality_G_@1.4-1.5_L4_tempLst1.json` | mismatch | item 0 field (weighted_edges, 2) mismatch: pred={'replace': 'weight=None'}, gt={'rename': 'weight'} |
| 14 | `networkx/clustering@1.5-1.6/clustering#1YY/nx.clustering_G_@1.5-1.6_L4_tempLst1.json` | mismatch | item 0 field (weighted, 2) mismatch: pred={'replace': 'weight=None'}, gt={'delete': 1, 'replace': 'weight=None'} |
| 15 | `networkx/degree@1.5-1.6/degree#1YY/G.degree__@1.5-1.6_L4_tempLst1.json` | mismatch | item 0 field (weighted, 1) mismatch: pred={'replace': 'weight=None'}, gt={'delete': 1, 'replace': 'weight=None'} |
| 16 | `networkx/edge_betweenness_centrality_subset@1.4-1.5/edge_betweenness_centrality_subset#1YY/nx.edge_betweenness_centrality_subset_G__sources__targets_@1.4-1.5_L6_tempLst1.json` | mismatch | item 0 field (weighted_edges, 4) mismatch: pred={'replace': 'weight=None'}, gt={'rename': 'weight'} |
| 17 | `networkx/geographical_threshold_graph@2.0-2.1/geographical_threshold_graph#1YY/nx.geographical_threshold_graph_10__0.1_@2.0-2.1_L2_tempLst1.json` | mismatch | item 0 field (alpha, 2) mismatch: pred={'delete': 1, 'replace': 'p_dist=None'}, gt={'delete': 1} |
| 18 | `networkx/networkx.betweenness_centrality@1.4-1.5/networkx.betweenness_centrality#1YY/nx.betweenness_centrality_G_@1.4-1.5_L3_tempLst1.json` | mismatch | item 0 field (weighted_edges, 2) mismatch: pred={'replace': 'weight=None'}, gt={'rename': 'weight'} |
| 19 | `networkx/networkx.to_pandas_edgelist@2.8.8-3.0/networkx.to_pandas_edgelist#1YY/nx.to_pandas_edgelist_G_@2.8.8-3.0_L7_tempLst1.json` | mismatch | item 0 field (order, 5) mismatch: pred={'delete': 1, 'replace': 'edge_key=None'}, gt={'delete': 1} |
| 20 | `networkx/shortest_path@1.4-1.5/shortest_path#1YY/nx.shortest_path_G_@1.4-1.5_L4_tempLst1.json` | mismatch | item 0 field (weighted, 3) mismatch: pred={'replace': 'weight=None'}, gt={'rename': 'weight'} |
| 21 | `networkx/shortest_path_length@1.4-1.5/shortest_path_length#1YY/nx.shortest_path_length_G_@1.4-1.5_L4_tempLst1.json` | mismatch | item 0 field (weighted, 3) mismatch: pred={'replace': 'weight=None'}, gt={'rename': 'weight'} |
| 22 | `networkx/spectral_layout@1.5-1.6/spectral_layout#1YY/nx.spectral_layout_G_@1.5-1.6_L4_tempLst1.json` | mismatch | item 0 field (weighted, 2) mismatch: pred={'replace': "weight='weight'"}, gt={'delete': 1, 'replace': "weight='weight'"} |
| 23 | `numpy/numpy.fix@1.12.1-1.13.0/numpy.fix#1YY/np.fix_x_@1.12.1-1.13.0_L6_tempLst1.json` | mismatch | item 0 field (y, 1) mismatch: pred={'replace': 'out=None'}, gt={'rename': 'out'} |
| 24 | `numpy/numpy.genfromtxt@1.9.3-1.10.0/numpy.genfromtxt#1YY/np.genfromtxt_f_@1.9.3-1.10.0_L4_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(max_rows, 21)'], gt_only=[] |
| 25 | `numpy/numpy.histogram@1.23.5-1.24.0/numpy.histogram#1YY/np.histogram_a_@1.23.5-1.24.0_L8_tempLst1.json` | mismatch | item 0 field (normed, 3) mismatch: pred={'delete': 1, 'replace': 'density=None'}, gt={'delete': 1} |
| 26 | `numpy/numpy.histogramdd@1.23.5-1.24.0/numpy.histogramdd#1YY/np.histogramdd_sample_@1.23.5-1.24.0_L3_tempLst1.json` | mismatch | item 0 field (normed, 3) mismatch: pred={'delete': 1, 'replace': 'density=None'}, gt={'delete': 1} |
| 27 | `numpy/numpy.isneginf@1.12.1-1.13.0/numpy.isneginf#1YY/np.isneginf_x_@1.12.1-1.13.0_L6_tempLst1.json` | mismatch | item 0 field (y, 1) mismatch: pred={'replace': 'out=None'}, gt={'rename': 'out'} |
| 28 | `numpy/numpy.isposinf@1.12.1-1.13.0/numpy.isposinf#1YY/np.isposinf_x_@1.12.1-1.13.0_L6_tempLst1.json` | mismatch | item 0 field (y, 1) mismatch: pred={'replace': 'out=None'}, gt={'rename': 'out'} |
| 29 | `pandas/DataFrame.between_time@1.5.3-2.0.0/DataFrame.between_time#1YY/ts.between_time__0_15____0_45__@1.5.3-2.0.0_L4_tempLst1.json` | mismatch | item 0 field (axis, 5) mismatch: pred={'typeChange': "'Axis\|None'", 'posChange': 3}, gt={'posChange': 3} |
| 30 | `pandas/DataFrame.groupby@1.5.3-2.0.0/DataFrame.groupby#1YY/df.groupby___Animal___@1.5.3-2.0.0_L3_tempLst1.json` | mismatch | item 0 field (group_keys, 5) mismatch: pred={'typeChange': "'bool'"}, gt={'typeChange': 'bool'} |
| 31 | `pandas/DataFrame.set_axis@1.5.3-2.0.0/DataFrame.set_axis#1YY/df.set_axis___a____b____c___@1.5.3-2.0.0_L3_tempLst1.json` | mismatch | item 0 field (copy, 4) mismatch: pred={'typeChange': "'bool\|None'"}, gt={'typeChange': 'bool\|None'} |
| 32 | `pandas/DataFrame.take@1.5.3-2.0.0/DataFrame.take#1YY/df.take__0__3__@1.5.3-2.0.0_L4_tempLst1.json` | mismatch | item 0 field (axis, 1) mismatch: pred={'typeChange': "'Axis'"}, gt={} |
| 33 | `pandas/DataFrame.to_excel@1.5.3-2.0.0/DataFrame.to_excel#1YY/df1.to_excel__._output.xlsx__@1.5.3-2.0.0_L3_tempLst1.json` | mismatch | item 0 field (encoding, 12) mismatch: pred={'delete': 1, 'replace': "inf_rep='inf'"}, gt={'delete': 1} |
| 34 | `pandas/Series.groupby@1.5.3-2.0.0/Series.groupby#1YY/ser.groupby___a____b____a____b___@1.5.3-2.0.0_L3_tempLst1.json` | mismatch | item 0 field (group_keys, 5) mismatch: pred={'typeChange': "'bool'"}, gt={'typeChange': 'bool'} |
| 35 | `pandas/Series.set_axis@1.5.3-2.0.0/Series.set_axis#1YY/s.set_axis___a____b____c___@1.5.3-2.0.0_L3_tempLst1.json` | mismatch | item 0 field (copy, 4) mismatch: pred={'typeChange': "'bool\|None'"}, gt={'typeChange': 'bool\|None'} |
| 36 | `pandas/Timestamp.fromordinal@1.5.3-2.0.0/Timestamp.fromordinal#1YY/pd.Timestamp.fromordinal_737425_@1.5.3-2.0.0_L2_tempLst1.json` | mismatch | item 0 field (freq, 1) mismatch: pred={'delete': 1, 'replace': 'tz=None'}, gt={'delete': 1} |
| 37 | `pandas/Timestamp@1.5.3-2.0.0/Timestamp#1YY/pd.Timestamp__2017-01-01T12__@1.5.3-2.0.0_L2_tempLst1.json` | mismatch | item 0 field (freq, 1) mismatch: pred={'delete': 1, 'replace': 'year=None'}, gt={'delete': 1} |
| 38 | `pandas/bdate_range@1.5.3-2.0.0/bdate_range#1YY/pd.bdate_range__1_1_2018____1_08_2018__@1.5.3-2.0.0_L2_tempLst1.json` | mismatch | item 0 field (closed, 9) mismatch: pred={'delete': 1, 'replace': "inclusive='both'"}, gt={'delete': 1} |
| 39 | `pandas/date_range@1.5.3-2.0.0/date_range#1YY/pd.date_range__1_1_2018____1_08_2018__@1.5.3-2.0.0_L2_tempLst1.json` | mismatch | item 0 field (closed, 7) mismatch: pred={'delete': 1, 'replace': 'inclusive=both'}, gt={'delete': 1} |
| 40 | `pandas/pandas.DataFrame.resample@1.5.3-2.0.0/pandas.DataFrame.resample#1YY/DataFrame.resample__3T__@1.5.3-2.0.0_L4_tempLst1.json` | mismatch | item 0 field (base, 7) mismatch: pred={'delete': 1, 'replace': 'level=None'}, gt={'delete': 1} |
| 41 | `pandas/pandas.Series.resample@1.5.3-2.0.0/pandas.Series.resample#1YY/series.resample__3T__@1.5.3-2.0.0_L4_tempLst1.json` | mismatch | item 0 field (base, 7) mismatch: pred={'delete': 1, 'replace': 'level=None'}, gt={'delete': 1} |
| 42 | `pandas/read_csv@1.5.3-2.0.0/read_csv#1YY/pd.read_csv__._dev.csv__@1.5.3-2.0.0_L2_tempLst1.json` | mismatch | item 0 field (date_format, 26) mismatch: pred={'addKey': 'date_format'}, gt={'addKey': 'date_format=None'} |
| 43 | `pandas/testing.assert_extension_array_equal@1.5.3-2.0.0/testing.assert_extension_array_equal#1YY/tm.assert_extension_array_equal_b__c_@1.5.3-2.0.0_L5_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(obj, 7)'], gt_only=[] |
| 44 | `pandas/testing.assert_frame_equal@1.5.3-2.0.0/testing.assert_frame_equal#1YY/assert_frame_equal_df1__df1_@1.5.3-2.0.0_L5_tempLst1.json` | mismatch | item 0 field (atol, 16) mismatch: pred={'typeChange': "'float'", 'posChange': 15}, gt={'posChange': 15} |
| 45 | `pandas/testing.assert_index_equal@1.5.3-2.0.0/testing.assert_index_equal#1YY/tm.assert_index_equal_a__b_@1.5.3-2.0.0_L5_tempLst1.json` | mismatch | item 0 field (check_less_precise, 4) mismatch: pred={'delete': 1, 'replace': 'check_exact=True'}, gt={'delete': 1} |
| 46 | `pandas/testing.assert_series_equal@1.5.3-2.0.0/testing.assert_series_equal#1YY/tm.assert_series_equal_a__b_@1.5.3-2.0.0_L5_tempLst1.json` | mismatch | item 0 field (atol, 14) mismatch: pred={'typeChange': "'float'", 'posChange': 13}, gt={'posChange': 13} |
| 47 | `plotly/plotly.figure_factory.create_choropleth@2.4.1-2.5.0/plotly.figure_factory.create_choropleth#1YY/ff.create_choropleth_fips__values_@2.4.1-2.5.0_L11_tempLst1.json` | mismatch | item 0 field (offline_mode, 9) mismatch: pred={'delete': 1, 'replace': 'show_hover=True'}, gt={'delete': 1} |
| 48 | `polars/polars.expr.str.strptime@0.17.15-0.18.0/polars.expr.str.strptime#1YY/a.str.strptime_pl.Date_@0.17.15-0.18.0_L4_tempLst1.json` | mismatch | item 0 field (utc, 6) mismatch: pred={'typeChange': 'bool\|None'}, gt={} |
| 49 | `rich/rich.syntax.Syntax@10.16.2-11.0.0/rich.syntax.Syntax#1YY/Syntax__print__hello_world______python__@10.16.2-11.0.0_L2_tempLst1.json` | mismatch | item 0 field (lexer_name, 1) mismatch: pred={'typeChange': 'Union[pygments.lexer.Lexer,str]', 'rename': 'lexer'}, gt={'rename': 'lexer'} |
| 50 | `scipy/scipy.linalg.solve@1.10.1-1.11.0/scipy.linalg.solve#1YY/scipy.linalg.solve_a__b_@1.10.1-1.11.0_L4_tempLst1.json` | mismatch | item 0 field (sym_pos, 2) mismatch: pred={'delete': 1, 'replace': 'lower=False'}, gt={'delete': 1} |
| 51 | `scipy/scipy.linalg.solve_banded@1.8.1-1.9.0/scipy.linalg.solve_banded#1YY/solve_banded_l_and_u__ab__b_@1.8.1-1.9.0_L6_tempLst1.json` | mismatch | item 0 field (debug, 5) mismatch: pred={'delete': 1, 'replace': 'check_finite=True'}, gt={'delete': 1} |
| 52 | `scipy/scipy.linalg.solve_triangular@1.8.1-1.9.0/scipy.linalg.solve_triangular#1YY/solve_triangular_a__b_@1.8.1-1.9.0_L5_tempLst1.json` | mismatch | item 0 field (debug, 6) mismatch: pred={'delete': 1, 'replace': 'check_finite=True'}, gt={'delete': 1} |
| 53 | `scipy/scipy.optimize.fmin_cobyla@0.19.1-1.0.0/scipy.optimize.fmin_cobyla#1YY/fmin_cobyla_objective__x0__constraints_@0.19.1-1.0.0_L13_tempLst1.json` | mismatch | item 0 field (iprint, 7) mismatch: pred={'delete': 1, 'replace': 'maxfun=1000'}, gt={'delete': 1} |
| 54 | `scipy/scipy.sparse.linalg.bicg@0.19.1-1.0.0/scipy.sparse.linalg.bicg#1YY/spla.bicg_A__b_@0.19.1-1.0.0_L6_tempLst1.json` | mismatch | item 0 field (xtype, 5) mismatch: pred={'delete': 1, 'replace': 'M=None'}, gt={'delete': 1} |
| 55 | `scipy/scipy.sparse.linalg.cg@0.19.1-1.0.0/scipy.sparse.linalg.cg#1YY/cg_A__b_@0.19.1-1.0.0_L5_tempLst1.json` | mismatch | item 0 field (xtype, 5) mismatch: pred={'delete': 1, 'replace': 'M=None'}, gt={'delete': 1} |
| 56 | `scipy/scipy.sparse.linalg.cgs@0.19.1-1.0.0/scipy.sparse.linalg.cgs#1YY/cgs_A__b_@0.19.1-1.0.0_L6_tempLst1.json` | mismatch | item 0 field (xtype, 5) mismatch: pred={'delete': 1, 'replace': 'M=None'}, gt={'delete': 1} |
| 57 | `scipy/scipy.sparse.linalg.gmres@0.19.1-1.0.0/scipy.sparse.linalg.gmres#1YY/gmres_A__b_@0.19.1-1.0.0_L13_tempLst1.json` | mismatch | item 0 field (xtype, 6) mismatch: pred={'delete': 1, 'replace': 'M=None'}, gt={'delete': 1} |
| 58 | `scipy/scipy.sparse.linalg.minres@0.19.1-1.0.0/scipy.sparse.linalg.minres#1YY/minres_A__b_@0.19.1-1.0.0_L6_tempLst1.json` | mismatch | item 0 field (xtype, 6) mismatch: pred={'delete': 1, 'replace': 'M=None'}, gt={'delete': 1} |
| 59 | `scipy/scipy.stats.rv_continuous@1.10.1-1.11.0/scipy.stats.rv_continuous#1YY/stats.rv_continuous__@1.10.1-1.11.0_L2_tempLst1.json` | mismatch | item 0 field (extradoc, 8) mismatch: pred={'delete': 1, 'replace': 'seed'}, gt={'delete': 1} |
| 60 | `scipy/scipy.stats.rv_discrete.expect@0.16.1-0.17.0/scipy.stats.rv_discrete.expect#1YY/custom_distribution.expect__@0.16.1-0.17.0_L6_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(maxcount, 6)'], gt_only=[] |
| 61 | `scipy/scipy.stats.rv_discrete@1.10.1-1.11.0/scipy.stats.rv_discrete#1YY/rv_discrete__@1.10.1-1.11.0_L2_tempLst1.json` | mismatch | item 0 field (extradoc, 9) mismatch: pred={'delete': 1, 'replace': 'seed=None'}, gt={'delete': 1} |
| 62 | `sklearn/linear_model.lasso_path@0.15.2-0.16.0/linear_model.lasso_path#1YY/lasso_path_X__y_@0.15.2-0.16.0_L5_tempLst1.json` | mismatch | item 0 field (coef_init, 10) mismatch: pred={'posChange': 8}, gt={'posChange': 8, 'replace': 'return_n_iter=False'} |
| 63 | `sklearn/sklearn.feature_selection.RFECV@0.17.1-0.18/sklearn.feature_selection.RFECV#1YY/RFECV_estimator_@0.17.1-0.18_L6_tempLst1.json` | mismatch | item 0 field (estimator_params, 4) mismatch: pred={'delete': 1, 'replace': 'verbose=0'}, gt={'delete': 1} |
| 64 | `tensorflow/tf.contrib.data.make_csv_dataset@1.10.1-1.11.0/tf.contrib.data.make_csv_dataset#1NN/tf.contrib.data.make_csv_dataset__._dev.csv___1__None__None__None__None_______True______True__None__True__10000__None__1__1__2__False__1_@1.10.1-1.11.0_L2_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(compression_type, 18)'], gt_only=[] |
| 65 | `torch/torch.btrifact@1.0.1-1.1.0/torch.btrifact#1YY/torch.btrifact_A_@1.0.1-1.1.0_L3_tempLst1.json` | mismatch | item 0 field (info, 1) mismatch: pred={'delete': 1, 'replace': 'out=None'}, gt={'delete': 1} |
| 66 | `tornado/tornado.autoreload.start@4.5.3-5.0/tornado.autoreload.start#1YY/tornado.autoreload.start__@4.5.3-5.0_L3_tempLst1.json` | mismatch | item 0 field (io_loop, 0) mismatch: pred={'delete': 1, 'replace': 'check_time=500'}, gt={'delete': 1} |
| 67 | `tornado/tornado.httpclient.AsyncHTTPClient.fetch@5.1.1-6.0/tornado.httpclient.AsyncHTTPClient.fetch#1YY/http_client.fetch__http___example.com__@5.1.1-6.0_L6_tempLst1.json` | mismatch | item 0 field (callback, 1) mismatch: pred={'delete': 1, 'replace': 'raise_error=True'}, gt={'delete': 1} |
| 68 | `tornado/tornado.iostream.BaseIOStream.read_bytes@5.1.1-6.0/tornado.iostream.BaseIOStream.read_bytes#1YY/stream.read_bytes_10_@5.1.1-6.0_L11_tempLst1.json` | mismatch | item 0 field (callback, 1) mismatch: pred={'delete': 1, 'replace': 'partial=False'}, gt={'delete': 1} |
| 69 | `tornado/tornado.tcpserver.TCPServer@4.5.3-5.0/tornado.tcpserver.TCPServer#1YY/tornado.tcpserver.TCPServer__@4.5.3-5.0_L3_tempLst1.json` | mismatch | item 0 field (io_loop, 0) mismatch: pred={'delete': 1, 'replace': 'ssl_options=None'}, gt={'delete': 1} |

## 语义不相关

| 指标 | 数值 |
| --- | ---: |
| 样例数 | 113 |
| 正确 | 33 |
| 错误 | 80 |
| 正确率 | 29.20% |

### 错误样例

| 序号 | 样例路径 | 错误类型 | 差异说明 |
| --- | --- | --- | --- |
| 1 | `click/click.Command@7.0-7.1/click.Command#1YY/click.Command__my_command__@7.0-7.1_L2_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(no_args_is_help, 9)'], gt_only=[] |
| 2 | `dask/dask.dataframe.core.drop@2.2.0-2.3.0/dask.dataframe.core.drop#1YY/ddf.drop__B___1_@2.2.0-2.3.0_L5_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(columns, 2)'], gt_only=[] |
| 3 | `dask/dask.dataframe.drop_duplicates@2.4.0-2.5.0/dask.dataframe.drop_duplicates#1YY/ddf.drop_duplicates__@2.4.0-2.5.0_L5_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(subset, 0)'], gt_only=[] |
| 4 | `dask/dask.dataframe.repartition@1.2.2-2.0.0/dask.dataframe.repartition#1YY/ddf.repartition_None__10_@1.2.2-2.0.0_L5_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(partition_size, 2)'], gt_only=[] |
| 5 | `dask/dask.dataframe.utils.assert_eq@2022.5.2-2022.6.0/dask.dataframe.utils.assert_eq#1YY/assert_eq_ddf_result__pdf_result_@2022.5.2-2022.6.0_L8_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(sort_results, 6)'], gt_only=[] |
| 6 | `flask/from_file@2.2.5-2.3.0/from_file#1YY/app.config.from_file__._test.json___json.load_@2.2.5-2.3.0_L4_tempLst1.json` | mismatch | item 0 field (load, 1) mismatch: pred={}, gt={'typeChange': 't.Callable[[t.IO[t.Any]],t.Mapping]'} |
| 7 | `gensim/gensim.models.base_any2vec.BaseWordEmbeddingsModel@3.4.0-3.5.0/gensim.models.base_any2vec.BaseWordEmbeddingsModel#1YY/BaseWordEmbeddingsModel__@3.4.0-3.5.0_L2_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(ns_exponent, 13)'], gt_only=[] |
| 8 | `gensim/gensim.models.doc2vec.Doc2Vec@3.5.0-3.6.0/gensim.models.doc2vec.Doc2Vec#1YY/Doc2Vec__@3.5.0-3.6.0_L3_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(corpus_file, 1)'], gt_only=[] |
| 9 | `gensim/gensim.models.ldamodel.LdaModel.diff@2.3.0-3.0.0/gensim.models.ldamodel.LdaModel.diff#1YY/lda1.diff_lda2_@2.3.0-3.0.0_L9_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(diagonal, 4)'], gt_only=[] |
| 10 | `gensim/gensim.models.word2vec.Word2Vec.intersect_word2vec_format@0.13.1-0.13.2/gensim.models.word2vec.Word2Vec.intersect_word2vec_format#1YY/model.intersect_word2vec_format_fname_@0.13.1-0.13.2_L7_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(lockf, 1)'], gt_only=[] |
| 11 | `gensim/gensim.models.word2vec.Word2Vec.train@1.0.1-2.0.0/gensim.models.word2vec.Word2Vec.train#1NN/model.train_sentences_@1.0.1-2.0.0_L5_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(end_alpha, 5)', '(epochs, 3)', '(start_alpha, 4)'], gt_only=[] |
| 12 | `keras/DepthwiseConv2D@2.2.4-2.2.5/DepthwiseConv2D#1YY/DepthwiseConv2D__3__3__@2.2.4-2.2.5_L4_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(dilation_rate, 5)'], gt_only=[] |
| 13 | `matplotlib/matplotlib.gridspec.GridSpec@2.1.2-2.2.0/matplotlib.gridspec.GridSpec#1YY/gridspec.GridSpec_2__2_@2.1.2-2.2.0_L3_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(figure, 2)'], gt_only=[] |
| 14 | `networkx/betweenness_centrality@1.5-1.6/betweenness_centrality#1YY/nx.betweenness_centrality_G_@1.5-1.6_L4_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(k, 1)'], gt_only=[] |
| 15 | `numpy/numpy.ma.argsort@1.12.1-1.13.0/numpy.ma.argsort#1YY/np.ma.argsort_data_@1.12.1-1.13.0_L5_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(endwith, 4)'], gt_only=[] |
| 16 | `numpy/numpy.quantile@1.21.6-1.22.0/numpy.quantile#1YY/np.quantile_a__q_@1.21.6-1.22.0_L9_tempLst1.json` | mismatch | item 0 field (interpolation, 5) mismatch: pred={'pos2key': 'interpolation', 'replace': 'method=linear'}, gt={'replace': "method='linear'", 'pos2key': 'interpolation'} |
| 17 | `pandas/DataFrame.ewm@1.3.5-1.4.0/DataFrame.ewm#1YY/df.ewm_0.5_@1.3.5-1.4.0_L4_tempLst1.json` | mismatch | item 0 field (times, 8) mismatch: pred={'typeChange': "'str\|np.ndarray\|DataFrame\|Series\|None'"}, gt={'typeChange': 'str\|np.ndarray\|DataFrame\|Series\|None'} |
| 18 | `pandas/DataFrame.reset_index@1.4.4-1.5.0/DataFrame.reset_index#1YY/df.reset_index__@1.4.4-1.5.0_L4_tempLst1.json` | mismatch | item 0 field (level, 0) mismatch: pred={'typeChange': "'IndexLabel'"}, gt={'typeChange': 'IndexLabel'} |
| 19 | `pandas/DataFrame.rolling@1.4.4-1.5.0/DataFrame.rolling#1YY/df.rolling_2_@1.4.4-1.5.0_L4_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(step, 7)'], gt_only=[] |
| 20 | `pandas/DataFrame.to_stata@1.3.5-1.4.0/DataFrame.to_stata#1YY/df.to_stata__animals.dta__@1.3.5-1.4.0_L3_tempLst1.json` | mismatch | item 0 field (path, 0) mismatch: pred={'typeChange': "'FilePath\|WriteBuffer[bytes]'"}, gt={'typeChange': 'FilePath\|WriteBuffer[bytes]'} |
| 21 | `pandas/Series.ewm@1.3.5-1.4.0/Series.ewm#1YY/df.ewm_0.5_@1.3.5-1.4.0_L4_tempLst1.json` | mismatch | item 0 field (times, 8) mismatch: pred={'typeChange': "'str\|np.ndarray\|DataFrame\|Series\|None'"}, gt={'typeChange': 'str\|np.ndarray\|DataFrame\|Series\|None'} |
| 22 | `pandas/Series.rolling@1.4.4-1.5.0/Series.rolling#1YY/df.rolling_2_@1.4.4-1.5.0_L4_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(step, 7)'], gt_only=[] |
| 23 | `pandas/Styler.background_gradient@1.2.5-1.3.0/Styler.background_gradient#1YY/df.style.background_gradient__@1.2.5-1.3.0_L13_tempLst1.json` | mismatch | item 0 field (axis, 3) mismatch: pred={'typeChange': "'Axis\|None'"}, gt={'typeChange': 'Axis\|None'} |
| 24 | `pandas/Styler.format@1.2.5-1.3.0/Styler.format#1YY/df.style.format____.2____@1.2.5-1.3.0_L4_tempLst1.json` | mismatch | item 0 field (formatter, 0) mismatch: pred={'typeChange': "'ExtFormatter\|None'"}, gt={} |
| 25 | `pandas/melt@1.0.5-1.1.0/melt#1YY/pd.melt_df_@1.0.5-1.1.0_L3_tempLst1.json` | mismatch | item 0 field (frame, 0) mismatch: pred={'typeChange': "'DataFrame'"}, gt={'typeChange': 'DataFrame'} |
| 26 | `pandas/read_csv@1.2.5-1.3.0/read_csv#1YY/pd.read_csv__._dev.csv__@1.2.5-1.3.0_L2_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(encoding_errors, 42)', '(on_bad_lines, 46)'], gt_only=[] |
| 27 | `pandas/testing.assert_frame_equal@1.0.5-1.1.0/testing.assert_frame_equal#1YY/assert_frame_equal_df1__df1_@1.0.5-1.1.0_L5_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(check_freq, 13)'], gt_only=[] |
| 28 | `pandas/testing.assert_series_equal@1.0.5-1.1.0/testing.assert_series_equal#1YY/assert_series_equal_df1__df1_@1.0.5-1.1.0_L5_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(check_freq, 11)'], gt_only=[] |
| 29 | `pandas/testing.assert_series_equal@1.1.5-1.2.0/testing.assert_series_equal#1YY/tm.assert_series_equal_a__b_@1.1.5-1.2.0_L5_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(check_flags, 12)'], gt_only=[] |
| 30 | `plotly/plotly.express.area@4.2.1-4.3.0/plotly.express.area#1YY/px.area__@4.2.1-4.3.0_L3_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(facet_col_wrap, 11)'], gt_only=[] |
| 31 | `plotly/plotly.express.bar@4.14.3-5.0.0/plotly.express.bar#1YY/px.bar__@4.14.3-5.0.0_L3_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(pattern_shape, 4)', '(pattern_shape_map, 27)', '(pattern_shape_sequence, 26)'], gt_only=[] |
| 32 | `plotly/plotly.express.bar@4.2.1-4.3.0/plotly.express.bar#1YY/px.bar__@4.2.1-4.3.0_L3_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(facet_col_wrap, 6)'], gt_only=[] |
| 33 | `plotly/plotly.express.bar@5.4.0-5.5.0/plotly.express.bar#1YY/px.bar__@5.4.0-5.5.0_L3_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(text_auto, 37)'], gt_only=[] |
| 34 | `plotly/plotly.express.bar_polar@4.14.3-5.0.0/plotly.express.bar_polar#1YY/px.bar_polar__@4.14.3-5.0.0_L3_tempLst1.json` | mismatch | item 0 field (barnorm, 17) mismatch: pred={'posChange': 20}, gt={'posChange': 20, 'replace': 'pattern_shape_map=None'} |
| 35 | `plotly/plotly.express.bar_polar@4.3.0-4.4.0/plotly.express.bar_polar#1YY/px.bar_polar__@4.3.0-4.4.0_L3_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(range_theta, 18)'], gt_only=[] |
| 36 | `plotly/plotly.express.box@4.2.1-4.3.0/plotly.express.box#1YY/px.box__@4.2.1-4.3.0_L3_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(facet_col_wrap, 6)'], gt_only=[] |
| 37 | `plotly/plotly.express.density_contour@5.1.0-5.2.1/plotly.express.density_contour#1YY/px.density_contour__@5.1.0-5.2.1_L3_tempLst1.json` | mismatch | item 0 field (log_x, 23) mismatch: pred={'posChange': 25, 'replace': "trendline_scope='trace'"}, gt={'posChange': 25} |
| 38 | `plotly/plotly.express.density_heatmap@4.2.1-4.3.0/plotly.express.density_heatmap#1YY/px.density_heatmap__@4.2.1-4.3.0_L3_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(facet_col_wrap, 6)'], gt_only=[] |
| 39 | `plotly/plotly.express.histogram@4.14.3-5.0.0/plotly.express.histogram#1YY/px.histogram__@4.14.3-5.0.0_L3_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(pattern_shape, 4)', '(pattern_shape_map, 19)', '(pattern_shape_sequence, 18)'], gt_only=[] |
| 40 | `plotly/plotly.express.histogram@4.2.1-4.3.0/plotly.express.histogram#1YY/px.histogram__@4.2.1-4.3.0_L3_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(facet_col_wrap, 6)'], gt_only=[] |
| 41 | `plotly/plotly.express.histogram@5.4.0-5.5.0/plotly.express.histogram#1YY/px.histogram__@5.4.0-5.5.0_L3_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(text_auto, 33)'], gt_only=[] |
| 42 | `plotly/plotly.express.imshow@4.13.0-4.14.0/plotly.express.imshow#1YY/px.imshow_img_rgb_@4.13.0-4.14.0_L4_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(animation_frame, 7)', '(facet_col, 8)', '(facet_col_spacing, 10)'], gt_only=[] |
| 43 | `plotly/plotly.express.line@4.2.1-4.3.0/plotly.express.line#1YY/px.line__@4.2.1-4.3.0_L3_tempLst1.json` | mismatch | item 0 field (error_x, 12) mismatch: pred={'posChange': 13}, gt={'posChange': 13, 'replace': 'facet_col_wrap=0'} |
| 44 | `plotly/plotly.express.line@5.1.0-5.2.1/plotly.express.line#1YY/px.line__@5.1.0-5.2.1_L3_tempLst1.json` | mismatch | item 0 field (log_x, 28) mismatch: pred={'posChange': 32, 'replace': 'symbol_sequence=None'}, gt={'posChange': 32} |
| 45 | `plotly/plotly.express.line_3d@5.1.0-5.2.1/plotly.express.line_3d#1YY/px.line_3d__@5.1.0-5.2.1_L3_tempLst1.json` | mismatch | item 0 field (log_x, 25) mismatch: pred={'posChange': 29, 'replace': 'symbol_sequence=None'}, gt={'posChange': 29} |
| 46 | `plotly/plotly.express.line_geo@5.1.0-5.2.1/plotly.express.line_geo#1YY/px.line_geo__@5.1.0-5.2.1_L3_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(markers, 30)', '(symbol, 19)', '(symbol_map, 29)'], gt_only=[] |
| 47 | `plotly/plotly.express.line_mapbox@4.3.0-4.4.0/plotly.express.line_mapbox#1YY/px.line_mapbox_us_cities___lat____lon__@4.3.0-4.4.0_L5_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(center, 16)', '(mapbox_style, 17)'], gt_only=[] |
| 48 | `plotly/plotly.express.line_polar@4.3.0-4.4.0/plotly.express.line_polar#1YY/px.line_polar__@4.3.0-4.4.0_L3_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(range_theta, 24)'], gt_only=[] |
| 49 | `plotly/plotly.express.line_polar@5.1.0-5.2.1/plotly.express.line_polar#1YY/px.line_polar__@5.1.0-5.2.1_L3_tempLst1.json` | mismatch | item 0 field (direction, 18) mismatch: pred={'posChange': 22, 'replace': 'symbol_sequence=None'}, gt={'posChange': 22} |
| 50 | `plotly/plotly.express.line_ternary@5.1.0-5.2.1/plotly.express.line_ternary#1YY/px.line_ternary__@5.1.0-5.2.1_L3_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(markers, 22)', '(symbol, 7)', '(symbol_map, 21)'], gt_only=[] |
| 51 | `plotly/plotly.express.scatter@5.1.0-5.2.1/plotly.express.scatter#1YY/px.scatter__@5.1.0-5.2.1_L3_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(trendline_options, 36)', '(trendline_scope, 38)'], gt_only=[] |
| 52 | `plotly/plotly.express.scatter_mapbox@4.3.0-4.4.0/plotly.express.scatter_mapbox#1YY/px.scatter_mapbox_df___centroid_lat____centroid_lon__@4.3.0-4.4.0_L3_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(center, 21)', '(mapbox_style, 22)'], gt_only=[] |
| 53 | `plotly/plotly.express.scatter_polar@4.3.0-4.4.0/plotly.express.scatter_polar#1YY/px.scatter_polar__@4.3.0-4.4.0_L3_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(range_theta, 26)'], gt_only=[] |
| 54 | `plotly/plotly.express.strip@4.2.1-4.3.0/plotly.express.strip#1YY/px.strip__@4.2.1-4.3.0_L3_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(facet_col_wrap, 6)'], gt_only=[] |
| 55 | `plotly/plotly.express.sunburst@4.4.1-4.5.0/plotly.express.sunburst#1YY/px.sunburst__@4.4.1-4.5.0_L3_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(path, 4)'], gt_only=[] |
| 56 | `plotly/plotly.express.treemap@4.4.1-4.5.0/plotly.express.treemap#1YY/px.treemap__@4.4.1-4.5.0_L3_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(path, 5)'], gt_only=[] |
| 57 | `plotly/plotly.express.violin@4.2.1-4.3.0/plotly.express.violin#1YY/px.violin__@4.2.1-4.3.0_L3_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(facet_col_wrap, 6)'], gt_only=[] |
| 58 | `plotly/plotly.figure_factory.create_violin@2.0.8-2.0.9/plotly.figure_factory.create_violin#1YY/create_violin_data_list_@2.0.8-2.0.9_L5_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(sort, 7)'], gt_only=[] |
| 59 | `polars/polars.repeat@0.17.14-0.17.15/polars.repeat#1YY/pl.repeat__z___3_@0.17.14-0.17.15_L2_tempLst1.json` | mismatch | item 0 field (value, 0) mismatch: pred={'typeChange': "'PythonLiteral\|None'"}, gt={'typeChange': 'PythonLiteral\|None'} |
| 60 | `rich/Columns@1.3.0-1.3.1/Columns#1YY/Columns_renderables_@1.3.0-1.3.1_L3_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(width, 2)'], gt_only=[] |
| 61 | `rich/install@12.5.1-12.6.0/install#1YY/pretty.install__@12.5.1-12.6.0_L2_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(max_depth, 6)'], gt_only=[] |
| 62 | `rich/rich.syntax.Syntax.from_path@11.0.0-11.1.0/rich.syntax.Syntax.from_path#1YY/Syntax.from_path__._example.py__@11.0.0-11.1.0_L2_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(lexer, 2)'], gt_only=[] |
| 63 | `scipy/scipy.stats.qmc.LatinHypercube@1.9.3-1.10.0/scipy.stats.qmc.LatinHypercube#1YY/qmc.LatinHypercube_d_@1.9.3-1.10.0_L7_tempLst1.json` | mismatch | item 0 field (optimization, 4) mismatch: pred={'typeChange': "Optional[Literal[('random-cd','lloyd')]]", 'posChange': 5}, gt={'typeChange': '"Optional[Literal[(\'random-cd\',\'lloyd\')]]"'} |
| 64 | `scipy/scipy.stats.ttest_ind@1.6.3-1.7.0/scipy.stats.ttest_ind#1YY/stats.ttest_ind_a__b_@1.6.3-1.7.0_L4_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(permutations, 5)'], gt_only=[] |
| 65 | `sklearn/calibration.CalibratedClassifierCV@1.1.3-1.2.0/calibration.CalibratedClassifierCV#1YY/CalibratedClassifierCV__@1.1.3-1.2.0_L6_tempLst1.json` | mismatch | item 0 field (base_estimator, 0) mismatch: pred={'replace': 'estimator=None'}, gt={'replace': 'estimator=None', 'pos2key': 'base_estimator'} |
| 66 | `sklearn/ensemble.AdaBoostClassifier@1.1.3-1.2.0/ensemble.AdaBoostClassifier#1YY/AdaBoostClassifier__@1.1.3-1.2.0_L4_tempLst1.json` | mismatch | item 0 field (base_estimator, 0) mismatch: pred={'replace': 'estimator=None'}, gt={'replace': 'estimator=None', 'pos2key': 'base_estimator'} |
| 67 | `sklearn/ensemble.AdaBoostRegressor@1.1.3-1.2.0/ensemble.AdaBoostRegressor#1YY/AdaBoostRegressor__@1.1.3-1.2.0_L4_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(estimator, 0)'], gt_only=[] |
| 68 | `sklearn/ensemble.BaggingClassifier@1.1.3-1.2.0/ensemble.BaggingClassifier#1YY/BaggingClassifier__@1.1.3-1.2.0_L5_tempLst1.json` | mismatch | item 0 field (base_estimator, 0) mismatch: pred={'replace': 'estimator'}, gt={'replace': 'estimator=None', 'pos2key': 'base_estimator'} |
| 69 | `sklearn/ensemble.BaggingRegressor@1.1.3-1.2.0/ensemble.BaggingRegressor#1YY/BaggingRegressor__@1.1.3-1.2.0_L5_tempLst1.json` | mismatch | item 0 field (base_estimator, 0) mismatch: pred={'replace': 'estimator'}, gt={'replace': 'estimator=None', 'pos2key': 'base_estimator'} |
| 70 | `sklearn/linear_model.RANSACRegressor@0.17.1-0.18/linear_model.RANSACRegressor#1YY/RANSACRegressor__@0.17.1-0.18_L2_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(loss, 10)'], gt_only=[] |
| 71 | `sklearn/linear_model.RANSACRegressor@1.0.2-1.1.0/linear_model.RANSACRegressor#1YY/RANSACRegressor__@1.0.2-1.1.0_L5_tempLst1.json` | mismatch | item 0 field (base_estimator, 0) mismatch: pred={'rename': 'estimator'}, gt={'replace': 'estimator=None', 'pos2key': 'base_estimator'} |
| 72 | `sklearn/sklearn.cluster.SpectralClustering@0.21.3-0.22/sklearn.cluster.SpectralClustering#1YY/SpectralClustering_5_@0.21.3-0.22_L4_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(n_components, 2)'], gt_only=[] |
| 73 | `sklearn/sklearn.discriminant_analysis.QuadraticDiscriminantAnalysis@0.18.1-0.19.0/sklearn.discriminant_analysis.QuadraticDiscriminantAnalysis#1YY/QuadraticDiscriminantAnalysis__@0.18.1-0.19.0_L5_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(store_covariances, 4)'], gt_only=[] |
| 74 | `sklearn/sklearn.linear_model.PassiveAggressiveClassifier@0.18.1-0.19.0/sklearn.linear_model.PassiveAggressiveClassifier#1YY/PassiveAggressiveClassifier__@0.18.1-0.19.0_L2_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(max_iter, 2)'], gt_only=[] |
| 75 | `sklearn/sklearn.svm.NuSVC@0.21.3-0.22/sklearn.svm.NuSVC#1YY/NuSVC__@0.21.3-0.22_L5_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(break_ties, 13)'], gt_only=[] |
| 76 | `sklearn/sklearn.svm.SVC@0.21.3-0.22/sklearn.svm.SVC#1YY/SVC__@0.21.3-0.22_L5_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(break_ties, 13)'], gt_only=[] |
| 77 | `sympy/sympy.physics.mechanics.PinJoint@1.11.1-1.12/sympy.physics.mechanics.PinJoint#1YY/PinJoint__PC___parent__child_@1.11.1-1.12_L4_tempLst1.json` | mismatch | item 0 field (child_joint_pos, 6) mismatch: pred={'rename': 'child_point', 'posChange': 13}, gt={'posChange': 13, 'replace': 'child_point=None'} |
| 78 | `sympy/sympy.physics.mechanics.PrismaticJoint@1.11.1-1.12/sympy.physics.mechanics.PrismaticJoint#1YY/PrismaticJoint__PC___parent__child_@1.11.1-1.12_L4_tempLst1.json` | mismatch | item 0 field (child_joint_pos, 6) mismatch: pred={'rename': 'child_point', 'posChange': 13}, gt={'posChange': 13, 'replace': 'child_point=None'} |
| 79 | `tensorflow/tf.keras.losses.SparseCategoricalCrossentropy@2.9.3-2.10.0/tf.keras.losses.SparseCategoricalCrossentropy#1YY/tf.keras.losses.SparseCategoricalCrossentropy__@2.9.3-2.10.0_L2_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(ignore_class, 1)'], gt_only=[] |
| 80 | `tornado/tornado.httpclient.HTTPRequest@3.0.2-3.1/tornado.httpclient.HTTPRequest#1YY/tornado.httpclient.HTTPRequest__http___httpbin.org_get__@3.0.2-3.1_L2_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(auth_mode, 6)'], gt_only=[] |
