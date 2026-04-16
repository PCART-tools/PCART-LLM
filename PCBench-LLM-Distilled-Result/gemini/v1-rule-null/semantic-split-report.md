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
| 语义相关 | 171 | 132 | 39 | 77.19% |
| 语义不相关 | 113 | 27 | 86 | 23.89% |
| 合并后 | 284 | 159 | 125 | 55.99% |

## 语义相关

| 指标 | 数值 |
| --- | ---: |
| 样例数 | 171 |
| 正确 | 132 |
| 错误 | 39 |
| 正确率 | 77.19% |

### 错误样例

| 序号 | 样例路径 | 错误类型 | 差异说明 |
| --- | --- | --- | --- |
| 1 | `fastapi/fastapi.encoders.jsonable_encoder@0.60.2-0.61.0/fastapi.encoders.jsonable_encoder#1YY/jsonable_encoder_item_@0.60.2-0.61.0_L14_tempLst1.json` | mismatch | item 0 field (skip_defaults, 4) mismatch: pred={'delete': 1, 'replace': 'exclude_unset'}, gt={'delete': 1} |
| 2 | `networkx/average_neighbor_degree@1.5-1.6/average_neighbor_degree#1YY/nx.average_neighbor_degree_G_@1.5-1.6_L4_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(source, 1)', '(target, 2)'], gt_only=['(weight, 4)'] |
| 3 | `networkx/clustering@1.5-1.6/clustering#1YY/nx.clustering_G_@1.5-1.6_L4_tempLst1.json` | mismatch | item 0 field (weighted, 2) mismatch: pred={'rename': 'weight'}, gt={'delete': 1, 'replace': 'weight=None'} |
| 4 | `networkx/degree@1.5-1.6/degree#1YY/G.degree__@1.5-1.6_L4_tempLst1.json` | mismatch | item 0 field (weighted, 1) mismatch: pred={'rename': 'weight'}, gt={'delete': 1, 'replace': 'weight=None'} |
| 5 | `networkx/edge_betweenness_centrality_subset@1.4-1.5/edge_betweenness_centrality_subset#1YY/nx.edge_betweenness_centrality_subset_G__sources__targets_@1.4-1.5_L6_tempLst1.json` | mismatch | item 0 field (weighted_edges, 4) mismatch: pred={'delete': 1, 'replace': 'weight=None'}, gt={'rename': 'weight'} |
| 6 | `networkx/geographical_threshold_graph@2.0-2.1/geographical_threshold_graph#1YY/nx.geographical_threshold_graph_10__0.1_@2.0-2.1_L2_tempLst1.json` | mismatch | item 0 field (alpha, 2) mismatch: pred={'delete': 1, 'replace': 'p_dist=None'}, gt={'delete': 1} |
| 7 | `networkx/networkx.to_pandas_edgelist@2.8.8-3.0/networkx.to_pandas_edgelist#1YY/nx.to_pandas_edgelist_G_@2.8.8-3.0_L7_tempLst1.json` | mismatch | item 0 field (edge_key, 6) mismatch: pred={'delete': 1}, gt={'posChange': 5} |
| 8 | `networkx/spectral_layout@1.5-1.6/spectral_layout#1YY/nx.spectral_layout_G_@1.5-1.6_L4_tempLst1.json` | mismatch | item 0 field (weighted, 2) mismatch: pred={'rename': 'weight'}, gt={'delete': 1, 'replace': "weight='weight'"} |
| 9 | `numpy/numpy.genfromtxt@1.9.3-1.10.0/numpy.genfromtxt#1YY/np.genfromtxt_f_@1.9.3-1.10.0_L4_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(max_rows, 21)'], gt_only=[] |
| 10 | `numpy/numpy.histogramdd@1.23.5-1.24.0/numpy.histogramdd#1YY/np.histogramdd_sample_@1.23.5-1.24.0_L3_tempLst1.json` | mismatch | item 0 field (normed, 3) mismatch: pred={'delete': 1, 'replace': 'density=None'}, gt={'delete': 1} |
| 11 | `pandas/DataFrame.between_time@1.5.3-2.0.0/DataFrame.between_time#1YY/ts.between_time__0_15____0_45__@1.5.3-2.0.0_L4_tempLst1.json` | mismatch | item 0 field (axis, 5) mismatch: pred={'typeChange': "'Axis\|None'", 'posChange': 3}, gt={'posChange': 3} |
| 12 | `pandas/DataFrame.groupby@1.5.3-2.0.0/DataFrame.groupby#1YY/df.groupby___Animal___@1.5.3-2.0.0_L3_tempLst1.json` | mismatch | item 0 field (group_keys, 5) mismatch: pred={'typeChange': "'bool'"}, gt={'typeChange': 'bool'} |
| 13 | `pandas/DataFrame.set_axis@1.5.3-2.0.0/DataFrame.set_axis#1YY/df.set_axis___a____b____c___@1.5.3-2.0.0_L3_tempLst1.json` | mismatch | item 0 field (copy, 4) mismatch: pred={'typeChange': "'bool\|None'"}, gt={'typeChange': 'bool\|None'} |
| 14 | `pandas/DataFrame.take@1.5.3-2.0.0/DataFrame.take#1YY/df.take__0__3__@1.5.3-2.0.0_L4_tempLst1.json` | mismatch | item 0 field (axis, 1) mismatch: pred={'typeChange': "'Axis'"}, gt={} |
| 15 | `pandas/DataFrame.to_latex@1.5.3-2.0.0/DataFrame.to_latex#1YY/df.to_latex__@1.5.3-2.0.0_L3_tempLst1.json` | mismatch | item 0 field (col_space, 2) mismatch: pred={'delete': 1, 'replace': 'header'}, gt={'delete': 1} |
| 16 | `pandas/Series.groupby@1.5.3-2.0.0/Series.groupby#1YY/ser.groupby___a____b____a____b___@1.5.3-2.0.0_L3_tempLst1.json` | mismatch | item 0 field (group_keys, 5) mismatch: pred={'typeChange': "'bool'"}, gt={'typeChange': 'bool'} |
| 17 | `pandas/Series.set_axis@1.5.3-2.0.0/Series.set_axis#1YY/s.set_axis___a____b____c___@1.5.3-2.0.0_L3_tempLst1.json` | mismatch | item 0 field (copy, 4) mismatch: pred={'typeChange': "'bool\|None'"}, gt={'typeChange': 'bool\|None'} |
| 18 | `pandas/Timestamp.fromordinal@1.5.3-2.0.0/Timestamp.fromordinal#1YY/pd.Timestamp.fromordinal_737425_@1.5.3-2.0.0_L2_tempLst1.json` | mismatch | item 0 field (freq, 1) mismatch: pred={'delete': 1, 'replace': 'tz=None'}, gt={'delete': 1} |
| 19 | `pandas/bdate_range@1.5.3-2.0.0/bdate_range#1YY/pd.bdate_range__1_1_2018____1_08_2018__@1.5.3-2.0.0_L2_tempLst1.json` | mismatch | item 0 field (freq, 3) mismatch: pred={'typeChange': "'Frequency'"}, gt={} |
| 20 | `pandas/date_range@1.5.3-2.0.0/date_range#1YY/pd.date_range__1_1_2018____1_08_2018__@1.5.3-2.0.0_L2_tempLst1.json` | mismatch | item 0 field (inclusive, 8) mismatch: pred={'typeChange': "'IntervalClosedType'", 'posChange': 7}, gt={'typeChange': 'IntervalClosedType', 'posChange': 7} |
| 21 | `pandas/pandas.DataFrame.resample@1.5.3-2.0.0/pandas.DataFrame.resample#1YY/DataFrame.resample__3T__@1.5.3-2.0.0_L4_tempLst1.json` | mismatch | item 0 field (group_keys, 12) mismatch: pred={'typeChange': "'bool'", 'posChange': 10}, gt={'typeChange': 'bool', 'posChange': 10} |
| 22 | `pandas/pandas.Series.resample@1.5.3-2.0.0/pandas.Series.resample#1YY/series.resample__3T__@1.5.3-2.0.0_L4_tempLst1.json` | mismatch | item 0 field (group_keys, 12) mismatch: pred={'typeChange': "'bool'", 'posChange': 10}, gt={'typeChange': 'bool', 'posChange': 10} |
| 23 | `pandas/read_csv@1.5.3-2.0.0/read_csv#1YY/pd.read_csv__._dev.csv__@1.5.3-2.0.0_L2_tempLst1.json` | mismatch | item 0 field (infer_datetime_format, 26) mismatch: pred={'typeChange': "'bool\|lib.NoDefault'"}, gt={} |
| 24 | `pandas/testing.assert_extension_array_equal@1.5.3-2.0.0/testing.assert_extension_array_equal#1YY/tm.assert_extension_array_equal_b__c_@1.5.3-2.0.0_L5_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(obj, 7)'], gt_only=[] |
| 25 | `pandas/testing.assert_frame_equal@1.5.3-2.0.0/testing.assert_frame_equal#1YY/assert_frame_equal_df1__df1_@1.5.3-2.0.0_L5_tempLst1.json` | mismatch | item 0 field (atol, 16) mismatch: pred={'typeChange': "'float'", 'posChange': 15}, gt={'posChange': 15} |
| 26 | `pandas/testing.assert_series_equal@1.5.3-2.0.0/testing.assert_series_equal#1YY/tm.assert_series_equal_a__b_@1.5.3-2.0.0_L5_tempLst1.json` | mismatch | item 0 field (atol, 14) mismatch: pred={'typeChange': "'float'", 'posChange': 13}, gt={'posChange': 13} |
| 27 | `plotly/plotly.figure_factory.create_choropleth@2.4.1-2.5.0/plotly.figure_factory.create_choropleth#1YY/ff.create_choropleth_fips__values_@2.4.1-2.5.0_L11_tempLst1.json` | mismatch | item 0 field (offline_mode, 9) mismatch: pred={'delete': 1, 'replace': 'show_hover=True'}, gt={'delete': 1} |
| 28 | `polars/polars.expr.str.strptime@0.17.15-0.18.0/polars.expr.str.strptime#1YY/a.str.strptime_pl.Date_@0.17.15-0.18.0_L4_tempLst1.json` | mismatch | item 0 field (utc, 6) mismatch: pred={'typeChange': 'bool\|None'}, gt={} |
| 29 | `rich/rich.syntax.Syntax@10.16.2-11.0.0/rich.syntax.Syntax#1YY/Syntax__print__hello_world______python__@10.16.2-11.0.0_L2_tempLst1.json` | mismatch | item 0 field (lexer_name, 1) mismatch: pred={'typeChange': 'Union[pygments.lexer.Lexer,str]', 'rename': 'lexer'}, gt={'rename': 'lexer'} |
| 30 | `scipy/scipy.optimize.fmin_cobyla@0.19.1-1.0.0/scipy.optimize.fmin_cobyla#1YY/fmin_cobyla_objective__x0__constraints_@0.19.1-1.0.0_L13_tempLst1.json` | mismatch | item 0 field (iprint, 7) mismatch: pred={'delete': 1, 'replace': 'maxfun=1000'}, gt={'delete': 1} |
| 31 | `scipy/scipy.stats.rv_discrete.expect@0.16.1-0.17.0/scipy.stats.rv_discrete.expect#1YY/custom_distribution.expect__@0.16.1-0.17.0_L6_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(maxcount, 6)'], gt_only=[] |
| 32 | `sklearn/linear_model.lasso_path@0.15.2-0.16.0/linear_model.lasso_path#1YY/lasso_path_X__y_@0.15.2-0.16.0_L5_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(positive, 11)'], gt_only=[] |
| 33 | `sklearn/sklearn.feature_selection.RFECV@0.17.1-0.18/sklearn.feature_selection.RFECV#1YY/RFECV_estimator_@0.17.1-0.18_L6_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(n_jobs, 5)'], gt_only=[] |
| 34 | `sympy/sympy.physics.units.quantities.Quantity@1.11.1-1.12/sympy.physics.units.quantities.Quantity#1YY/Quantity__velocity__@1.11.1-1.12_L2_tempLst1.json` | mismatch | item 0 field (dimension, 2) mismatch: pred={'delete': 1, 'replace': 'latex_repr=None'}, gt={'delete': 1} |
| 35 | `tensorflow/tf.contrib.data.make_csv_dataset@1.10.1-1.11.0/tf.contrib.data.make_csv_dataset#1NN/tf.contrib.data.make_csv_dataset__._dev.csv___1__None__None__None__None_______True______True__None__True__10000__None__1__1__2__False__1_@1.10.1-1.11.0_L2_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(compression_type, 18)'], gt_only=[] |
| 36 | `tensorflow/tf.contrib.data.make_csv_dataset@1.8.0-1.9.0/tf.contrib.data.make_csv_dataset#1NN/tf.contrib.data.make_csv_dataset__._dev.csv___1__None__None__None_______True______True__None__None__True__1__None__1__1__2__False__tf.float32__1_@1.8.0-1.9.0_L2_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(select_columns, 5)'], gt_only=[] |
| 37 | `torch/torch.btrifact@1.0.1-1.1.0/torch.btrifact#1YY/torch.btrifact_A_@1.0.1-1.1.0_L3_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(out, 2)'], gt_only=[] |
| 38 | `tornado/tornado.httpclient.AsyncHTTPClient.fetch@5.1.1-6.0/tornado.httpclient.AsyncHTTPClient.fetch#1YY/http_client.fetch__http___example.com__@5.1.1-6.0_L6_tempLst1.json` | mismatch | item 0 field (callback, 1) mismatch: pred={'delete': 1, 'replace': 'raise_error=True'}, gt={'delete': 1} |
| 39 | `tornado/tornado.iostream.BaseIOStream.read_bytes@5.1.1-6.0/tornado.iostream.BaseIOStream.read_bytes#1YY/stream.read_bytes_10_@5.1.1-6.0_L11_tempLst1.json` | mismatch | item 0 field (callback, 1) mismatch: pred={'delete': 1, 'replace': 'partial=False'}, gt={'delete': 1} |

