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
| 语义相关 | 171 | 101 | 70 | 59.06% |
| 语义不相关 | 113 | 17 | 96 | 15.04% |
| 合并后 | 284 | 118 | 166 | 41.55% |

## 语义相关

| 指标 | 数值 |
| --- | ---: |
| 样例数 | 171 |
| 正确 | 101 |
| 错误 | 70 |
| 正确率 | 59.06% |

### 错误样例

| 序号 | 样例路径 | 错误类型 | 差异说明 |
| --- | --- | --- | --- |
| 1 | `aiohttp/aiohttp.BaseConnector@0.8.1-0.8.2/aiohttp.BaseConnector#1YY/aiohttp.BaseConnector__@0.8.1-0.8.2_L2_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(keepalive_timeout, 2)', '(loop, 5)'], gt_only=['(loop, 4)'] |
| 2 | `aiohttp/aiohttp.ClientSession@1.3.5-2.0.0/aiohttp.ClientSession#1YY/aiohttp.ClientSession__@1.3.5-2.0.0_L18_tempLst1.json` | mismatch | item 0 field (conn_timeout, 16) mismatch: pred={'addKey': 'conn_timeout'}, gt={'addKey': 'conn_timeout=None'} |
| 3 | `aiohttp/aiohttp.TCPConnector@2.3.10-3.0.0/aiohttp.TCPConnector#1YY/aiohttp.TCPConnector__@2.3.10-3.0.0_L9_tempLst1.json` | mismatch | item 0 field (enable_cleanup_closed, 14) mismatch: pred={'posChange': 14}, gt={} |
| 4 | `dask/dask.dataframe.read_parquet@2022.4.1-2022.4.2/dask.dataframe.read_parquet#1YY/dd.read_parquet__._example.parquet__@2022.4.1-2022.4.2_L2_tempLst1.json` | mismatch | item 0 field (gather_statistics, 7) mismatch: pred={'delete': 1, 'replace': 'calculate_divisions=None'}, gt={'rename': 'calculate_divisions'} |
| 5 | `gensim/gensim.models.doc2vec.Doc2Vec.similarity_unseen_docs@4.0.1-4.1.0/gensim.models.doc2vec.Doc2Vec.similarity_unseen_docs#1YY/model.similarity_unseen_docs_doc_words1__doc_words2_@4.0.1-4.1.0_L7_tempLst1.json` | mismatch | item 0 field (steps, 4) mismatch: pred={'delete': 1, 'replace': 'epochs'}, gt={'rename': 'epochs'} |
| 6 | `gensim/gensim.models.fasttext.FastText@3.8.3-4.0.0/gensim.models.fasttext.FastText#1YY/FastText__@3.8.3-4.0.0_L2_tempLst1.json` | mismatch | item 0 field (compatible_hash, 27) mismatch: pred={'delete': 1, 'replace': 'max_final_vocab'}, gt={'delete': 1, 'replace': 'max_final_vocab=None'} |
| 7 | `httpx/Response@0.17.1-0.18.0/Response#1YY/Response_1_@0.17.1-0.18.0_L2_tempLst1.json` | mismatch | item 0 field (ext, 9) mismatch: pred={'delete': 1, 'replace': 'extensions'}, gt={'rename': 'extensions'} |
| 8 | `httpx/URL@0.13.3-0.14.0/URL#1YY/httpx.URL_url_str_@0.13.3-0.14.0_L4_tempLst1.json` | mismatch | item 0 field (params, 2) mismatch: pred={'typeChange': "Union[ForwardRef('QueryParams'),Mapping[str,Union[str,int,float,, gt={'posChange': 1} |
| 9 | `httpx/httpx.AsyncClient@0.11.1-0.12.0/httpx.AsyncClient#1YY/httpx.AsyncClient__@0.11.1-0.12.0_L3_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(trust_env, 15)', '(uds, 16)'], gt_only=['(trust_env, 16)', '(uds, 17)'] |
| 10 | `httpx/httpx.delete@0.7.4-0.7.5/httpx.delete#1YY/delete__https___example.com_resource__@0.7.4-0.7.5_L2_tempLst1.json` | mismatch | item 0 field (allow_redirects, 10) mismatch: pred={'posChange': 7}, gt={} |
| 11 | `jax/jax.experimental.jax2tf.convert@0.4.12-0.4.13/jax.experimental.jax2tf.convert#1YY/jax2tf.convert_sum_of_squares_@0.4.12-0.4.13_L7_tempLst1.json` | mismatch | item 0 field (enable_xla, 4) mismatch: pred={'typeChange': 'bool'}, gt={} |
| 12 | `matplotlib/matplotlib.colorbar.Colorbar.set_ticks@3.6.3-3.7.0/matplotlib.colorbar.Colorbar.set_ticks#1YY/cbar.set_ticks_ticks_@3.6.3-3.7.0_L7_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(minor, 3)'], gt_only=['(minor, 4)'] |
| 13 | `matplotlib/matplotlib.image.BboxImage@3.2.2-3.3.0/matplotlib.image.BboxImage#1YY/mpimg.BboxImage_bbox_@3.2.2-3.3.0_L6_tempLst1.json` | mismatch | item 0 field (filternorm, 5) mismatch: pred={'typeChange': 'bool'}, gt={} |
| 14 | `matplotlib/matplotlib.patheffects.SimplePatchShadow@1.4.3-1.5.0/matplotlib.patheffects.SimplePatchShadow#1YY/pe.SimplePatchShadow__@1.4.3-1.5.0_L5_tempLst1.json` | mismatch | item 0 field (patch_alpha, 3) mismatch: pred={'delete': 1, 'replace': 'rho'}, gt={'delete': 1} |
| 15 | `networkx/average_clustering@1.5-1.6/average_clustering#1YY/nx.average_clustering_G_@1.5-1.6_L4_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(nodes, 1)'], gt_only=[] |
| 16 | `networkx/average_neighbor_degree@1.5-1.6/average_neighbor_degree#1YY/nx.average_neighbor_degree_G_@1.5-1.6_L4_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(source, 1)', '(target, 2)'], gt_only=['(weight, 4)'] |
| 17 | `networkx/average_shortest_path_length@1.4-1.5/average_shortest_path_length#1YY/nx.average_shortest_path_length_G_@1.4-1.5_L4_tempLst1.json` | mismatch | item 0 field (weighted, 1) mismatch: pred={'delete': 1, 'replace': 'weight=None'}, gt={'rename': 'weight'} |
| 18 | `networkx/betweenness_centrality_source@1.4-1.5/betweenness_centrality_source#1YY/nx.betweenness_centrality_source_G_@1.4-1.5_L4_tempLst1.json` | mismatch | item 0 field (weighted_edges, 2) mismatch: pred={'delete': 1, 'replace': 'weight=None'}, gt={'rename': 'weight'} |
| 19 | `networkx/closeness_vitality@1.4-1.5/closeness_vitality#1YY/nx.closeness_vitality_G_@1.4-1.5_L4_tempLst1.json` | mismatch | item 0 field (weighted_edges, 2) mismatch: pred={'delete': 1, 'replace': 'weight=None'}, gt={'rename': 'weight'} |
| 20 | `networkx/degree@1.5-1.6/degree#1YY/G.degree__@1.5-1.6_L4_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(weight, 1)'], gt_only=[] |
| 21 | `networkx/edge_betweenness_centrality_subset@1.4-1.5/edge_betweenness_centrality_subset#1YY/nx.edge_betweenness_centrality_subset_G__sources__targets_@1.4-1.5_L6_tempLst1.json` | mismatch | item 0 field (weighted_edges, 4) mismatch: pred={'delete': 1, 'replace': 'weight=None'}, gt={'rename': 'weight'} |
| 22 | `networkx/geographical_threshold_graph@2.0-2.1/geographical_threshold_graph#1YY/nx.geographical_threshold_graph_10__0.1_@2.0-2.1_L2_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(p_dist, 6)'], gt_only=[] |
| 23 | `networkx/networkx.betweenness_centrality@1.4-1.5/networkx.betweenness_centrality#1YY/nx.betweenness_centrality_G_@1.4-1.5_L3_tempLst1.json` | mismatch | item 0 field (weighted_edges, 2) mismatch: pred={'delete': 1, 'replace': 'weight=None'}, gt={'rename': 'weight'} |
| 24 | `networkx/networkx.to_pandas_edgelist@2.8.8-3.0/networkx.to_pandas_edgelist#1YY/nx.to_pandas_edgelist_G_@2.8.8-3.0_L7_tempLst1.json` | mismatch | item 0 field (order, 5) mismatch: pred={'delete': 1, 'replace': 'edge_key'}, gt={'delete': 1} |
| 25 | `networkx/networkx.union@2.8.8-3.0/networkx.union#1YY/nx.union_G__H_@2.8.8-3.0_L6_tempLst1.json` | mismatch | item 0 field (rename, 2) mismatch: pred={'typeChange': 'iterable , optional'}, gt={} |
| 26 | `networkx/shortest_path@1.4-1.5/shortest_path#1YY/nx.shortest_path_G_@1.4-1.5_L4_tempLst1.json` | mismatch | item 0 field (weighted, 3) mismatch: pred={'delete': 1, 'replace': 'weight=None'}, gt={'rename': 'weight'} |
| 27 | `networkx/shortest_path_length@1.4-1.5/shortest_path_length#1YY/nx.shortest_path_length_G_@1.4-1.5_L4_tempLst1.json` | mismatch | item 0 field (weighted, 3) mismatch: pred={'delete': 1, 'replace': 'weight=None'}, gt={'rename': 'weight'} |
| 28 | `numpy/numpy.genfromtxt@1.9.3-1.10.0/numpy.genfromtxt#1YY/np.genfromtxt_f_@1.9.3-1.10.0_L4_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(max_rows, 21)'], gt_only=[] |
| 29 | `numpy/numpy.histogram2d@1.23.5-1.24.0/numpy.histogram2d#1YY/np.histogram2d_x__y_@1.23.5-1.24.0_L4_tempLst1.json` | mismatch | item 0 field (normed, 4) mismatch: pred={'delete': 1, 'replace': 'density'}, gt={'delete': 1} |
| 30 | `numpy/numpy.histogram@1.23.5-1.24.0/numpy.histogram#1YY/np.histogram_a_@1.23.5-1.24.0_L8_tempLst1.json` | mismatch | item 0 field (normed, 3) mismatch: pred={'delete': 1, 'replace': 'density'}, gt={'delete': 1} |
| 31 | `numpy/numpy.histogramdd@1.23.5-1.24.0/numpy.histogramdd#1YY/np.histogramdd_sample_@1.23.5-1.24.0_L3_tempLst1.json` | mismatch | item 0 field (normed, 3) mismatch: pred={'delete': 1, 'replace': 'density'}, gt={'delete': 1} |
| 32 | `pandas/DataFrame.between_time@1.5.3-2.0.0/DataFrame.between_time#1YY/ts.between_time__0_15____0_45__@1.5.3-2.0.0_L4_tempLst1.json` | mismatch | item 0 field (axis, 5) mismatch: pred={'typeChange': "'Axis\|None'", 'posChange': 3}, gt={'posChange': 3} |
| 33 | `pandas/DataFrame.groupby@1.5.3-2.0.0/DataFrame.groupby#1YY/df.groupby___Animal___@1.5.3-2.0.0_L3_tempLst1.json` | mismatch | item 0 field (group_keys, 5) mismatch: pred={'typeChange': "'bool'"}, gt={'typeChange': 'bool'} |
| 34 | `pandas/DataFrame.mask@1.5.3-2.0.0/DataFrame.mask#1YY/s.mask_s___0_@1.5.3-2.0.0_L4_tempLst1.json` | mismatch | item 0 field (other, 1) mismatch: pred={'typeChange': 'null'}, gt={} |
| 35 | `pandas/DataFrame.set_axis@1.5.3-2.0.0/DataFrame.set_axis#1YY/df.set_axis___a____b____c___@1.5.3-2.0.0_L3_tempLst1.json` | mismatch | item 0 field (copy, 4) mismatch: pred={'typeChange': "'bool\|None'", 'posChange': 3}, gt={'typeChange': 'bool\|None'} |
| 36 | `pandas/DataFrame.take@1.5.3-2.0.0/DataFrame.take#1YY/df.take__0__3__@1.5.3-2.0.0_L4_tempLst1.json` | mismatch | item 0 field (axis, 1) mismatch: pred={'typeChange': "'Axis'"}, gt={} |
| 37 | `pandas/DataFrame.to_latex@1.5.3-2.0.0/DataFrame.to_latex#1YY/df.to_latex__@1.5.3-2.0.0_L3_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(bold_rows, 9)', '(caption, 18)', '(column_format, 10)'], gt_only=['(bold_rows, 10)', '(caption, 19)', '(column_format, 11)'] |
| 38 | `pandas/Series.groupby@1.5.3-2.0.0/Series.groupby#1YY/ser.groupby___a____b____a____b___@1.5.3-2.0.0_L3_tempLst1.json` | mismatch | item 0 field (group_keys, 5) mismatch: pred={'typeChange': "'bool'"}, gt={'typeChange': 'bool'} |
| 39 | `pandas/Series.mask@1.5.3-2.0.0/Series.mask#1YY/s.mask_s___0_@1.5.3-2.0.0_L4_tempLst1.json` | mismatch | item 0 field (other, 1) mismatch: pred={'typeChange': 'null'}, gt={} |
| 40 | `pandas/Series.set_axis@1.5.3-2.0.0/Series.set_axis#1YY/s.set_axis___a____b____c___@1.5.3-2.0.0_L3_tempLst1.json` | mismatch | item 0 field (copy, 4) mismatch: pred={'typeChange': "'bool\|None'", 'posChange': 3}, gt={'typeChange': 'bool\|None'} |
| 41 | `pandas/Timestamp@1.5.3-2.0.0/Timestamp#1YY/pd.Timestamp__2017-01-01T12__@1.5.3-2.0.0_L2_tempLst1.json` | mismatch | item 0 field (freq, 1) mismatch: pred={'delete': 1, 'replace': 'year'}, gt={'delete': 1} |
| 42 | `pandas/bdate_range@1.5.3-2.0.0/bdate_range#1YY/pd.bdate_range__1_1_2018____1_08_2018__@1.5.3-2.0.0_L2_tempLst1.json` | mismatch | item 0 field (freq, 3) mismatch: pred={'typeChange': "'Frequency'"}, gt={} |
| 43 | `pandas/date_range@1.5.3-2.0.0/date_range#1YY/pd.date_range__1_1_2018____1_08_2018__@1.5.3-2.0.0_L2_tempLst1.json` | mismatch | item 0 field (inclusive, 8) mismatch: pred={'typeChange': "'IntervalClosedType'", 'posChange': 7}, gt={'typeChange': 'IntervalClosedType', 'posChange': 7} |
| 44 | `pandas/pandas.DataFrame.resample@1.5.3-2.0.0/pandas.DataFrame.resample#1YY/DataFrame.resample__3T__@1.5.3-2.0.0_L4_tempLst1.json` | mismatch | item 0 field (group_keys, 12) mismatch: pred={'typeChange': "'bool'", 'posChange': 10}, gt={'typeChange': 'bool', 'posChange': 10} |
| 45 | `pandas/pandas.Series.resample@1.5.3-2.0.0/pandas.Series.resample#1YY/series.resample__3T__@1.5.3-2.0.0_L4_tempLst1.json` | mismatch | item 0 field (group_keys, 12) mismatch: pred={'typeChange': "'bool'", 'posChange': 10}, gt={'typeChange': 'bool', 'posChange': 10} |
| 46 | `pandas/read_csv@1.5.3-2.0.0/read_csv#1YY/pd.read_csv__._dev.csv__@1.5.3-2.0.0_L2_tempLst1.json` | mismatch | item 0 field (cache_dates, 30) mismatch: pred={'posChange': 28}, gt={} |
| 47 | `pandas/testing.assert_extension_array_equal@1.5.3-2.0.0/testing.assert_extension_array_equal#1YY/tm.assert_extension_array_equal_b__c_@1.5.3-2.0.0_L5_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(obj, 7)'], gt_only=[] |
| 48 | `pandas/testing.assert_frame_equal@1.5.3-2.0.0/testing.assert_frame_equal#1YY/assert_frame_equal_df1__df1_@1.5.3-2.0.0_L5_tempLst1.json` | mismatch | item 0 field (atol, 16) mismatch: pred={'typeChange': "'float'", 'posChange': 15}, gt={'posChange': 15} |
| 49 | `pandas/testing.assert_series_equal@1.5.3-2.0.0/testing.assert_series_equal#1YY/tm.assert_series_equal_a__b_@1.5.3-2.0.0_L5_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(atol, 13)', '(check_categorical, 8)', '(check_category_order, 9)'], gt_only=['(atol, 14)', '(check_categorical, 9)', '(check_category_order, 10)'] |
| 50 | `plotly/plotly.figure_factory.create_choropleth@2.4.1-2.5.0/plotly.figure_factory.create_choropleth#1YY/ff.create_choropleth_fips__values_@2.4.1-2.5.0_L11_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(centroid_marker, 13)', '(county_outline, 12)', '(exponent_format, 15)'], gt_only=['(centroid_marker, 14)', '(county_outline, 13)', '(exponent_format, 16)'] |
| 51 | `polars/polars.Expr.map_dict@0.16.18-0.17.0/polars.Expr.map_dict#1YY/pl.col__country_code__.map_dict_country_code_dict_@0.16.18-0.17.0_L4_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(return_dtype, 3)'], gt_only=[] |
| 52 | `polars/polars.expr.str.strptime@0.17.15-0.18.0/polars.expr.str.strptime#1YY/a.str.strptime_pl.Date_@0.17.15-0.18.0_L4_tempLst1.json` | mismatch | item 0 field (utc, 6) mismatch: pred={'typeChange': 'bool\|None'}, gt={} |
| 53 | `rich/rich.syntax.Syntax@10.16.2-11.0.0/rich.syntax.Syntax#1YY/Syntax__print__hello_world______python__@10.16.2-11.0.0_L2_tempLst1.json` | mismatch | item 0 field (lexer_name, 1) mismatch: pred={'delete': 1, 'replace': 'lexer'}, gt={'rename': 'lexer'} |
| 54 | `rich/traceback.install@7.0.0-7.1.0/traceback.install#1YY/install__@7.0.0-7.1.0_L3_tempLst1.json` | mismatch | item 0 field (extra_lines, 4) mismatch: pred={'posChange': 3}, gt={} |
| 55 | `scipy/scipy.optimize.fmin_cobyla@0.19.1-1.0.0/scipy.optimize.fmin_cobyla#1YY/fmin_cobyla_objective__x0__constraints_@0.19.1-1.0.0_L13_tempLst1.json` | mismatch | item 0 field (iprint, 7) mismatch: pred={'delete': 1, 'replace': 'maxfun'}, gt={'delete': 1} |
| 56 | `scipy/scipy.spatial.distance.pdist@0.19.1-1.0.0/scipy.spatial.distance.pdist#1YY/pdist_X_@0.19.1-1.0.0_L3_tempLst1.json` | mismatch | item 0 field (p, 2) mismatch: pred={'delete': 1, 'replace': '*args'}, gt={'delete': 1} |
| 57 | `scipy/scipy.stats.rv_continuous@1.10.1-1.11.0/scipy.stats.rv_continuous#1YY/stats.rv_continuous__@1.10.1-1.11.0_L2_tempLst1.json` | mismatch | item 0 field (extradoc, 8) mismatch: pred={'delete': 1, 'replace': 'seed'}, gt={'delete': 1} |
| 58 | `scipy/scipy.stats.rv_discrete.expect@0.16.1-0.17.0/scipy.stats.rv_discrete.expect#1YY/custom_distribution.expect__@0.16.1-0.17.0_L6_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(maxcount, 6)'], gt_only=[] |
| 59 | `sklearn/ensemble.GradientBoostingRegressor@0.23.2-0.24.0/ensemble.GradientBoostingRegressor#1YY/GradientBoostingRegressor__@0.23.2-0.24.0_L6_tempLst1.json` | mismatch | item 0 field (random_state, 13) mismatch: pred={'typeChange': 'int, RandomState instance or None'}, gt={} |
| 60 | `sklearn/linear_model.LinearRegression@1.1.3-1.2.0/linear_model.LinearRegression#1YY/LinearRegression__@1.1.3-1.2.0_L5_tempLst1.json` | mismatch | item 0 field (copy_X, 3) mismatch: pred={'posChange': 2}, gt={} |
| 61 | `sklearn/linear_model.lasso_path@0.15.2-0.16.0/linear_model.lasso_path#1YY/lasso_path_X__y_@0.15.2-0.16.0_L5_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(positive, 11)'], gt_only=[] |
| 62 | `sklearn/sklearn.feature_selection.RFECV@0.17.1-0.18/sklearn.feature_selection.RFECV#1YY/RFECV_estimator_@0.17.1-0.18_L6_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(n_jobs, 5)'], gt_only=[] |
| 63 | `sympy/sympy.crypto.crypto.rsa_public_key@1.4-1.5/sympy.crypto.crypto.rsa_public_key#1YY/rsa_public_key_p__q__e_@1.4-1.5_L6_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(args, 0)', '(index, 0)', '(multipower, 0)'], gt_only=[] |
| 64 | `tensorflow/tf.contrib.data.make_csv_dataset@1.10.1-1.11.0/tf.contrib.data.make_csv_dataset#1NN/tf.contrib.data.make_csv_dataset__._dev.csv___1__None__None__None__None_______True______True__None__True__10000__None__1__1__2__False__1_@1.10.1-1.11.0_L2_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(compression_type, 18)', '(num_rows_for_inference, 17)', '(sloppy, 16)'], gt_only=['(num_rows_for_inference, 18)', '(sloppy, 17)'] |
| 65 | `tensorflow/tf.contrib.data.make_csv_dataset@1.8.0-1.9.0/tf.contrib.data.make_csv_dataset#1NN/tf.contrib.data.make_csv_dataset__._dev.csv___1__None__None__None_______True______True__None__None__True__1__None__1__1__2__False__tf.float32__1_@1.8.0-1.9.0_L2_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(select_columns, 5)'], gt_only=[] |
| 66 | `torch/torch.btrifact@1.0.1-1.1.0/torch.btrifact#1YY/torch.btrifact_A_@1.0.1-1.1.0_L3_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(out, 2)'], gt_only=[] |
| 67 | `tornado/tornado.httpclient.AsyncHTTPClient.fetch@5.1.1-6.0/tornado.httpclient.AsyncHTTPClient.fetch#1YY/http_client.fetch__http___example.com__@5.1.1-6.0_L6_tempLst1.json` | mismatch | item 0 field (raise_error, 2) mismatch: pred={'typeChange': 'bool', 'posChange': 1}, gt={'posChange': 1} |
| 68 | `tornado/tornado.httpclient.AsyncHTTPClient@2.4.1-3.0/tornado.httpclient.AsyncHTTPClient#1YY/tornado.httpclient.AsyncHTTPClient__@2.4.1-3.0_L2_tempLst1.json` | mismatch | item 0 field (max_clients, 1) mismatch: pred={'delete': 1, 'replace': 'force_instance=False'}, gt={'delete': 1} |
| 69 | `tornado/tornado.iostream.BaseIOStream.read_bytes@5.1.1-6.0/tornado.iostream.BaseIOStream.read_bytes#1YY/stream.read_bytes_10_@5.1.1-6.0_L11_tempLst1.json` | mismatch | item 0 field (num_bytes, 0) mismatch: pred={'typeChange': 'int'}, gt={} |
| 70 | `transformers/transformers.modeling_albert.AlbertForPreTraining.forward@2.11.0-3.0.0/transformers.modeling_albert.AlbertForPreTraining.forward#1YY/model.forward_input_ids_@2.11.0-3.0.0_L11_tempLst1.json` | mismatch | item 0 field (masked_lm_labels, 6) mismatch: pred={'delete': 1, 'replace': 'labels'}, gt={'rename': 'labels'} |

## 语义不相关

| 指标 | 数值 |
| --- | ---: |
| 样例数 | 113 |
| 正确 | 17 |
| 错误 | 96 |
| 正确率 | 15.04% |

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
| 11 | `gensim/gensim.models.ldamodel.LdaModel.diff@2.3.0-3.0.0/gensim.models.ldamodel.LdaModel.diff#1YY/lda1.diff_lda2_@2.3.0-3.0.0_L9_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(annotation, 6)', '(diagonal, 5)'], gt_only=['(annotation, 5)'] |
| 12 | `gensim/gensim.models.word2vec.Word2Vec.intersect_word2vec_format@0.13.1-0.13.2/gensim.models.word2vec.Word2Vec.intersect_word2vec_format#1YY/model.intersect_word2vec_format_fname_@0.13.1-0.13.2_L7_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(lockf, 1)'], gt_only=[] |
| 13 | `gensim/gensim.models.word2vec.Word2Vec.train@1.0.1-2.0.0/gensim.models.word2vec.Word2Vec.train#1NN/model.train_sentences_@1.0.1-2.0.0_L5_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(end_alpha, 5)', '(epochs, 3)', '(start_alpha, 4)'], gt_only=[] |
| 14 | `keras/Conv2DTranspose@2.2.2-2.2.3/Conv2DTranspose#1YY/Conv2DTranspose_64___3__3__@2.2.2-2.2.3_L4_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(dilation_rate, 6)'], gt_only=[] |
| 15 | `keras/DepthwiseConv2D@2.2.4-2.2.5/DepthwiseConv2D#1YY/DepthwiseConv2D__3__3__@2.2.4-2.2.5_L4_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(dilation_rate, 5)'], gt_only=[] |
| 16 | `keras/keras.preprocessing.image.ImageDataGenerator@2.1.4-2.1.5/keras.preprocessing.image.ImageDataGenerator#1YY/ImageDataGenerator__@2.1.4-2.1.5_L2_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(brightness_range, 9)'], gt_only=[] |
| 17 | `matplotlib/matplotlib.gridspec.GridSpec@2.1.2-2.2.0/matplotlib.gridspec.GridSpec#1YY/gridspec.GridSpec_2__2_@2.1.2-2.2.0_L3_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(figure, 2)'], gt_only=[] |
| 18 | `networkx/betweenness_centrality@1.5-1.6/betweenness_centrality#1YY/nx.betweenness_centrality_G_@1.5-1.6_L4_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(k, 1)'], gt_only=[] |
| 19 | `networkx/networkx.linalg.graphmatrix.adjacency_matrix@2.5.1-2.6/networkx.linalg.graphmatrix.adjacency_matrix#1YY/nx.adjacency_matrix_G_@2.5.1-2.6_L4_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(dtype, 2)'], gt_only=[] |
| 20 | `numpy/numpy.ma.argsort@1.12.1-1.13.0/numpy.ma.argsort#1YY/np.ma.argsort_data_@1.12.1-1.13.0_L5_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(endwith, 4)', '(fill_value, 5)'], gt_only=[] |
| 21 | `numpy/numpy.percentile@1.21.6-1.22.0/numpy.percentile#1YY/np.percentile_a___25__50__75__@1.21.6-1.22.0_L3_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(interpolation, 8)', '(method, 5)'], gt_only=[] |
| 22 | `numpy/numpy.quantile@1.21.6-1.22.0/numpy.quantile#1YY/np.quantile_a__q_@1.21.6-1.22.0_L9_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(method, 5)'], gt_only=[] |
| 23 | `pandas/DataFrame.ewm@1.3.5-1.4.0/DataFrame.ewm#1YY/df.ewm_0.5_@1.3.5-1.4.0_L4_tempLst1.json` | mismatch | item 0 field (times, 8) mismatch: pred={'typeChange': "'str\|np.ndarray\|DataFrame\|Series\|None'"}, gt={'typeChange': 'str\|np.ndarray\|DataFrame\|Series\|None'} |
| 24 | `pandas/DataFrame.reset_index@1.4.4-1.5.0/DataFrame.reset_index#1YY/df.reset_index__@1.4.4-1.5.0_L4_tempLst1.json` | mismatch | item 0 field (level, 0) mismatch: pred={'typeChange': "'IndexLabel'"}, gt={'typeChange': 'IndexLabel'} |
| 25 | `pandas/DataFrame.rolling@1.4.4-1.5.0/DataFrame.rolling#1YY/df.rolling_2_@1.4.4-1.5.0_L4_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(step, 7)'], gt_only=[] |
| 26 | `pandas/DataFrame.to_stata@1.3.5-1.4.0/DataFrame.to_stata#1YY/df.to_stata__animals.dta__@1.3.5-1.4.0_L3_tempLst1.json` | mismatch | item 0 field (path, 0) mismatch: pred={'typeChange': "'FilePath\|WriteBuffer[bytes]'"}, gt={'typeChange': 'FilePath\|WriteBuffer[bytes]'} |
| 27 | `pandas/Series.ewm@1.3.5-1.4.0/Series.ewm#1YY/df.ewm_0.5_@1.3.5-1.4.0_L4_tempLst1.json` | mismatch | item 0 field (times, 8) mismatch: pred={'typeChange': "'str\|np.ndarray\|DataFrame\|Series\|None'"}, gt={'typeChange': 'str\|np.ndarray\|DataFrame\|Series\|None'} |
| 28 | `pandas/Series.rolling@1.4.4-1.5.0/Series.rolling#1YY/df.rolling_2_@1.4.4-1.5.0_L4_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(step, 7)'], gt_only=[] |
| 29 | `pandas/Styler.background_gradient@1.2.5-1.3.0/Styler.background_gradient#1YY/df.style.background_gradient__@1.2.5-1.3.0_L13_tempLst1.json` | mismatch | item 0 field (axis, 3) mismatch: pred={'typeChange': "'Axis\|None'"}, gt={'typeChange': 'Axis\|None'} |
| 30 | `pandas/Styler.format@1.2.5-1.3.0/Styler.format#1YY/df.style.format____.2____@1.2.5-1.3.0_L4_tempLst1.json` | mismatch | item 0 field (formatter, 0) mismatch: pred={'typeChange': "'ExtFormatter\|None'"}, gt={} |
| 31 | `pandas/melt@1.0.5-1.1.0/melt#1YY/pd.melt_df_@1.0.5-1.1.0_L3_tempLst1.json` | mismatch | item 0 field (frame, 0) mismatch: pred={'typeChange': "'DataFrame'"}, gt={'typeChange': 'DataFrame'} |
| 32 | `pandas/read_csv@1.2.5-1.3.0/read_csv#1YY/pd.read_csv__._dev.csv__@1.2.5-1.3.0_L2_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(encoding_errors, 42)', '(on_bad_lines, 46)'], gt_only=[] |
| 33 | `pandas/testing.assert_frame_equal@1.0.5-1.1.0/testing.assert_frame_equal#1YY/assert_frame_equal_df1__df1_@1.0.5-1.1.0_L5_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(obj, 16)'], gt_only=[] |
| 34 | `pandas/testing.assert_series_equal@1.0.5-1.1.0/testing.assert_series_equal#1YY/assert_series_equal_df1__df1_@1.0.5-1.1.0_L5_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(check_freq, 11)'], gt_only=[] |
| 35 | `pandas/testing.assert_series_equal@1.1.5-1.2.0/testing.assert_series_equal#1YY/tm.assert_series_equal_a__b_@1.1.5-1.2.0_L5_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(check_flags, 12)'], gt_only=[] |
| 36 | `plotly/plotly.express.area@4.2.1-4.3.0/plotly.express.area#1YY/px.area__@4.2.1-4.3.0_L3_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(facet_col_wrap, 11)'], gt_only=[] |
| 37 | `plotly/plotly.express.bar@4.14.3-5.0.0/plotly.express.bar#1YY/px.bar__@4.14.3-5.0.0_L3_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(pattern_shape, 4)', '(pattern_shape_map, 27)', '(pattern_shape_sequence, 26)'], gt_only=[] |
| 38 | `plotly/plotly.express.bar@4.2.1-4.3.0/plotly.express.bar#1YY/px.bar__@4.2.1-4.3.0_L3_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(facet_col_wrap, 6)'], gt_only=['(hover_name, 6)'] |
| 39 | `plotly/plotly.express.bar@5.4.0-5.5.0/plotly.express.bar#1YY/px.bar__@5.4.0-5.5.0_L3_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(text_auto, 37)'], gt_only=[] |
| 40 | `plotly/plotly.express.bar_polar@4.14.3-5.0.0/plotly.express.bar_polar#1YY/px.bar_polar__@4.14.3-5.0.0_L3_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(pattern_shape, 4)', '(pattern_shape_map, 17)', '(pattern_shape_sequence, 16)'], gt_only=[] |
| 41 | `plotly/plotly.express.bar_polar@4.3.0-4.4.0/plotly.express.bar_polar#1YY/px.bar_polar__@4.3.0-4.4.0_L3_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(range_theta, 18)'], gt_only=[] |
| 42 | `plotly/plotly.express.box@4.2.1-4.3.0/plotly.express.box#1YY/px.box__@4.2.1-4.3.0_L3_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(facet_col_wrap, 6)'], gt_only=[] |
| 43 | `plotly/plotly.express.density_contour@4.2.1-4.3.0/plotly.express.density_contour#1YY/px.density_contour__@4.2.1-4.3.0_L3_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(facet_col_wrap, 7)'], gt_only=[] |
| 44 | `plotly/plotly.express.density_contour@5.1.0-5.2.1/plotly.express.density_contour#1YY/px.density_contour__@5.1.0-5.2.1_L3_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(trendline_options, 22)', '(trendline_scope, 24)'], gt_only=[] |
| 45 | `plotly/plotly.express.density_heatmap@4.2.1-4.3.0/plotly.express.density_heatmap#1YY/px.density_heatmap__@4.2.1-4.3.0_L3_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(animation_frame, 9)', '(animation_group, 10)', '(category_orders, 11)'], gt_only=['(animation_frame, 8)', '(animation_group, 9)', '(category_orders, 10)'] |
| 46 | `plotly/plotly.express.density_heatmap@5.4.0-5.5.0/plotly.express.density_heatmap#1YY/px.density_heatmap__@5.4.0-5.5.0_L3_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(text_auto, 30)'], gt_only=[] |
| 47 | `plotly/plotly.express.histogram@4.14.3-5.0.0/plotly.express.histogram#1YY/px.histogram__@4.14.3-5.0.0_L3_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(pattern_shape, 4)', '(pattern_shape_map, 19)', '(pattern_shape_sequence, 18)'], gt_only=[] |
| 48 | `plotly/plotly.express.histogram@4.2.1-4.3.0/plotly.express.histogram#1YY/px.histogram__@4.2.1-4.3.0_L3_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(facet_col_wrap, 6)'], gt_only=[] |
| 49 | `plotly/plotly.express.histogram@5.4.0-5.5.0/plotly.express.histogram#1YY/px.histogram__@5.4.0-5.5.0_L3_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(text_auto, 33)'], gt_only=[] |
| 50 | `plotly/plotly.express.imshow@4.13.0-4.14.0/plotly.express.imshow#1YY/px.imshow_img_rgb_@4.13.0-4.14.0_L4_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(animation_frame, 7)', '(facet_col, 8)', '(facet_col_spacing, 10)'], gt_only=[] |
| 51 | `plotly/plotly.express.line@4.2.1-4.3.0/plotly.express.line#1YY/px.line__@4.2.1-4.3.0_L3_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(facet_col_wrap, 12)'], gt_only=['(error_x, 12)'] |
| 52 | `plotly/plotly.express.line@5.1.0-5.2.1/plotly.express.line#1YY/px.line__@5.1.0-5.2.1_L3_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(markers, 31)', '(symbol, 6)', '(symbol_map, 30)'], gt_only=[] |
| 53 | `plotly/plotly.express.line_3d@5.1.0-5.2.1/plotly.express.line_3d#1YY/px.line_3d__@5.1.0-5.2.1_L3_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(markers, 28)', '(symbol, 8)', '(symbol_map, 27)'], gt_only=[] |
| 54 | `plotly/plotly.express.line_geo@5.1.0-5.2.1/plotly.express.line_geo#1YY/px.line_geo__@5.1.0-5.2.1_L3_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(markers, 30)', '(symbol, 19)', '(symbol_map, 29)'], gt_only=[] |
| 55 | `plotly/plotly.express.line_mapbox@4.3.0-4.4.0/plotly.express.line_mapbox#1YY/px.line_mapbox_us_cities___lat____lon__@4.3.0-4.4.0_L5_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(center, 16)', '(mapbox_style, 17)'], gt_only=[] |
| 56 | `plotly/plotly.express.line_polar@4.3.0-4.4.0/plotly.express.line_polar#1YY/px.line_polar__@4.3.0-4.4.0_L3_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(range_theta, 24)'], gt_only=[] |
| 57 | `plotly/plotly.express.line_polar@5.1.0-5.2.1/plotly.express.line_polar#1YY/px.line_polar__@5.1.0-5.2.1_L3_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(markers, 21)', '(symbol, 10)', '(symbol_map, 20)'], gt_only=[] |
| 58 | `plotly/plotly.express.line_ternary@5.1.0-5.2.1/plotly.express.line_ternary#1YY/px.line_ternary__@5.1.0-5.2.1_L3_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(markers, 22)', '(symbol, 7)', '(symbol_map, 21)'], gt_only=[] |
| 59 | `plotly/plotly.express.scatter@4.2.1-4.3.0/plotly.express.scatter#1YY/px.scatter__@4.2.1-4.3.0_L3_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(facet_col_wrap, 12)'], gt_only=['(error_x, 12)'] |
| 60 | `plotly/plotly.express.scatter@5.1.0-5.2.1/plotly.express.scatter#1YY/px.scatter__@5.1.0-5.2.1_L3_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(trendline_options, 36)', '(trendline_scope, 38)'], gt_only=[] |
| 61 | `plotly/plotly.express.scatter_mapbox@4.3.0-4.4.0/plotly.express.scatter_mapbox#1YY/px.scatter_mapbox_df___centroid_lat____centroid_lon__@4.3.0-4.4.0_L3_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(center, 21)', '(mapbox_style, 22)'], gt_only=[] |
| 62 | `plotly/plotly.express.scatter_polar@4.3.0-4.4.0/plotly.express.scatter_polar#1YY/px.scatter_polar__@4.3.0-4.4.0_L3_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(range_theta, 26)'], gt_only=[] |
| 63 | `plotly/plotly.express.strip@4.2.1-4.3.0/plotly.express.strip#1YY/px.strip__@4.2.1-4.3.0_L3_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(facet_col_wrap, 6)'], gt_only=[] |
| 64 | `plotly/plotly.express.sunburst@4.4.1-4.5.0/plotly.express.sunburst#1YY/px.sunburst__@4.4.1-4.5.0_L3_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(path, 4)'], gt_only=[] |
| 65 | `plotly/plotly.express.treemap@4.4.1-4.5.0/plotly.express.treemap#1YY/px.treemap__@4.4.1-4.5.0_L3_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(path, 5)'], gt_only=[] |
| 66 | `plotly/plotly.express.violin@4.2.1-4.3.0/plotly.express.violin#1YY/px.violin__@4.2.1-4.3.0_L3_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(facet_col_wrap, 6)'], gt_only=[] |
| 67 | `plotly/plotly.figure_factory.create_violin@2.0.8-2.0.9/plotly.figure_factory.create_violin#1YY/create_violin_data_list_@2.0.8-2.0.9_L5_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(sort, 7)'], gt_only=[] |
| 68 | `plotly/plotly.tools.FigureFactory.create_distplot@1.10.0-1.11.0/plotly.tools.FigureFactory.create_distplot#1YY/FF.create_distplot_hist_data__group_labels_@1.10.0-1.11.0_L9_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(histnorm, 10)'], gt_only=[] |
| 69 | `polars/polars.repeat@0.17.14-0.17.15/polars.repeat#1YY/pl.repeat__z___3_@0.17.14-0.17.15_L2_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(eager, 4)', '(name, 5)'], gt_only=['(eager, 3)', '(name, 4)'] |
| 70 | `rich/Columns@1.3.0-1.3.1/Columns#1YY/Columns_renderables_@1.3.0-1.3.1_L3_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(width, 2)'], gt_only=[] |
| 71 | `rich/Panel@2.3.1-3.0.0/Panel#1YY/Panel_None_@2.3.1-3.0.0_L2_tempLst1.json` | mismatch | item 0 field (box, 1) mismatch: pred={'typeChange': 'rich.box.Box'}, gt={} |
| 72 | `rich/Panel@3.1.0-3.2.0/Panel#1YY/Panel_renderable_@3.1.0-3.2.0_L6_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(padding, 8)', '(width, 7)'], gt_only=['(padding, 7)', '(width, 6)'] |
| 73 | `rich/install@12.5.1-12.6.0/install#1YY/pretty.install__@12.5.1-12.6.0_L2_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(max_depth, 6)'], gt_only=[] |
| 74 | `rich/rich.syntax.Syntax.from_path@11.0.0-11.1.0/rich.syntax.Syntax.from_path#1YY/Syntax.from_path__._example.py__@11.0.0-11.1.0_L2_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(lexer, 2)'], gt_only=[] |
| 75 | `scipy/scipy.stats.qmc.LatinHypercube@1.9.3-1.10.0/scipy.stats.qmc.LatinHypercube#1YY/qmc.LatinHypercube_d_@1.9.3-1.10.0_L7_tempLst1.json` | mismatch | item 0 field (centered, 2) mismatch: pred={'typeChange': "'bool'"}, gt={} |
| 76 | `scipy/scipy.stats.ttest_ind@1.6.3-1.7.0/scipy.stats.ttest_ind#1YY/stats.ttest_ind_a__b_@1.6.3-1.7.0_L4_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(permutations, 5)'], gt_only=[] |
| 77 | `sklearn/calibration.CalibratedClassifierCV@1.1.3-1.2.0/calibration.CalibratedClassifierCV#1YY/CalibratedClassifierCV__@1.1.3-1.2.0_L6_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(base_estimator, 6)'], gt_only=[] |
| 78 | `sklearn/ensemble.AdaBoostClassifier@1.1.3-1.2.0/ensemble.AdaBoostClassifier#1YY/AdaBoostClassifier__@1.1.3-1.2.0_L4_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(base_estimator, 6)'], gt_only=[] |
| 79 | `sklearn/ensemble.AdaBoostRegressor@1.1.3-1.2.0/ensemble.AdaBoostRegressor#1YY/AdaBoostRegressor__@1.1.3-1.2.0_L4_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(base_estimator, 6)'], gt_only=[] |
| 80 | `sklearn/ensemble.BaggingClassifier@1.1.3-1.2.0/ensemble.BaggingClassifier#1YY/BaggingClassifier__@1.1.3-1.2.0_L5_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(base_estimator, 12)'], gt_only=[] |
| 81 | `sklearn/ensemble.BaggingRegressor@1.1.3-1.2.0/ensemble.BaggingRegressor#1YY/BaggingRegressor__@1.1.3-1.2.0_L5_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(base_estimator, 12)'], gt_only=[] |
| 82 | `sklearn/ensemble.HistGradientBoostingRegressor@0.22.2-0.23.0/ensemble.HistGradientBoostingRegressor#1YY/HistGradientBoostingRegressor__@0.22.2-0.23.0_L5_tempLst1.json` | mismatch | item 0 field (monotonic_cst, 9) mismatch: pred={'addKey': 'monotonic_cst'}, gt={'addKey': 'monotonic_cst=None'} |
| 83 | `sklearn/linear_model.RANSACRegressor@0.17.1-0.18/linear_model.RANSACRegressor#1YY/RANSACRegressor__@0.17.1-0.18_L2_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(loss, 10)'], gt_only=[] |
| 84 | `sklearn/linear_model.RANSACRegressor@1.0.2-1.1.0/linear_model.RANSACRegressor#1YY/RANSACRegressor__@1.0.2-1.1.0_L5_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(estimator, 0)'], gt_only=[] |
| 85 | `sklearn/sklearn.cluster.SpectralClustering@0.21.3-0.22/sklearn.cluster.SpectralClustering#1YY/SpectralClustering_5_@0.21.3-0.22_L4_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(n_components, 2)'], gt_only=[] |
| 86 | `sklearn/sklearn.discriminant_analysis.QuadraticDiscriminantAnalysis@0.18.1-0.19.0/sklearn.discriminant_analysis.QuadraticDiscriminantAnalysis#1YY/QuadraticDiscriminantAnalysis__@0.18.1-0.19.0_L5_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(store_covariances, 4)'], gt_only=[] |
| 87 | `sklearn/sklearn.linear_model.BayesianRidge@0.21.3-0.22/sklearn.linear_model.BayesianRidge#1YY/linear_model.BayesianRidge__@0.21.3-0.22_L2_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(alpha_init, 6)', '(lambda_init, 7)'], gt_only=[] |
| 88 | `sklearn/sklearn.linear_model.PassiveAggressiveClassifier@0.18.1-0.19.0/sklearn.linear_model.PassiveAggressiveClassifier#1YY/PassiveAggressiveClassifier__@0.18.1-0.19.0_L2_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(max_iter, 2)', '(tol, 3)'], gt_only=[] |
| 89 | `sklearn/sklearn.svm.NuSVC@0.21.3-0.22/sklearn.svm.NuSVC#1YY/NuSVC__@0.21.3-0.22_L5_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(break_ties, 13)'], gt_only=[] |
| 90 | `sklearn/sklearn.svm.SVC@0.21.3-0.22/sklearn.svm.SVC#1YY/SVC__@0.21.3-0.22_L5_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(break_ties, 13)'], gt_only=[] |
| 91 | `sympy/sympy.physics.mechanics.PinJoint@1.11.1-1.12/sympy.physics.mechanics.PinJoint#1YY/PinJoint__PC___parent__child_@1.11.1-1.12_L4_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(child_joint_pos, 13)', '(parent_joint_pos, 12)'], gt_only=[] |
| 92 | `sympy/sympy.physics.mechanics.PrismaticJoint@1.11.1-1.12/sympy.physics.mechanics.PrismaticJoint#1YY/PrismaticJoint__PC___parent__child_@1.11.1-1.12_L4_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(child_joint_pos, 13)', '(parent_joint_pos, 12)'], gt_only=[] |
| 93 | `tensorflow/tf.data.Dataset.random@2.11.1-2.12.0/tf.data.Dataset.random#1YY/tf.data.Dataset.random__@2.11.1-2.12.0_L2_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(rerandomize_each_iteration, 1)'], gt_only=[] |
| 94 | `tensorflow/tf.keras.losses.SparseCategoricalCrossentropy@2.9.3-2.10.0/tf.keras.losses.SparseCategoricalCrossentropy#1YY/tf.keras.losses.SparseCategoricalCrossentropy__@2.9.3-2.10.0_L2_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(ignore_class, 1)'], gt_only=[] |
| 95 | `tensorflow/tf.string_split@1.13.2-1.14.0/tf.string_split#1YY/tf.string_split_string_tensor_@1.13.2-1.14.0_L4_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(delimiter, 3)'], gt_only=[] |
| 96 | `tornado/tornado.httpclient.HTTPRequest@3.0.2-3.1/tornado.httpclient.HTTPRequest#1YY/tornado.httpclient.HTTPRequest__http___httpbin.org_get__@3.0.2-3.1_L2_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(auth_mode, 6)', '(connect_timeout, 7)', '(if_modified_since, 6)'], gt_only=['(connect_timeout, 6)', '(if_modified_since, 8)', '(request_timeout, 7)'] |
