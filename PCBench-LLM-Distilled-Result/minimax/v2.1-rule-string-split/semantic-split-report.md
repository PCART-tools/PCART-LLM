# PCBench-LLM-Distilled-NaN 语义切分对比报告

## 说明

- 切分依据：`/Users/ganymede/Downloads/PCART-LLM/PCBench-LLM-Distilled-groundTruth/Semantic-Related-contains_delete_or_rename.json`
- 命中 `files.delete_or_rename` 的样例记为“语义相关”
- 未命中的样例记为“语义不相关”
- 对比结果目录：`/Users/ganymede/Downloads/PCART-LLM/PCBench-LLM-Distilled-Result/minimax/v2.1-rule-string-split/PCBench-LLM-Distilled-NaN/Benchmark`
- 对比 ground truth：`/Users/ganymede/Downloads/PCART-LLM/PCBench-LLM-Distilled-groundTruth/PCBench-LLM-Distilled-groundTruth-DictOnly`
- 判定规则：结果 JSON 中的 `repairLst[].repairDict` 与对应 ground truth JSON 完全一致则记为“正确”，否则记为“错误”

## 总体统计

| 部分 | 样例数 | 正确 | 错误 | 正确率 |
| --- | ---: | ---: | ---: | ---: |
| 语义相关 | 171 | 129 | 42 | 75.44% |
| 语义不相关 | 113 | 48 | 65 | 42.48% |
| 合并后 | 284 | 177 | 107 | 62.32% |

## 语义相关

| 指标 | 数值 |
| --- | ---: |
| 样例数 | 171 |
| 正确 | 129 |
| 错误 | 42 |
| 正确率 | 75.44% |

### 错误样例