## 语义不相关

| 指标 | 数值 |
| --- | ---: |
| 样例数 | 113 |
| 正确 | 27 |
| 错误 | 86 |
| 正确率 | 23.89% |

### 错误样例

| 序号 | 样例路径 | 错误类型 | 差异说明 |
| --- | --- | --- | --- |
| 1 | `click/click.Command@7.0-7.1/click.Command#1YY/click.Command__my_command__@7.0-7.1_L2_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(no_args_is_help, 9)'], gt_only=[] |
| 2 | `dask/dask.dataframe.drop_duplicates@2.4.0-2.5.0/dask.dataframe.drop_duplicates#1YY/ddf.drop_duplicates__@2.4.0-2.5.0_L5_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(subset, 0)'], gt_only=[] |
| 3 | `dask/dask.dataframe.utils.assert_eq@2022.5.2-2022.6.0/dask.dataframe.utils.assert_eq#1YY/assert_eq_ddf_result__pdf_result_@2022.5.2-2022.6.0_L8_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(sort_results, 6)'], gt_only=[] |
| 4 | `flask/from_file@2.2.5-2.3.0/from_file#1YY/app.config.from_file__._test.json___json.load_@2.2.5-2.3.0_L4_tempLst1.json` | mismatch | item 0 field (filename, 0) mismatch: pred={'typeChange': "'str'"}, gt={} |
| 5 | `gensim/gensim.models.base_any2vec.BaseWordEmbeddingsModel@3.4.0-3.5.0/gensim.models.base_any2vec.BaseWordEmbeddingsModel#1YY/BaseWordEmbeddingsModel__@3.4.0-3.5.0_L2_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(ns_exponent, 13)'], gt_only=[] |
| 6 | `gensim/gensim.models.coherencemodel.CoherenceModel@0.13.1-0.13.2/gensim.models.coherencemodel.CoherenceModel#1NN/CoherenceModel_lda_model__documents_@0.13.1-0.13.2_L8_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(topics, 1)'], gt_only=[] |
| 7 | `gensim/gensim.models.doc2vec.Doc2Vec@3.5.0-3.6.0/gensim.models.doc2vec.Doc2Vec#1YY/Doc2Vec__@3.5.0-3.6.0_L3_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(corpus_file, 1)'], gt_only=[] |
| 8 | `gensim/gensim.models.word2vec.Word2Vec.intersect_word2vec_format@0.13.1-0.13.2/gensim.models.word2vec.Word2Vec.intersect_word2vec_format#1YY/model.intersect_word2vec_format_fname_@0.13.1-0.13.2_L7_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(lockf, 1)'], gt_only=[] |
| 9 | `gensim/gensim.models.word2vec.Word2Vec.train@1.0.1-2.0.0/gensim.models.word2vec.Word2Vec.train#1NN/model.train_sentences_@1.0.1-2.0.0_L5_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(end_alpha, 5)', '(epochs, 3)', '(start_alpha, 4)'], gt_only=[] |
| 10 | `keras/Conv2DTranspose@2.2.2-2.2.3/Conv2DTranspose#1YY/Conv2DTranspose_64___3__3__@2.2.2-2.2.3_L4_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(dilation_rate, 6)'], gt_only=[] |
| 11 | `keras/DepthwiseConv2D@2.2.4-2.2.5/DepthwiseConv2D#1YY/DepthwiseConv2D__3__3__@2.2.4-2.2.5_L4_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(dilation_rate, 5)'], gt_only=[] |
| 12 | `keras/keras.preprocessing.image.ImageDataGenerator@2.1.4-2.1.5/keras.preprocessing.image.ImageDataGenerator#1YY/ImageDataGenerator__@2.1.4-2.1.5_L2_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(brightness_range, 9)'], gt_only=[] |
| 13 | `matplotlib/matplotlib.gridspec.GridSpec@2.1.2-2.2.0/matplotlib.gridspec.GridSpec#1YY/gridspec.GridSpec_2__2_@2.1.2-2.2.0_L3_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(figure, 2)'], gt_only=[] |
| 14 | `networkx/betweenness_centrality@1.5-1.6/betweenness_centrality#1YY/nx.betweenness_centrality_G_@1.5-1.6_L4_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(k, 1)'], gt_only=[] |
| 15 | `networkx/networkx.linalg.graphmatrix.adjacency_matrix@2.5.1-2.6/networkx.linalg.graphmatrix.adjacency_matrix#1YY/nx.adjacency_matrix_G_@2.5.1-2.6_L4_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(dtype, 2)'], gt_only=[] |
| 16 | `numpy/numpy.ma.argsort@1.12.1-1.13.0/numpy.ma.argsort#1YY/np.ma.argsort_data_@1.12.1-1.13.0_L5_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(endwith, 4)'], gt_only=[] |
| 17 | `numpy/numpy.percentile@1.21.6-1.22.0/numpy.percentile#1YY/np.percentile_a___25__50__75__@1.21.6-1.22.0_L3_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(method, 5)'], gt_only=[] |
| 18 | `numpy/numpy.quantile@1.21.6-1.22.0/numpy.quantile#1YY/np.quantile_a__q_@1.21.6-1.22.0_L9_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(method, 5)'], gt_only=[] |
| 19 | `pandas/DataFrame.ewm@1.3.5-1.4.0/DataFrame.ewm#1YY/df.ewm_0.5_@1.3.5-1.4.0_L4_tempLst1.json` | mismatch | item 0 field (times, 8) mismatch: pred={'typeChange': "'str\|np.ndarray\|DataFrame\|Series\|None'"}, gt={'typeChange': 'str\|np.ndarray\|DataFrame\|Series\|None'} |
| 20 | `pandas/DataFrame.reset_index@1.4.4-1.5.0/DataFrame.reset_index#1YY/df.reset_index__@1.4.4-1.5.0_L4_tempLst1.json` | mismatch | item 0 field (level, 0) mismatch: pred={'typeChange': "'IndexLabel'"}, gt={'typeChange': 'IndexLabel'} |
| 21 | `pandas/DataFrame.rolling@1.4.4-1.5.0/DataFrame.rolling#1YY/df.rolling_2_@1.4.4-1.5.0_L4_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(step, 7)'], gt_only=[] |
| 22 | `pandas/DataFrame.to_stata@1.3.5-1.4.0/DataFrame.to_stata#1YY/df.to_stata__animals.dta__@1.3.5-1.4.0_L3_tempLst1.json` | mismatch | item 0 field (path, 0) mismatch: pred={'typeChange': "'FilePath\|WriteBuffer[bytes]'"}, gt={'typeChange': 'FilePath\|WriteBuffer[bytes]'} |
| 23 | `pandas/Series.ewm@1.3.5-1.4.0/Series.ewm#1YY/df.ewm_0.5_@1.3.5-1.4.0_L4_tempLst1.json` | mismatch | item 0 field (times, 8) mismatch: pred={'typeChange': "'str\|np.ndarray\|DataFrame\|Series\|None'"}, gt={'typeChange': 'str\|np.ndarray\|DataFrame\|Series\|None'} |
| 24 | `pandas/Series.rolling@1.4.4-1.5.0/Series.rolling#1YY/df.rolling_2_@1.4.4-1.5.0_L4_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(step, 7)'], gt_only=[] |
| 25 | `pandas/Styler.background_gradient@1.2.5-1.3.0/Styler.background_gradient#1YY/df.style.background_gradient__@1.2.5-1.3.0_L13_tempLst1.json` | mismatch | item 0 field (axis, 3) mismatch: pred={'typeChange': "'Axis\|None'"}, gt={'typeChange': 'Axis\|None'} |
| 26 | `pandas/Styler.format@1.2.5-1.3.0/Styler.format#1YY/df.style.format____.2____@1.2.5-1.3.0_L4_tempLst1.json` | mismatch | item 0 field (formatter, 0) mismatch: pred={'typeChange': "'ExtFormatter\|None'"}, gt={} |
| 27 | `pandas/melt@1.0.5-1.1.0/melt#1YY/pd.melt_df_@1.0.5-1.1.0_L3_tempLst1.json` | mismatch | item 0 field (frame, 0) mismatch: pred={'typeChange': "'DataFrame'"}, gt={'typeChange': 'DataFrame'} |
| 28 | `pandas/read_csv@1.2.5-1.3.0/read_csv#1YY/pd.read_csv__._dev.csv__@1.2.5-1.3.0_L2_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(encoding_errors, 42)', '(on_bad_lines, 46)'], gt_only=[] |
| 29 | `pandas/testing.assert_frame_equal@1.0.5-1.1.0/testing.assert_frame_equal#1YY/assert_frame_equal_df1__df1_@1.0.5-1.1.0_L5_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(check_freq, 13)'], gt_only=[] |
| 30 | `pandas/testing.assert_series_equal@1.0.5-1.1.0/testing.assert_series_equal#1YY/assert_series_equal_df1__df1_@1.0.5-1.1.0_L5_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(check_freq, 11)'], gt_only=[] |
| 31 | `pandas/testing.assert_series_equal@1.1.5-1.2.0/testing.assert_series_equal#1YY/tm.assert_series_equal_a__b_@1.1.5-1.2.0_L5_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(check_flags, 12)'], gt_only=[] |
| 32 | `plotly/plotly.express.area@4.2.1-4.3.0/plotly.express.area#1YY/px.area__@4.2.1-4.3.0_L3_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(facet_col_wrap, 11)'], gt_only=[] |
| 33 | `plotly/plotly.express.bar@4.14.3-5.0.0/plotly.express.bar#1YY/px.bar__@4.14.3-5.0.0_L3_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(pattern_shape, 4)', '(pattern_shape_map, 27)', '(pattern_shape_sequence, 26)'], gt_only=[] |
| 34 | `plotly/plotly.express.bar@4.2.1-4.3.0/plotly.express.bar#1YY/px.bar__@4.2.1-4.3.0_L3_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(facet_col_wrap, 6)'], gt_only=[] |
| 35 | `plotly/plotly.express.bar@5.4.0-5.5.0/plotly.express.bar#1YY/px.bar__@5.4.0-5.5.0_L3_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(text_auto, 37)'], gt_only=[] |
| 36 | `plotly/plotly.express.bar_polar@4.14.3-5.0.0/plotly.express.bar_polar#1YY/px.bar_polar__@4.14.3-5.0.0_L3_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(pattern_shape, 4)', '(pattern_shape_map, 17)', '(pattern_shape_sequence, 16)'], gt_only=[] |
| 37 | `plotly/plotly.express.bar_polar@4.3.0-4.4.0/plotly.express.bar_polar#1YY/px.bar_polar__@4.3.0-4.4.0_L3_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(range_theta, 18)'], gt_only=[] |
| 38 | `plotly/plotly.express.box@4.2.1-4.3.0/plotly.express.box#1YY/px.box__@4.2.1-4.3.0_L3_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(facet_col_wrap, 6)'], gt_only=[] |
| 39 | `plotly/plotly.express.density_contour@4.2.1-4.3.0/plotly.express.density_contour#1YY/px.density_contour__@4.2.1-4.3.0_L3_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(facet_col_wrap, 7)'], gt_only=[] |
| 40 | `plotly/plotly.express.density_contour@5.1.0-5.2.1/plotly.express.density_contour#1YY/px.density_contour__@5.1.0-5.2.1_L3_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(trendline_options, 22)', '(trendline_scope, 24)'], gt_only=[] |
| 41 | `plotly/plotly.express.density_heatmap@4.2.1-4.3.0/plotly.express.density_heatmap#1YY/px.density_heatmap__@4.2.1-4.3.0_L3_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(facet_col_wrap, 6)'], gt_only=[] |
| 42 | `plotly/plotly.express.density_heatmap@5.4.0-5.5.0/plotly.express.density_heatmap#1YY/px.density_heatmap__@5.4.0-5.5.0_L3_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(text_auto, 30)'], gt_only=[] |
| 43 | `plotly/plotly.express.histogram@4.14.3-5.0.0/plotly.express.histogram#1YY/px.histogram__@4.14.3-5.0.0_L3_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(pattern_shape, 4)', '(pattern_shape_map, 19)', '(pattern_shape_sequence, 18)'], gt_only=[] |
| 44 | `plotly/plotly.express.histogram@4.2.1-4.3.0/plotly.express.histogram#1YY/px.histogram__@4.2.1-4.3.0_L3_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(facet_col_wrap, 6)'], gt_only=[] |
| 45 | `plotly/plotly.express.histogram@5.4.0-5.5.0/plotly.express.histogram#1YY/px.histogram__@5.4.0-5.5.0_L3_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(text_auto, 33)'], gt_only=[] |
| 46 | `plotly/plotly.express.imshow@4.13.0-4.14.0/plotly.express.imshow#1YY/px.imshow_img_rgb_@4.13.0-4.14.0_L4_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(animation_frame, 7)', '(facet_col, 8)', '(facet_col_spacing, 10)'], gt_only=[] |
| 47 | `plotly/plotly.express.line@4.2.1-4.3.0/plotly.express.line#1YY/px.line__@4.2.1-4.3.0_L3_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(facet_col_wrap, 12)'], gt_only=[] |
| 48 | `plotly/plotly.express.line@5.1.0-5.2.1/plotly.express.line#1YY/px.line__@5.1.0-5.2.1_L3_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(markers, 31)', '(symbol, 6)', '(symbol_map, 30)'], gt_only=[] |
| 49 | `plotly/plotly.express.line_3d@5.1.0-5.2.1/plotly.express.line_3d#1YY/px.line_3d__@5.1.0-5.2.1_L3_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(markers, 28)', '(symbol, 8)', '(symbol_map, 27)'], gt_only=[] |
| 50 | `plotly/plotly.express.line_geo@5.1.0-5.2.1/plotly.express.line_geo#1YY/px.line_geo__@5.1.0-5.2.1_L3_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(markers, 30)', '(symbol, 19)', '(symbol_map, 29)'], gt_only=[] |
| 51 | `plotly/plotly.express.line_mapbox@4.3.0-4.4.0/plotly.express.line_mapbox#1YY/px.line_mapbox_us_cities___lat____lon__@4.3.0-4.4.0_L5_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(center, 16)', '(mapbox_style, 17)'], gt_only=[] |
| 52 | `plotly/plotly.express.line_polar@4.3.0-4.4.0/plotly.express.line_polar#1YY/px.line_polar__@4.3.0-4.4.0_L3_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(range_theta, 24)'], gt_only=[] |
| 53 | `plotly/plotly.express.line_polar@5.1.0-5.2.1/plotly.express.line_polar#1YY/px.line_polar__@5.1.0-5.2.1_L3_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(markers, 21)', '(symbol, 10)', '(symbol_map, 20)'], gt_only=[] |
| 54 | `plotly/plotly.express.line_ternary@5.1.0-5.2.1/plotly.express.line_ternary#1YY/px.line_ternary__@5.1.0-5.2.1_L3_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(markers, 22)', '(symbol, 7)', '(symbol_map, 21)'], gt_only=[] |
| 55 | `plotly/plotly.express.scatter@4.2.1-4.3.0/plotly.express.scatter#1YY/px.scatter__@4.2.1-4.3.0_L3_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(facet_col_wrap, 12)'], gt_only=[] |
| 56 | `plotly/plotly.express.scatter@5.1.0-5.2.1/plotly.express.scatter#1YY/px.scatter__@5.1.0-5.2.1_L3_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(trendline_options, 36)', '(trendline_scope, 38)'], gt_only=[] |
| 57 | `plotly/plotly.express.scatter_mapbox@4.3.0-4.4.0/plotly.express.scatter_mapbox#1YY/px.scatter_mapbox_df___centroid_lat____centroid_lon__@4.3.0-4.4.0_L3_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(center, 21)', '(mapbox_style, 22)'], gt_only=[] |
| 58 | `plotly/plotly.express.scatter_polar@4.3.0-4.4.0/plotly.express.scatter_polar#1YY/px.scatter_polar__@4.3.0-4.4.0_L3_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(range_theta, 26)'], gt_only=[] |
| 59 | `plotly/plotly.express.strip@4.2.1-4.3.0/plotly.express.strip#1YY/px.strip__@4.2.1-4.3.0_L3_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(facet_col_wrap, 6)'], gt_only=[] |
| 60 | `plotly/plotly.express.sunburst@4.4.1-4.5.0/plotly.express.sunburst#1YY/px.sunburst__@4.4.1-4.5.0_L3_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(path, 4)'], gt_only=[] |
| 61 | `plotly/plotly.express.treemap@4.4.1-4.5.0/plotly.express.treemap#1YY/px.treemap__@4.4.1-4.5.0_L3_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(path, 5)'], gt_only=[] |
| 62 | `plotly/plotly.express.violin@4.2.1-4.3.0/plotly.express.violin#1YY/px.violin__@4.2.1-4.3.0_L3_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(facet_col_wrap, 6)'], gt_only=[] |
| 63 | `plotly/plotly.figure_factory.create_violin@2.0.8-2.0.9/plotly.figure_factory.create_violin#1YY/create_violin_data_list_@2.0.8-2.0.9_L5_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(sort, 7)'], gt_only=[] |
| 64 | `plotly/plotly.tools.FigureFactory.create_distplot@1.10.0-1.11.0/plotly.tools.FigureFactory.create_distplot#1YY/FF.create_distplot_hist_data__group_labels_@1.10.0-1.11.0_L9_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(histnorm, 6)'], gt_only=[] |
| 65 | `polars/polars.repeat@0.17.14-0.17.15/polars.repeat#1YY/pl.repeat__z___3_@0.17.14-0.17.15_L2_tempLst1.json` | mismatch | item 0 field (value, 0) mismatch: pred={'typeChange': "'PythonLiteral\|None'"}, gt={'typeChange': 'PythonLiteral\|None'} |
| 66 | `rich/Columns@1.3.0-1.3.1/Columns#1YY/Columns_renderables_@1.3.0-1.3.1_L3_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(width, 2)'], gt_only=[] |
| 67 | `rich/install@12.5.1-12.6.0/install#1YY/pretty.install__@12.5.1-12.6.0_L2_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(max_depth, 6)'], gt_only=[] |
| 68 | `rich/rich.syntax.Syntax.from_path@11.0.0-11.1.0/rich.syntax.Syntax.from_path#1YY/Syntax.from_path__._example.py__@11.0.0-11.1.0_L2_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(lexer, 2)'], gt_only=[] |
| 69 | `scipy/scipy.stats.ttest_ind@1.6.3-1.7.0/scipy.stats.ttest_ind#1YY/stats.ttest_ind_a__b_@1.6.3-1.7.0_L4_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(permutations, 5)'], gt_only=[] |
| 70 | `sklearn/calibration.CalibratedClassifierCV@1.1.3-1.2.0/calibration.CalibratedClassifierCV#1YY/CalibratedClassifierCV__@1.1.3-1.2.0_L6_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(estimator, 0)'], gt_only=[] |
| 71 | `sklearn/ensemble.AdaBoostClassifier@1.1.3-1.2.0/ensemble.AdaBoostClassifier#1YY/AdaBoostClassifier__@1.1.3-1.2.0_L4_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(base_estimator, 6)'], gt_only=[] |
| 72 | `sklearn/ensemble.AdaBoostRegressor@1.1.3-1.2.0/ensemble.AdaBoostRegressor#1YY/AdaBoostRegressor__@1.1.3-1.2.0_L4_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(estimator, 0)'], gt_only=[] |
| 73 | `sklearn/ensemble.BaggingClassifier@1.1.3-1.2.0/ensemble.BaggingClassifier#1YY/BaggingClassifier__@1.1.3-1.2.0_L5_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(estimator, 0)'], gt_only=[] |
| 74 | `sklearn/ensemble.BaggingRegressor@1.1.3-1.2.0/ensemble.BaggingRegressor#1YY/BaggingRegressor__@1.1.3-1.2.0_L5_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(estimator, 0)'], gt_only=[] |
| 75 | `sklearn/linear_model.RANSACRegressor@0.17.1-0.18/linear_model.RANSACRegressor#1YY/RANSACRegressor__@0.17.1-0.18_L2_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(loss, 10)'], gt_only=[] |
| 76 | `sklearn/linear_model.RANSACRegressor@1.0.2-1.1.0/linear_model.RANSACRegressor#1YY/RANSACRegressor__@1.0.2-1.1.0_L5_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(estimator, 0)'], gt_only=[] |
| 77 | `sklearn/sklearn.cluster.SpectralClustering@0.21.3-0.22/sklearn.cluster.SpectralClustering#1YY/SpectralClustering_5_@0.21.3-0.22_L4_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(n_components, 2)'], gt_only=[] |
| 78 | `sklearn/sklearn.linear_model.BayesianRidge@0.21.3-0.22/sklearn.linear_model.BayesianRidge#1YY/linear_model.BayesianRidge__@0.21.3-0.22_L2_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(alpha_init, 6)', '(lambda_init, 7)'], gt_only=[] |
| 79 | `sklearn/sklearn.linear_model.PassiveAggressiveClassifier@0.18.1-0.19.0/sklearn.linear_model.PassiveAggressiveClassifier#1YY/PassiveAggressiveClassifier__@0.18.1-0.19.0_L2_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(max_iter, 2)', '(tol, 3)'], gt_only=[] |
| 80 | `sklearn/sklearn.svm.NuSVC@0.21.3-0.22/sklearn.svm.NuSVC#1YY/NuSVC__@0.21.3-0.22_L5_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(break_ties, 13)'], gt_only=[] |
| 81 | `sklearn/sklearn.svm.SVC@0.21.3-0.22/sklearn.svm.SVC#1YY/SVC__@0.21.3-0.22_L5_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(break_ties, 13)'], gt_only=[] |
| 82 | `sympy/sympy.physics.mechanics.PinJoint@1.11.1-1.12/sympy.physics.mechanics.PinJoint#1YY/PinJoint__PC___parent__child_@1.11.1-1.12_L4_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(child_point, 6)', '(parent_point, 5)'], gt_only=[] |
| 83 | `sympy/sympy.physics.mechanics.PrismaticJoint@1.11.1-1.12/sympy.physics.mechanics.PrismaticJoint#1YY/PrismaticJoint__PC___parent__child_@1.11.1-1.12_L4_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(child_point, 6)', '(parent_point, 5)'], gt_only=[] |
| 84 | `tensorflow/tf.keras.losses.SparseCategoricalCrossentropy@2.9.3-2.10.0/tf.keras.losses.SparseCategoricalCrossentropy#1YY/tf.keras.losses.SparseCategoricalCrossentropy__@2.9.3-2.10.0_L2_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(ignore_class, 1)'], gt_only=[] |
| 85 | `tensorflow/tf.string_split@1.13.2-1.14.0/tf.string_split#1YY/tf.string_split_string_tensor_@1.13.2-1.14.0_L4_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(sep, 1)'], gt_only=[] |
| 86 | `tornado/tornado.httpclient.HTTPRequest@3.0.2-3.1/tornado.httpclient.HTTPRequest#1YY/tornado.httpclient.HTTPRequest__http___httpbin.org_get__@3.0.2-3.1_L2_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(auth_mode, 6)'], gt_only=[] |