| 序号 | 样例路径 | 错误类型 | 差异说明 |
| --- | --- | --- | --- |
| 1 | `aiohttp/aiohttp.ClientSession@1.3.5-2.0.0/aiohttp.ClientSession#1YY/aiohttp.ClientSession__@1.3.5-2.0.0_L18_tempLst1.json` | mismatch | item 0 field (json_serialize, 7) mismatch: pred={'addKey': 'json_serialize'}, gt={'addKey': 'json_serialize=<functiondumpsat0x7af4f31667b8>'} |
| 2 | `gensim/gensim.models.doc2vec.Doc2Vec.similarity_unseen_docs@4.0.1-4.1.0/gensim.models.doc2vec.Doc2Vec.similarity_unseen_docs#1YY/model.similarity_unseen_docs_doc_words1__doc_words2_@4.0.1-4.1.0_L7_tempLst1.json` | mismatch | item 0 field (alpha, 2) mismatch: pred={'addPos': 'alpha=None'}, gt={} |
| 3 | `httpx/URL@0.13.3-0.14.0/URL#1YY/httpx.URL_url_str_@0.13.3-0.14.0_L4_tempLst1.json` | mismatch | item 0 field (params, 2) mismatch: pred={}, gt={'posChange': 1} |
| 4 | `httpx/httpx.AsyncClient@0.11.1-0.12.0/httpx.AsyncClient#1YY/httpx.AsyncClient__@0.11.1-0.12.0_L3_tempLst1.json` | mismatch | item 0 field (trust_env, 16) mismatch: pred={'posChange': 15}, gt={} |
| 5 | `httpx/httpx.delete@0.7.4-0.7.5/httpx.delete#1YY/delete__https___example.com_resource__@0.7.4-0.7.5_L2_tempLst1.json` | mismatch | item 0 field (allow_redirects, 10) mismatch: pred={'posChange': 7}, gt={} |
| 6 | `jax/jax.experimental.jax2tf.convert@0.4.12-0.4.13/jax.experimental.jax2tf.convert#1YY/jax2tf.convert_sum_of_squares_@0.4.12-0.4.13_L7_tempLst1.json` | mismatch | item 0 field (enable_xla, 4) mismatch: pred={'typeChange': 'bool'}, gt={} |
| 7 | `matplotlib/matplotlib.colorbar.Colorbar.set_ticks@3.6.3-3.7.0/matplotlib.colorbar.Colorbar.set_ticks#1YY/cbar.set_ticks_ticks_@3.6.3-3.7.0_L7_tempLst1.json` | mismatch | item 0 field (labels, 2) mismatch: pred={'key2pos': 'labels'}, gt={'pos2key': 'labels'} |
| 8 | `matplotlib/matplotlib.patches.FancyArrowPatch@3.5.3-3.6.0/matplotlib.patches.FancyArrowPatch#1YY/FancyArrowPatch__0.2__0.2____0.8__0.8__@3.5.3-3.6.0_L3_tempLst1.json` | mismatch | item 0 field (arrowstyle, 3) mismatch: pred={'posChange': 4, 'pos2key': 'arrowstyle'}, gt={'pos2key': 'arrowstyle'} |
| 9 | `networkx/average_neighbor_degree@1.5-1.6/average_neighbor_degree#1YY/nx.average_neighbor_degree_G_@1.5-1.6_L4_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(target, 2)'], gt_only=['(weight, 4)'] |
| 10 | `networkx/closeness_vitality@1.4-1.5/closeness_vitality#1YY/nx.closeness_vitality_G_@1.4-1.5_L4_tempLst1.json` | mismatch | item 0 field (G, 0) mismatch: pred={'addPos': 'G'}, gt={} |
| 11 | `networkx/clustering@1.5-1.6/clustering#1YY/nx.clustering_G_@1.5-1.6_L4_tempLst1.json` | mismatch | item 0 field (weighted, 2) mismatch: pred={'rename': 'weight'}, gt={'delete': 1, 'replace': 'weight=None'} |
| 12 | `networkx/degree@1.5-1.6/degree#1YY/G.degree__@1.5-1.6_L4_tempLst1.json` | mismatch | item 0 field (weighted, 1) mismatch: pred={'rename': 'weight'}, gt={'delete': 1, 'replace': 'weight=None'} |
| 13 | `networkx/geographical_threshold_graph@2.0-2.1/geographical_threshold_graph#1YY/nx.geographical_threshold_graph_10__0.1_@2.0-2.1_L2_tempLst1.json` | mismatch | item 0 field (metric, 6) mismatch: pred={'posChange': 5, 'replace': 'p_dist'}, gt={'posChange': 5, 'replace': 'p_dist=None'} |
| 14 | `networkx/is_isomorphic@1.5-1.6/is_isomorphic#1YY/nx.is_isomorphic_G1__G2_@1.5-1.6_L6_tempLst1.json` | mismatch | item 0 field (rtol, 3) mismatch: pred={'delete': 1, 'replace': 'edge_match'}, gt={'delete': 1, 'replace': 'edge_match=None'} |
| 15 | `networkx/networkx.closeness_centrality@1.4-1.5/networkx.closeness_centrality#1YY/nx.closeness_centrality_G_@1.4-1.5_L3_tempLst1.json` | mismatch | item 0 field (weighted_edges, 2) mismatch: pred={'rename': 'distance'}, gt={'delete': 1, 'replace': 'distance=None'} |
| 16 | `networkx/networkx.min_weight_matching@2.8.8-3.0/networkx.min_weight_matching#1YY/nx.min_weight_matching_G_@2.8.8-3.0_L4_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=[], gt_only=['(weight, 2)'] |
| 17 | `networkx/spectral_layout@1.5-1.6/spectral_layout#1YY/nx.spectral_layout_G_@1.5-1.6_L4_tempLst1.json` | mismatch | item 0 field (weighted, 2) mismatch: pred={'rename': 'weight'}, gt={'delete': 1, 'replace': "weight='weight'"} |
| 18 | `pandas/DataFrame.between_time@1.5.3-2.0.0/DataFrame.between_time#1YY/ts.between_time__0_15____0_45__@1.5.3-2.0.0_L4_tempLst1.json` | mismatch | item 0 field (axis, 5) mismatch: pred={'typeChange': "'Axis\|None'", 'posChange': 3}, gt={'posChange': 3} |
| 19 | `pandas/DataFrame.groupby@1.5.3-2.0.0/DataFrame.groupby#1YY/df.groupby___Animal___@1.5.3-2.0.0_L3_tempLst1.json` | mismatch | item 0 field (dropna, 8) mismatch: pred={}, gt={'posChange': 7} |
| 20 | `pandas/DataFrame.set_axis@1.5.3-2.0.0/DataFrame.set_axis#1YY/df.set_axis___a____b____c___@1.5.3-2.0.0_L3_tempLst1.json` | mismatch | item 0 field (copy, 4) mismatch: pred={'typeChange': "'bool\|None'"}, gt={'typeChange': 'bool\|None'} |
| 21 | `pandas/DataFrame.take@1.5.3-2.0.0/DataFrame.take#1YY/df.take__0__3__@1.5.3-2.0.0_L4_tempLst1.json` | mismatch | item 0 field (axis, 1) mismatch: pred={'typeChange': "'Axis'"}, gt={} |
| 22 | `pandas/DataFrame.to_excel@1.5.3-2.0.0/DataFrame.to_excel#1YY/df1.to_excel__._output.xlsx__@1.5.3-2.0.0_L3_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(freeze_panes, 14)', '(inf_rep, 12)', '(storage_options, 15)'], gt_only=['(freeze_panes, 15)', '(inf_rep, 13)', '(storage_options, 16)'] |
| 23 | `pandas/DataFrame.to_latex@1.5.3-2.0.0/DataFrame.to_latex#1YY/df.to_latex__@1.5.3-2.0.0_L3_tempLst1.json` | mismatch | item 0 field (buf, 0) mismatch: pred={'posChange': 0}, gt={} |
| 24 | `pandas/Series.groupby@1.5.3-2.0.0/Series.groupby#1YY/ser.groupby___a____b____a____b___@1.5.3-2.0.0_L3_tempLst1.json` | mismatch | item 0 field (group_keys, 5) mismatch: pred={'typeChange': "'bool'"}, gt={'typeChange': 'bool'} |
| 25 | `pandas/Series.set_axis@1.5.3-2.0.0/Series.set_axis#1YY/s.set_axis___a____b____c___@1.5.3-2.0.0_L3_tempLst1.json` | mismatch | item 0 field (copy, 4) mismatch: pred={'typeChange': "'bool\|None'", 'posChange': 3}, gt={'typeChange': 'bool\|None'} |
| 26 | `pandas/Timestamp@1.5.3-2.0.0/Timestamp#1YY/pd.Timestamp__2017-01-01T12__@1.5.3-2.0.0_L2_tempLst1.json` | mismatch | item 0 field (fold, 14) mismatch: pred={'pos2key': 'fold'}, gt={} |
| 27 | `pandas/bdate_range@1.5.3-2.0.0/bdate_range#1YY/pd.bdate_range__1_1_2018____1_08_2018__@1.5.3-2.0.0_L2_tempLst1.json` | mismatch | item 0 field (inclusive, 10) mismatch: pred={'posChange': 9}, gt={'typeChange': 'IntervalClosedType', 'posChange': 9} |
| 28 | `pandas/date_range@1.5.3-2.0.0/date_range#1YY/pd.date_range__1_1_2018____1_08_2018__@1.5.3-2.0.0_L2_tempLst1.json` | mismatch | item 0 field (closed, 7) mismatch: pred={'rename': 'inclusive'}, gt={'delete': 1} |
| 29 | `pandas/pandas.DataFrame.resample@1.5.3-2.0.0/pandas.DataFrame.resample#1YY/DataFrame.resample__3T__@1.5.3-2.0.0_L4_tempLst1.json` | mismatch | item 0 field (group_keys, 12) mismatch: pred={'typeChange': "'bool'", 'posChange': 10}, gt={'typeChange': 'bool', 'posChange': 10} |
| 30 | `pandas/pandas.Series.resample@1.5.3-2.0.0/pandas.Series.resample#1YY/series.resample__3T__@1.5.3-2.0.0_L4_tempLst1.json` | mismatch | item 0 field (group_keys, 12) mismatch: pred={'typeChange': "'bool'", 'posChange': 10}, gt={'typeChange': 'bool', 'posChange': 10} |
| 31 | `pandas/read_csv@1.5.3-2.0.0/read_csv#1YY/pd.read_csv__._dev.csv__@1.5.3-2.0.0_L2_tempLst1.json` | mismatch | item 0 field (cache_dates, 30) mismatch: pred={'posChange': 28}, gt={} |
| 32 | `pandas/testing.assert_extension_array_equal@1.5.3-2.0.0/testing.assert_extension_array_equal#1YY/tm.assert_extension_array_equal_b__c_@1.5.3-2.0.0_L5_tempLst1.json` | mismatch | item 0 field (check_exact, 5) mismatch: pred={'typeChange': "'bool'", 'posChange': 4}, gt={'posChange': 4} |
| 33 | `pandas/testing.assert_frame_equal@1.5.3-2.0.0/testing.assert_frame_equal#1YY/assert_frame_equal_df1__df1_@1.5.3-2.0.0_L5_tempLst1.json` | mismatch | item 0 field (atol, 16) mismatch: pred={'typeChange': "'float'", 'posChange': 15}, gt={'posChange': 15} |
| 34 | `pandas/testing.assert_series_equal@1.5.3-2.0.0/testing.assert_series_equal#1YY/tm.assert_series_equal_a__b_@1.5.3-2.0.0_L5_tempLst1.json` | mismatch | item 0 field (atol, 14) mismatch: pred={'typeChange': "'float'", 'posChange': 13}, gt={'posChange': 13} |
| 35 | `polars/polars.expr.str.strptime@0.17.15-0.18.0/polars.expr.str.strptime#1YY/a.str.strptime_pl.Date_@0.17.15-0.18.0_L4_tempLst1.json` | mismatch | item 0 field (utc, 6) mismatch: pred={'typeChange': 'bool\|None'}, gt={} |
| 36 | `pydantic/pydantic.main.create_model@1.4-1.5/pydantic.main.create_model#1YY/create_model__DynamicModel__@1.4-1.5_L13_tempLst1.json` | mismatch | item 0 field (model_name, 0) mismatch: pred={'rename': '__model_name'}, gt={'typeChange': 'str', 'rename': '__model_name'} |
| 37 | `rich/traceback.install@7.0.0-7.1.0/traceback.install#1YY/install__@7.0.0-7.1.0_L3_tempLst1.json` | mismatch | item 0 field (extra_lines, 4) mismatch: pred={'posChange': 3}, gt={} |
| 38 | `tensorflow/tf.contrib.data.make_csv_dataset@1.8.0-1.9.0/tf.contrib.data.make_csv_dataset#1NN/tf.contrib.data.make_csv_dataset__._dev.csv___1__None__None__None_______True______True__None__None__True__1__None__1__1__2__False__tf.float32__1_@1.8.0-1.9.0_L2_tempLst1.json` | mismatch | item 0 field (field_delim, 5) mismatch: pred={'posChange': 6, 'replace': 'select_columns'}, gt={'posChange': 6, 'replace': 'select_columns=None'} |
| 39 | `tensorflow/tf.data.experimental.service.DispatchServer@2.3.4-2.4.0/tf.data.experimental.service.DispatchServer#1NY/tf.data.experimental.service.DispatchServer_0_@2.3.4-2.4.0_L2_tempLst1.json` | mismatch | item 0 field (port, 0) mismatch: pred={'delete': 1, 'replace': 'config'}, gt={'delete': 1, 'replace': 'config=None'} |
| 40 | `torch/torch.btrifact@1.0.1-1.1.0/torch.btrifact#1YY/torch.btrifact_A_@1.0.1-1.1.0_L3_tempLst1.json` | mismatch | item 0 field (pivot, 2) mismatch: pred={'posChange': 1, 'replace': 'out'}, gt={'posChange': 1, 'replace': 'out=None'} |
| 41 | `tornado/tornado.iostream.BaseIOStream.read_bytes@5.1.1-6.0/tornado.iostream.BaseIOStream.read_bytes#1YY/stream.read_bytes_10_@5.1.1-6.0_L11_tempLst1.json` | mismatch | item 0 field (num_bytes, 0) mismatch: pred={'typeChange': 'int'}, gt={} |
| 42 | `transformers/transformers.modeling_albert.AlbertForPreTraining.forward@2.11.0-3.0.0/transformers.modeling_albert.AlbertForPreTraining.forward#1YY/model.forward_input_ids_@2.11.0-3.0.0_L11_tempLst1.json` | mismatch | item 0 field (output_attentions, 8) mismatch: pred={'addPos': 'output_attentions'}, gt={'addPos': 'output_attentions=None'} |

## 语义不相关

| 指标 | 数值 |
| --- | ---: |
| 样例数 | 113 |
| 正确 | 48 |
| 错误 | 65 |
| 正确率 | 42.48% |

### 错误样例

| 序号 | 样例路径 | 错误类型 | 差异说明 |
| --- | --- | --- | --- |
| 1 | `dask/dask.dataframe.core.drop@2.2.0-2.3.0/dask.dataframe.core.drop#1YY/ddf.drop__B___1_@2.2.0-2.3.0_L5_tempLst1.json` | mismatch | item 0 field (errors, 2) mismatch: pred={'posChange': 3, 'replace': 'columns'}, gt={'posChange': 3, 'replace': 'columns=None'} |
| 2 | `dask/dask.dataframe.drop_duplicates@2.4.0-2.5.0/dask.dataframe.drop_duplicates#1YY/ddf.drop_duplicates__@2.4.0-2.5.0_L5_tempLst1.json` | mismatch | item 0 field (split_every, 0) mismatch: pred={'posChange': 1}, gt={'posChange': 1, 'replace': 'subset=None'} |
| 3 | `dask/dask.dataframe.repartition@1.2.2-2.0.0/dask.dataframe.repartition#1YY/ddf.repartition_None__10_@1.2.2-2.0.0_L5_tempLst1.json` | mismatch | item 0 field (freq, 2) mismatch: pred={'posChange': 3}, gt={'posChange': 3, 'replace': 'partition_size=None'} |
| 4 | `flask/from_file@2.2.5-2.3.0/from_file#1YY/app.config.from_file__._test.json___json.load_@2.2.5-2.3.0_L4_tempLst1.json` | mismatch | item 0 field (filename, 0) mismatch: pred={'typeChange': "'str'"}, gt={} |
| 5 | `gensim/gensim.models.coherencemodel.CoherenceModel@0.13.1-0.13.2/gensim.models.coherencemodel.CoherenceModel#1NN/CoherenceModel_lda_model__documents_@0.13.1-0.13.2_L8_tempLst1.json` | mismatch | item 0 field (model, 0) mismatch: pred={'posChange': 0}, gt={} |
| 6 | `gensim/gensim.models.ldamodel.LdaModel.diff@2.3.0-3.0.0/gensim.models.ldamodel.LdaModel.diff#1YY/lda1.diff_lda2_@2.3.0-3.0.0_L9_tempLst1.json` | mismatch | item 0 field (annotation, 5) mismatch: pred={'addPos': 'annotation'}, gt={'addPos': 'annotation=True'} |
| 7 | `gensim/gensim.models.word2vec.Word2Vec.train@1.0.1-2.0.0/gensim.models.word2vec.Word2Vec.train#1NN/model.train_sentences_@1.0.1-2.0.0_L5_tempLst1.json` | mismatch | item 0 field (queue_factor, 4) mismatch: pred={'posChange': 7, 'replace': 'start_alpha'}, gt={'posChange': 7, 'replace': 'start_alpha=None'} |
| 8 | `keras/keras.preprocessing.image.ImageDataGenerator@2.1.4-2.1.5/keras.preprocessing.image.ImageDataGenerator#1YY/ImageDataGenerator__@2.1.4-2.1.5_L2_tempLst1.json` | mismatch | item 0 field (shear_range, 9) mismatch: pred={'posChange': 10, 'replace': 'brightness_range'}, gt={'posChange': 10, 'replace': 'brightness_range=None'} |
| 9 | `matplotlib/matplotlib.axes.Axes.imshow@3.4.3-3.5.0/matplotlib.axes.Axes.imshow#1YY/plt.imshow_X_@3.4.3-3.5.0_L4_tempLst1.json` | mismatch | item 0 field (interpolation_stage, 11) mismatch: pred={'addKey': 'interpolation_stage'}, gt={'addKey': 'interpolation_stage=None'} |
| 10 | `matplotlib/matplotlib.gridspec.GridSpec@2.1.2-2.2.0/matplotlib.gridspec.GridSpec#1YY/gridspec.GridSpec_2__2_@2.1.2-2.2.0_L3_tempLst1.json` | mismatch | item 0 field (left, 2) mismatch: pred={'posChange': 3, 'replace': 'left'}, gt={'posChange': 3, 'replace': 'figure=None'} |
| 11 | `networkx/networkx.linalg.graphmatrix.adjacency_matrix@2.5.1-2.6/networkx.linalg.graphmatrix.adjacency_matrix#1YY/nx.adjacency_matrix_G_@2.5.1-2.6_L4_tempLst1.json` | mismatch | item 0 field (weight, 2) mismatch: pred={'posChange': 3, 'replace': 'weight'}, gt={'posChange': 3, 'replace': 'dtype=None'} |
| 12 | `numpy/numpy.percentile@1.21.6-1.22.0/numpy.percentile#1YY/np.percentile_a___25__50__75__@1.21.6-1.22.0_L3_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(method, 5)'], gt_only=[] |
| 13 | `numpy/numpy.quantile@1.21.6-1.22.0/numpy.quantile#1YY/np.quantile_a__q_@1.21.6-1.22.0_L9_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(method, 5)'], gt_only=[] |
| 14 | `pandas/DataFrame.ewm@1.3.5-1.4.0/DataFrame.ewm#1YY/df.ewm_0.5_@1.3.5-1.4.0_L4_tempLst1.json` | mismatch | item 0 field (times, 8) mismatch: pred={}, gt={'typeChange': 'str\|np.ndarray\|DataFrame\|Series\|None'} |
| 15 | `pandas/DataFrame.reset_index@1.4.4-1.5.0/DataFrame.reset_index#1YY/df.reset_index__@1.4.4-1.5.0_L4_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=[], gt_only=['(allow_duplicates, 5)', '(names, 6)'] |
| 16 | `pandas/DataFrame.rolling@1.4.4-1.5.0/DataFrame.rolling#1YY/df.rolling_2_@1.4.4-1.5.0_L4_tempLst1.json` | mismatch | item 0 field (method, 7) mismatch: pred={'posChange': 8, 'replace': 'step'}, gt={'posChange': 8, 'replace': 'step=None'} |
| 17 | `pandas/DataFrame.to_stata@1.3.5-1.4.0/DataFrame.to_stata#1YY/df.to_stata__animals.dta__@1.3.5-1.4.0_L3_tempLst1.json` | mismatch | item 0 field (path, 0) mismatch: pred={'typeChange': "'FilePath\|WriteBuffer[bytes]'"}, gt={'typeChange': 'FilePath\|WriteBuffer[bytes]'} |
| 18 | `pandas/Series.ewm@1.3.5-1.4.0/Series.ewm#1YY/df.ewm_0.5_@1.3.5-1.4.0_L4_tempLst1.json` | mismatch | item 0 field (times, 8) mismatch: pred={'typeChange': "'str\|np.ndarray\|DataFrame\|Series\|None'"}, gt={'typeChange': 'str\|np.ndarray\|DataFrame\|Series\|None'} |
| 19 | `pandas/Series.rolling@1.4.4-1.5.0/Series.rolling#1YY/df.rolling_2_@1.4.4-1.5.0_L4_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(method, 8)', '(step, 7)'], gt_only=['(method, 7)'] |
| 20 | `pandas/Styler.background_gradient@1.2.5-1.3.0/Styler.background_gradient#1YY/df.style.background_gradient__@1.2.5-1.3.0_L13_tempLst1.json` | mismatch | item 0 field (axis, 3) mismatch: pred={}, gt={'typeChange': 'Axis\|None'} |
| 21 | `pandas/Styler.format@1.2.5-1.3.0/Styler.format#1YY/df.style.format____.2____@1.2.5-1.3.0_L4_tempLst1.json` | mismatch | item 0 field (decimal, 4) mismatch: pred={'addPos': 'decimal'}, gt={'addPos': "decimal='.'"} |
| 22 | `pandas/melt@1.0.5-1.1.0/melt#1YY/pd.melt_df_@1.0.5-1.1.0_L3_tempLst1.json` | mismatch | item 0 field (frame, 0) mismatch: pred={'typeChange': "'DataFrame'"}, gt={'typeChange': 'DataFrame'} |
| 23 | `pandas/read_csv@1.2.5-1.3.0/read_csv#1YY/pd.read_csv__._dev.csv__@1.2.5-1.3.0_L2_tempLst1.json` | mismatch | item 0 field (decimal, 34) mismatch: pred={'typeChange': "'str'"}, gt={} |
| 24 | `pandas/testing.assert_frame_equal@1.0.5-1.1.0/testing.assert_frame_equal#1YY/assert_frame_equal_df1__df1_@1.0.5-1.1.0_L5_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(check_freq, 13)'], gt_only=[] |
| 25 | `plotly/plotly.express.area@4.2.1-4.3.0/plotly.express.area#1YY/px.area__@4.2.1-4.3.0_L3_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(facet_col_wrap, 11)'], gt_only=[] |
| 26 | `plotly/plotly.express.bar@4.14.3-5.0.0/plotly.express.bar#1YY/px.bar__@4.14.3-5.0.0_L3_tempLst1.json` | mismatch | item 0 field (color, 3) mismatch: pred={'posChange': 3}, gt={} |
| 27 | `plotly/plotly.express.bar@4.2.1-4.3.0/plotly.express.bar#1YY/px.bar__@4.2.1-4.3.0_L3_tempLst1.json` | mismatch | item 0 field (hover_name, 6) mismatch: pred={'posChange': 7, 'replace': 'hover_name'}, gt={'posChange': 7, 'replace': 'facet_col_wrap=0'} |
| 28 | `plotly/plotly.express.bar@5.4.0-5.5.0/plotly.express.bar#1YY/px.bar__@5.4.0-5.5.0_L3_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(height, 41)', '(template, 39)', '(text_auto, 37)'], gt_only=['(height, 40)', '(template, 38)', '(title, 37)'] |
| 29 | `plotly/plotly.express.bar_polar@4.3.0-4.4.0/plotly.express.bar_polar#1YY/px.bar_polar__@4.3.0-4.4.0_L3_tempLst1.json` | mismatch | item 0 field (log_r, 18) mismatch: pred={'posChange': 19, 'replace': 'log_r'}, gt={'posChange': 19, 'replace': 'range_theta=None'} |
| 30 | `plotly/plotly.express.box@4.2.1-4.3.0/plotly.express.box#1YY/px.box__@4.2.1-4.3.0_L3_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(facet_col_wrap, 6)'], gt_only=[] |
| 31 | `plotly/plotly.express.density_contour@5.1.0-5.2.1/plotly.express.density_contour#1YY/px.density_contour__@5.1.0-5.2.1_L3_tempLst1.json` | mismatch | item 0 field (log_y, 24) mismatch: pred={'posChange': 26, 'replace': 'log_y'}, gt={'posChange': 26, 'replace': "trendline_scope='trace'"} |
| 32 | `plotly/plotly.express.density_heatmap@4.2.1-4.3.0/plotly.express.density_heatmap#1YY/px.density_heatmap__@4.2.1-4.3.0_L3_tempLst1.json` | mismatch | item 0 field (data_frame, 0) mismatch: pred={'posChange': 0}, gt={} |
| 33 | `plotly/plotly.express.histogram@4.14.3-5.0.0/plotly.express.histogram#1YY/px.histogram__@4.14.3-5.0.0_L3_tempLst1.json` | mismatch | item 0 field (facet_row, 4) mismatch: pred={'posChange': 5, 'replace': 'pattern_shape'}, gt={'posChange': 5, 'replace': 'pattern_shape=None'} |
| 34 | `plotly/plotly.express.imshow@4.13.0-4.14.0/plotly.express.imshow#1YY/px.imshow_img_rgb_@4.13.0-4.14.0_L4_tempLst1.json` | mismatch | item 0 field (color_continuous_midpoint, 8) mismatch: pred={'posChange': 13, 'replace': 'facet_col'}, gt={'posChange': 13, 'replace': 'facet_col=None'} |
| 35 | `plotly/plotly.express.line@5.1.0-5.2.1/plotly.express.line#1YY/px.line__@5.1.0-5.2.1_L3_tempLst1.json` | mismatch | item 0 field (color, 4) mismatch: pred={'posChange': 4}, gt={} |
| 36 | `plotly/plotly.express.line_3d@5.1.0-5.2.1/plotly.express.line_3d#1YY/px.line_3d__@5.1.0-5.2.1_L3_tempLst1.json` | mismatch | item 0 field (color, 4) mismatch: pred={'posChange': 4}, gt={} |
| 37 | `plotly/plotly.express.line_geo@5.1.0-5.2.1/plotly.express.line_geo#1YY/px.line_geo__@5.1.0-5.2.1_L3_tempLst1.json` | mismatch | item 0 field (animation_frame, 19) mismatch: pred={'posChange': 20, 'replace': 'symbol'}, gt={'posChange': 20, 'replace': 'symbol=None'} |
| 38 | `plotly/plotly.express.line_mapbox@4.3.0-4.4.0/plotly.express.line_mapbox#1YY/px.line_mapbox_us_cities___lat____lon__@4.3.0-4.4.0_L5_tempLst1.json` | mismatch | item 0 field (template, 17) mismatch: pred={'posChange': 19, 'replace': 'mapbox_style'}, gt={'posChange': 19, 'replace': 'mapbox_style=None'} |
| 39 | `plotly/plotly.express.line_polar@4.3.0-4.4.0/plotly.express.line_polar#1YY/px.line_polar__@4.3.0-4.4.0_L3_tempLst1.json` | mismatch | item 0 field (log_r, 24) mismatch: pred={'posChange': 25, 'replace': 'range_theta'}, gt={'posChange': 25, 'replace': 'range_theta=None'} |
| 40 | `plotly/plotly.express.line_polar@5.1.0-5.2.1/plotly.express.line_polar#1YY/px.line_polar__@5.1.0-5.2.1_L3_tempLst1.json` | mismatch | item 0 field (animation_frame, 10) mismatch: pred={'posChange': 11, 'replace': 'symbol'}, gt={'posChange': 11, 'replace': 'symbol=None'} |
| 41 | `plotly/plotly.express.scatter@4.2.1-4.3.0/plotly.express.scatter#1YY/px.scatter__@4.2.1-4.3.0_L3_tempLst1.json` | mismatch | item 0 field (error_x, 12) mismatch: pred={'posChange': 13, 'replace': 'error_x'}, gt={'posChange': 13, 'replace': 'facet_col_wrap=0'} |
| 42 | `plotly/plotly.express.scatter@5.1.0-5.2.1/plotly.express.scatter#1YY/px.scatter__@5.1.0-5.2.1_L3_tempLst1.json` | mismatch | item 0 field (trendline_color_override, 36) mismatch: pred={'posChange': 37, 'replace': 'trendline_options'}, gt={'posChange': 37, 'replace': 'trendline_options=None'} |
| 43 | `plotly/plotly.express.sunburst@4.4.1-4.5.0/plotly.express.sunburst#1YY/px.sunburst__@4.4.1-4.5.0_L3_tempLst1.json` | mismatch | item 0 field (ids, 4) mismatch: pred={'posChange': 5, 'replace': 'path'}, gt={'posChange': 5, 'replace': 'path=None'} |
| 44 | `plotly/plotly.tools.FigureFactory.create_distplot@1.10.0-1.11.0/plotly.tools.FigureFactory.create_distplot#1YY/FF.create_distplot_hist_data__group_labels_@1.10.0-1.11.0_L9_tempLst1.json` | mismatch | item 0 field (show_hist, 6) mismatch: pred={'posChange': 7, 'replace': 'histnorm=probabilitydensity'}, gt={'posChange': 7, 'replace': "histnorm='probabilitydensity'"} |
| 45 | `polars/polars.arg_where@0.16.18-0.17.0/polars.arg_where#1YY/pl.arg_where_pl.col__a_____2____0_@0.16.18-0.17.0_L2_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(eager, 2)'], gt_only=[] |
| 46 | `polars/polars.repeat@0.17.14-0.17.15/polars.repeat#1YY/pl.repeat__z___3_@0.17.14-0.17.15_L2_tempLst1.json` | mismatch | item 0 field (eager, 3) mismatch: pred={'posChange': 4}, gt={} |
| 47 | `rich/Columns@1.3.0-1.3.1/Columns#1YY/Columns_renderables_@1.3.0-1.3.1_L3_tempLst1.json` | mismatch | item 0 field (expand, 2) mismatch: pred={'posChange': 3, 'replace': 'width'}, gt={'posChange': 3, 'replace': 'width=None'} |
| 48 | `rich/rich.syntax.Syntax.from_path@11.0.0-11.1.0/rich.syntax.Syntax.from_path#1YY/Syntax.from_path__._example.py__@11.0.0-11.1.0_L2_tempLst1.json` | mismatch | item 0 field (theme, 2) mismatch: pred={'typeChange': 'Union[str,rich.syntax.SyntaxTheme]', 'posChange': 3, 'replace': , gt={'posChange': 3, 'replace': 'lexer=None'} |
| 49 | `scipy/scipy.stats.qmc.LatinHypercube@1.9.3-1.10.0/scipy.stats.qmc.LatinHypercube#1YY/qmc.LatinHypercube_d_@1.9.3-1.10.0_L7_tempLst1.json` | mismatch | item 0 field (optimization, 4) mismatch: pred={'typeChange': "Optional[Literal[('random-cd','lloyd')]]", 'posChange': 5}, gt={'typeChange': '"Optional[Literal[(\'random-cd\',\'lloyd\')]]"'} |
| 50 | `sklearn/calibration.CalibratedClassifierCV@1.1.3-1.2.0/calibration.CalibratedClassifierCV#1YY/CalibratedClassifierCV__@1.1.3-1.2.0_L6_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(estimator, 0)'], gt_only=[] |
| 51 | `sklearn/ensemble.AdaBoostClassifier@1.1.3-1.2.0/ensemble.AdaBoostClassifier#1YY/AdaBoostClassifier__@1.1.3-1.2.0_L4_tempLst1.json` | mismatch | item 0 field (base_estimator, 0) mismatch: pred={'pos2key': 'base_estimator'}, gt={'replace': 'estimator=None', 'pos2key': 'base_estimator'} |
| 52 | `sklearn/ensemble.AdaBoostRegressor@1.1.3-1.2.0/ensemble.AdaBoostRegressor#1YY/AdaBoostRegressor__@1.1.3-1.2.0_L4_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(base_estimator, 1)', '(base_estimator, 6)'], gt_only=[] |
| 53 | `sklearn/ensemble.BaggingClassifier@1.1.3-1.2.0/ensemble.BaggingClassifier#1YY/BaggingClassifier__@1.1.3-1.2.0_L5_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(estimator, 0)'], gt_only=[] |
| 54 | `sklearn/ensemble.BaggingRegressor@1.1.3-1.2.0/ensemble.BaggingRegressor#1YY/BaggingRegressor__@1.1.3-1.2.0_L5_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(estimator, 0)'], gt_only=[] |
| 55 | `sklearn/ensemble.HistGradientBoostingRegressor@0.22.2-0.23.0/ensemble.HistGradientBoostingRegressor#1YY/HistGradientBoostingRegressor__@0.22.2-0.23.0_L5_tempLst1.json` | mismatch | item 0 field (l2_regularization, 6) mismatch: pred={'posChange': 7, 'pos2key': 'l2_regularization'}, gt={'pos2key': 'l2_regularization'} |
| 56 | `sklearn/linear_model.Lars@0.22.2-0.23.0/linear_model.Lars#1YY/linear_model.Lars__@0.22.2-0.23.0_L2_tempLst1.json` | mismatch | item 0 field (jitter, 9) mismatch: pred={'addKey': 'jitter'}, gt={'addKey': 'jitter=None'} |
| 57 | `sklearn/linear_model.LassoLars@0.22.2-0.23.0/linear_model.LassoLars#1YY/linear_model.LassoLars__@0.22.2-0.23.0_L2_tempLst1.json` | mismatch | item 0 field (jitter, 11) mismatch: pred={'addKey': 'jitter'}, gt={'addKey': 'jitter=None'} |
| 58 | `sklearn/linear_model.RANSACRegressor@1.0.2-1.1.0/linear_model.RANSACRegressor#1YY/RANSACRegressor__@1.0.2-1.1.0_L5_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(estimator, 0)'], gt_only=[] |
| 59 | `sklearn/sklearn.cluster.SpectralClustering@0.21.3-0.22/sklearn.cluster.SpectralClustering#1YY/SpectralClustering_5_@0.21.3-0.22_L4_tempLst1.json` | mismatch | item 0 field (random_state, 2) mismatch: pred={'posChange': 3, 'replace': 'n_components'}, gt={'posChange': 3, 'replace': 'n_components=None'} |
| 60 | `sklearn/sklearn.linear_model.PassiveAggressiveClassifier@0.18.1-0.19.0/sklearn.linear_model.PassiveAggressiveClassifier#1YY/PassiveAggressiveClassifier__@0.18.1-0.19.0_L2_tempLst1.json` | mismatch | item 0 field (n_iter, 2) mismatch: pred={'posChange': 12, 'replace': 'max_iter'}, gt={'posChange': 12, 'replace': 'max_iter=None'} |
| 61 | `sklearn/sklearn.svm.NuSVC@0.21.3-0.22/sklearn.svm.NuSVC#1YY/NuSVC__@0.21.3-0.22_L5_tempLst1.json` | mismatch | item 0 field (random_state, 13) mismatch: pred={'posChange': 14}, gt={'posChange': 14, 'replace': 'break_ties=False'} |
| 62 | `sympy/sympy.physics.mechanics.PrismaticJoint@1.11.1-1.12/sympy.physics.mechanics.PrismaticJoint#1YY/PrismaticJoint__PC___parent__child_@1.11.1-1.12_L4_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(child_joint_pos, 13)', '(parent_joint_pos, 12)'], gt_only=[] |
| 63 | `tensorflow/tf.data.Dataset.random@2.11.1-2.12.0/tf.data.Dataset.random#1YY/tf.data.Dataset.random__@2.11.1-2.12.0_L2_tempLst1.json` | mismatch | item 0 field (name, 1) mismatch: pred={'posChange': 2}, gt={'posChange': 2, 'replace': 'rerandomize_each_iteration=None'} |
| 64 | `tensorflow/tf.keras.losses.SparseCategoricalCrossentropy@2.9.3-2.10.0/tf.keras.losses.SparseCategoricalCrossentropy#1YY/tf.keras.losses.SparseCategoricalCrossentropy__@2.9.3-2.10.0_L2_tempLst1.json` | mismatch | item 0 field (reduction, 1) mismatch: pred={'posChange': 2, 'replace': 'ignore_class'}, gt={'posChange': 2, 'replace': 'ignore_class=None'} |
| 65 | `tensorflow/tf.string_split@1.13.2-1.14.0/tf.string_split#1YY/tf.string_split_string_tensor_@1.13.2-1.14.0_L4_tempLst1.json` | mismatch | item 0 field (delimiter, 1) mismatch: pred={'posChange': 3, 'replace': 'sep'}, gt={'posChange': 3, 'replace': 'sep=None'} |
