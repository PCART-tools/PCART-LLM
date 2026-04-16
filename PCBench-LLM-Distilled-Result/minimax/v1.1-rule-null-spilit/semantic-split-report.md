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
| 语义相关 | 171 | 124 | 47 | 72.51% |
| 语义不相关 | 113 | 55 | 58 | 48.67% |
| 合并后 | 284 | 179 | 105 | 63.03% |

## 语义相关

| 指标 | 数值 |
| --- | ---: |
| 样例数 | 171 |
| 正确 | 124 |
| 错误 | 47 |
| 正确率 | 72.51% |

### 错误样例

| 序号 | 样例路径 | 错误类型 | 差异说明 |
| --- | --- | --- | --- |
| 1 | `aiohttp/aiohttp.ClientSession@1.3.5-2.0.0/aiohttp.ClientSession#1YY/aiohttp.ClientSession__@1.3.5-2.0.0_L18_tempLst1.json` | mismatch | item 0 field (cookie_jar, 11) mismatch: pred={'posChange': 12}, gt={} |
| 2 | `fastapi/fastapi.encoders.jsonable_encoder@0.60.2-0.61.0/fastapi.encoders.jsonable_encoder#1YY/jsonable_encoder_item_@0.60.2-0.61.0_L14_tempLst1.json` | mismatch | item 0 field (exclude, 2) mismatch: pred={}, gt={'typeChange': 'Optional[Union[SetIntStr,DictIntStrAny]]'} |
| 3 | `gensim/gensim.models.fasttext.FastText@3.8.3-4.0.0/gensim.models.fasttext.FastText#1YY/FastText__@3.8.3-4.0.0_L2_tempLst1.json` | mismatch | item 0 field (iter, 18) mismatch: pred={'posChange': 18, 'replace': 'epochs=5'}, gt={'rename': 'epochs'} |
| 4 | `gensim/gensim.models.hdpmodel.HdpModel.print_topics@0.13.1-0.13.2/gensim.models.hdpmodel.HdpModel.print_topics#1YY/hdp.print_topics__@0.13.1-0.13.2_L7_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(num_topics, 0)', '(num_words, 1)'], gt_only=['(topics, 0)', '(topn, 1)'] |
| 5 | `httpx/URL@0.13.3-0.14.0/URL#1YY/httpx.URL_url_str_@0.13.3-0.14.0_L4_tempLst1.json` | mismatch | item 0 field (params, 2) mismatch: pred={'typeChange': "Union[ForwardRef('QueryParams'),Mapping[str,Union[str,int,float,, gt={'posChange': 1} |
| 6 | `jax/jax.experimental.jax2tf.convert@0.4.12-0.4.13/jax.experimental.jax2tf.convert#1YY/jax2tf.convert_sum_of_squares_@0.4.12-0.4.13_L7_tempLst1.json` | mismatch | item 0 field (enable_xla, 4) mismatch: pred={'typeChange': 'bool'}, gt={} |
| 7 | `networkx/average_clustering@1.5-1.6/average_clustering#1YY/nx.average_clustering_G_@1.5-1.6_L4_tempLst1.json` | mismatch | item 0 field (weight, 2) mismatch: pred={'addPos': 'weight'}, gt={'addPos': 'weight=None'} |
| 8 | `networkx/clustering@1.5-1.6/clustering#1YY/nx.clustering_G_@1.5-1.6_L4_tempLst1.json` | mismatch | item 0 field (weighted, 2) mismatch: pred={'rename': 'weight'}, gt={'delete': 1, 'replace': 'weight=None'} |
| 9 | `networkx/degree@1.5-1.6/degree#1YY/G.degree__@1.5-1.6_L4_tempLst1.json` | mismatch | item 0 field (weighted, 1) mismatch: pred={'rename': 'weight'}, gt={'delete': 1, 'replace': 'weight=None'} |
| 10 | `networkx/is_isomorphic@1.5-1.6/is_isomorphic#1YY/nx.is_isomorphic_G1__G2_@1.5-1.6_L6_tempLst1.json` | mismatch | item 0 field (rtol, 3) mismatch: pred={'delete': 1, 'replace': 'edge_match'}, gt={'delete': 1, 'replace': 'edge_match=None'} |
| 11 | `networkx/networkx.closeness_centrality@1.4-1.5/networkx.closeness_centrality#1YY/nx.closeness_centrality_G_@1.4-1.5_L3_tempLst1.json` | mismatch | item 0 field (weighted_edges, 2) mismatch: pred={'rename': 'distance'}, gt={'delete': 1, 'replace': 'distance=None'} |
| 12 | `networkx/spectral_layout@1.5-1.6/spectral_layout#1YY/nx.spectral_layout_G_@1.5-1.6_L4_tempLst1.json` | mismatch | item 0 field (weighted, 2) mismatch: pred={'rename': 'weight'}, gt={'delete': 1, 'replace': "weight='weight'"} |
| 13 | `numpy/numpy.genfromtxt@1.9.3-1.10.0/numpy.genfromtxt#1YY/np.genfromtxt_f_@1.9.3-1.10.0_L4_tempLst1.json` | mismatch | item 0 field (loose, 21) mismatch: pred={'posChange': 19, 'replace': 'max_rows'}, gt={'posChange': 19, 'replace': 'max_rows=None'} |
| 14 | `numpy/numpy.histogram2d@1.23.5-1.24.0/numpy.histogram2d#1YY/np.histogram2d_x__y_@1.23.5-1.24.0_L4_tempLst1.json` | mismatch | item 0 field (weights, 5) mismatch: pred={'posChange': 5}, gt={} |
| 15 | `pandas/DataFrame.between_time@1.5.3-2.0.0/DataFrame.between_time#1YY/ts.between_time__0_15____0_45__@1.5.3-2.0.0_L4_tempLst1.json` | mismatch | item 0 field (axis, 5) mismatch: pred={'typeChange': "'Axis\|None'", 'posChange': 3}, gt={'posChange': 3} |
| 16 | `pandas/DataFrame.groupby@1.5.3-2.0.0/DataFrame.groupby#1YY/df.groupby___Animal___@1.5.3-2.0.0_L3_tempLst1.json` | mismatch | item 0 field (group_keys, 5) mismatch: pred={'typeChange': "'bool'"}, gt={'typeChange': 'bool'} |
| 17 | `pandas/DataFrame.set_axis@1.5.3-2.0.0/DataFrame.set_axis#1YY/df.set_axis___a____b____c___@1.5.3-2.0.0_L3_tempLst1.json` | mismatch | item 0 field (copy, 4) mismatch: pred={'typeChange': "'bool\|None'"}, gt={'typeChange': 'bool\|None'} |
| 18 | `pandas/DataFrame.take@1.5.3-2.0.0/DataFrame.take#1YY/df.take__0__3__@1.5.3-2.0.0_L4_tempLst1.json` | mismatch | item 0 field (axis, 1) mismatch: pred={'typeChange': "'Axis'"}, gt={} |
| 19 | `pandas/DataFrame.to_latex@1.5.3-2.0.0/DataFrame.to_latex#1YY/df.to_latex__@1.5.3-2.0.0_L3_tempLst1.json` | mismatch | item 0 field (col_space, 2) mismatch: pred={}, gt={'delete': 1} |
| 20 | `pandas/Series.groupby@1.5.3-2.0.0/Series.groupby#1YY/ser.groupby___a____b____a____b___@1.5.3-2.0.0_L3_tempLst1.json` | mismatch | item 0 field (dropna, 8) mismatch: pred={}, gt={'posChange': 7} |
| 21 | `pandas/Series.set_axis@1.5.3-2.0.0/Series.set_axis#1YY/s.set_axis___a____b____c___@1.5.3-2.0.0_L3_tempLst1.json` | mismatch | item 0 field (copy, 4) mismatch: pred={'typeChange': "'bool\|None'", 'posChange': 3}, gt={'typeChange': 'bool\|None'} |
| 22 | `pandas/bdate_range@1.5.3-2.0.0/bdate_range#1YY/pd.bdate_range__1_1_2018____1_08_2018__@1.5.3-2.0.0_L2_tempLst1.json` | mismatch | item 0 field (freq, 3) mismatch: pred={'typeChange': "'Frequency'"}, gt={} |
| 23 | `pandas/date_range@1.5.3-2.0.0/date_range#1YY/pd.date_range__1_1_2018____1_08_2018__@1.5.3-2.0.0_L2_tempLst1.json` | mismatch | item 0 field (inclusive, 8) mismatch: pred={'typeChange': "'IntervalClosedType'", 'posChange': 7}, gt={'typeChange': 'IntervalClosedType', 'posChange': 7} |
| 24 | `pandas/pandas.DataFrame.resample@1.5.3-2.0.0/pandas.DataFrame.resample#1YY/DataFrame.resample__3T__@1.5.3-2.0.0_L4_tempLst1.json` | mismatch | item 0 field (group_keys, 12) mismatch: pred={'typeChange': "'bool'", 'posChange': 10}, gt={'typeChange': 'bool', 'posChange': 10} |
| 25 | `pandas/pandas.Series.resample@1.5.3-2.0.0/pandas.Series.resample#1YY/series.resample__3T__@1.5.3-2.0.0_L4_tempLst1.json` | mismatch | item 0 field (group_keys, 12) mismatch: pred={'typeChange': "'bool'", 'posChange': 10}, gt={'typeChange': 'bool', 'posChange': 10} |
| 26 | `pandas/read_csv@1.5.3-2.0.0/read_csv#1YY/pd.read_csv__._dev.csv__@1.5.3-2.0.0_L2_tempLst1.json` | mismatch | item 0 field (cache_dates, 30) mismatch: pred={'posChange': 28}, gt={} |
| 27 | `pandas/testing.assert_extension_array_equal@1.5.3-2.0.0/testing.assert_extension_array_equal#1YY/tm.assert_extension_array_equal_b__c_@1.5.3-2.0.0_L5_tempLst1.json` | mismatch | item 0 field (atol, 7) mismatch: pred={'posChange': 6, 'replace': 'obj'}, gt={'posChange': 6, 'replace': "obj='ExtensionArray'"} |
| 28 | `pandas/testing.assert_frame_equal@1.5.3-2.0.0/testing.assert_frame_equal#1YY/assert_frame_equal_df1__df1_@1.5.3-2.0.0_L5_tempLst1.json` | mismatch | item 0 field (atol, 16) mismatch: pred={'typeChange': "'float'", 'posChange': 15}, gt={'posChange': 15} |
| 29 | `pandas/testing.assert_series_equal@1.5.3-2.0.0/testing.assert_series_equal#1YY/tm.assert_series_equal_a__b_@1.5.3-2.0.0_L5_tempLst1.json` | mismatch | item 0 field (atol, 14) mismatch: pred={'typeChange': "'float'", 'posChange': 13}, gt={'posChange': 13} |
| 30 | `polars/polars.Expr.str.ljust@0.16.18-0.17.0/polars.Expr.str.ljust#1YY/context.str.ljust_10_@0.16.18-0.17.0_L4_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(fill_char, 1)'], gt_only=['(fillchar, 1)'] |
| 31 | `polars/polars.expr.str.strptime@0.17.15-0.18.0/polars.expr.str.strptime#1YY/a.str.strptime_pl.Date_@0.17.15-0.18.0_L4_tempLst1.json` | mismatch | item 0 field (utc, 6) mismatch: pred={'typeChange': 'bool\|None'}, gt={} |
| 32 | `pydantic/pydantic.main.create_model@1.4-1.5/pydantic.main.create_model#1YY/create_model__DynamicModel__@1.4-1.5_L13_tempLst1.json` | mismatch | item 0 field (model_name, 0) mismatch: pred={'rename': '__model_name'}, gt={'typeChange': 'str', 'rename': '__model_name'} |
| 33 | `rich/rich.syntax.Syntax@10.16.2-11.0.0/rich.syntax.Syntax#1YY/Syntax__print__hello_world______python__@10.16.2-11.0.0_L2_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(lexer, 1)'], gt_only=[] |
| 34 | `rich/traceback.install@7.0.0-7.1.0/traceback.install#1YY/install__@7.0.0-7.1.0_L3_tempLst1.json` | mismatch | item 0 field (extra_lines, 4) mismatch: pred={'posChange': 3}, gt={} |
| 35 | `scipy/scipy.sparse.linalg.splu@0.19.1-1.0.0/scipy.sparse.linalg.splu#1YY/splu_A_@0.19.1-1.0.0_L4_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(drop_tol, 2)'], gt_only=['(drop_tol, 3)'] |
| 36 | `sklearn/ensemble.GradientBoostingRegressor@0.23.2-0.24.0/ensemble.GradientBoostingRegressor#1YY/GradientBoostingRegressor__@0.23.2-0.24.0_L6_tempLst1.json` | mismatch | item 0 field (ccp_alpha, 23) mismatch: pred={'posChange': 22}, gt={} |
| 37 | `sklearn/linear_model.RANSACRegressor@1.2.2-1.3.0/linear_model.RANSACRegressor#1YY/RANSACRegressor__@1.2.2-1.3.0_L4_tempLst1.json` | mismatch | item 0 field (base_estimator, 13) mismatch: pred={'rename': 'estimator'}, gt={'delete': 1} |
| 38 | `sklearn/linear_model.lasso_path@0.15.2-0.16.0/linear_model.lasso_path#1YY/lasso_path_X__y_@0.15.2-0.16.0_L5_tempLst1.json` | mismatch | item 0 field (coef_init, 10) mismatch: pred={'posChange': 8, 'replace': 'coef_init'}, gt={'posChange': 8, 'replace': 'return_n_iter=False'} |
| 39 | `sympy/sympy.crypto.crypto.rsa_public_key@1.4-1.5/sympy.crypto.crypto.rsa_public_key#1YY/rsa_public_key_p__q__e_@1.4-1.5_L6_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=[], gt_only=['(e, 2)', '(p, 0)', '(q, 1)'] |
| 40 | `tensorflow/tf.contrib.data.make_csv_dataset@1.10.1-1.11.0/tf.contrib.data.make_csv_dataset#1NN/tf.contrib.data.make_csv_dataset__._dev.csv___1__None__None__None__None_______True______True__None__True__10000__None__1__1__2__False__1_@1.10.1-1.11.0_L2_tempLst1.json` | mismatch | item 0 field (num_rows_for_inference, 18) mismatch: pred={'posChange': 17, 'replace': 'compression_type'}, gt={'posChange': 17, 'replace': 'compression_type=None'} |
| 41 | `tensorflow/tf.contrib.data.make_csv_dataset@1.8.0-1.9.0/tf.contrib.data.make_csv_dataset#1NN/tf.contrib.data.make_csv_dataset__._dev.csv___1__None__None__None_______True______True__None__None__True__1__None__1__1__2__False__tf.float32__1_@1.8.0-1.9.0_L2_tempLst1.json` | mismatch | item 0 field (default_float_type, 18) mismatch: pred={}, gt={'delete': 1} |
| 42 | `tensorflow/tf.data.experimental.service.DispatchServer@2.3.4-2.4.0/tf.data.experimental.service.DispatchServer#1NY/tf.data.experimental.service.DispatchServer_0_@2.3.4-2.4.0_L2_tempLst1.json` | mismatch | item 0 field (port, 0) mismatch: pred={'rename': 'config'}, gt={'delete': 1, 'replace': 'config=None'} |
| 43 | `torch/torch.btrifact@1.0.1-1.1.0/torch.btrifact#1YY/torch.btrifact_A_@1.0.1-1.1.0_L3_tempLst1.json` | mismatch | item 0 field (pivot, 2) mismatch: pred={'posChange': 1, 'replace': 'pivot'}, gt={'posChange': 1, 'replace': 'out=None'} |
| 44 | `tornado/tornado.httpclient.AsyncHTTPClient.fetch@5.1.1-6.0/tornado.httpclient.AsyncHTTPClient.fetch#1YY/http_client.fetch__http___example.com__@5.1.1-6.0_L6_tempLst1.json` | mismatch | item 0 field (raise_error, 2) mismatch: pred={'typeChange': 'bool', 'posChange': 1}, gt={'posChange': 1} |
| 45 | `tornado/tornado.iostream.BaseIOStream.read_bytes@5.1.1-6.0/tornado.iostream.BaseIOStream.read_bytes#1YY/stream.read_bytes_10_@5.1.1-6.0_L11_tempLst1.json` | mismatch | item 0 field (num_bytes, 0) mismatch: pred={'typeChange': 'int'}, gt={} |
| 46 | `transformers/transformers.modeling_albert.AlbertForPreTraining.forward@2.11.0-3.0.0/transformers.modeling_albert.AlbertForPreTraining.forward#1YY/model.forward_input_ids_@2.11.0-3.0.0_L11_tempLst1.json` | mismatch | item 0 field (output_attentions, 8) mismatch: pred={'addPos': 'output_attentions'}, gt={'addPos': 'output_attentions=None'} |
| 47 | `xgboost/predict@1.3.3-1.4.0/predict#1YY/model.predict_X_test_@1.3.3-1.4.0_L8_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=[], gt_only=['(iteration_range, 5)'] |

## 语义不相关

| 指标 | 数值 |
| --- | ---: |
| 样例数 | 113 |
| 正确 | 55 |
| 错误 | 58 |
| 正确率 | 48.67% |

### 错误样例

| 序号 | 样例路径 | 错误类型 | 差异说明 |
| --- | --- | --- | --- |
| 1 | `dask/dask.dataframe.core.drop@2.2.0-2.3.0/dask.dataframe.core.drop#1YY/ddf.drop__B___1_@2.2.0-2.3.0_L5_tempLst1.json` | mismatch | item 0 field (errors, 2) mismatch: pred={'posChange': 3, 'replace': 'columns'}, gt={'posChange': 3, 'replace': 'columns=None'} |
| 2 | `dask/dask.dataframe.drop_duplicates@2.4.0-2.5.0/dask.dataframe.drop_duplicates#1YY/ddf.drop_duplicates__@2.4.0-2.5.0_L5_tempLst1.json` | mismatch | item 0 field (split_every, 0) mismatch: pred={'posChange': 1, 'replace': 'split_every'}, gt={'posChange': 1, 'replace': 'subset=None'} |
| 3 | `flask/from_file@2.2.5-2.3.0/from_file#1YY/app.config.from_file__._test.json___json.load_@2.2.5-2.3.0_L4_tempLst1.json` | mismatch | item 0 field (load, 1) mismatch: pred={}, gt={'typeChange': 't.Callable[[t.IO[t.Any]],t.Mapping]'} |
| 4 | `gensim/gensim.models.coherencemodel.CoherenceModel@0.13.1-0.13.2/gensim.models.coherencemodel.CoherenceModel#1NN/CoherenceModel_lda_model__documents_@0.13.1-0.13.2_L8_tempLst1.json` | mismatch | item 0 field (texts, 1) mismatch: pred={'posChange': 2, 'replace': 'texts'}, gt={'posChange': 2, 'replace': 'topics=None'} |
| 5 | `gensim/gensim.models.doc2vec.Doc2Vec@3.5.0-3.6.0/gensim.models.doc2vec.Doc2Vec#1YY/Doc2Vec__@3.5.0-3.6.0_L3_tempLst1.json` | mismatch | item 0 field (dm_mean, 1) mismatch: pred={'posChange': 2, 'replace': 'corpus_file'}, gt={'posChange': 2, 'replace': 'corpus_file=None'} |
| 6 | `gensim/gensim.models.ldamodel.LdaModel.diff@2.3.0-3.0.0/gensim.models.ldamodel.LdaModel.diff#1YY/lda1.diff_lda2_@2.3.0-3.0.0_L9_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(diagonal, 4)'], gt_only=[] |
| 7 | `gensim/gensim.models.word2vec.Word2Vec.train@1.0.1-2.0.0/gensim.models.word2vec.Word2Vec.train#1NN/model.train_sentences_@1.0.1-2.0.0_L5_tempLst1.json` | mismatch | item 0 field (queue_factor, 4) mismatch: pred={'posChange': 7, 'replace': 'start_alpha'}, gt={'posChange': 7, 'replace': 'start_alpha=None'} |
| 8 | `matplotlib/matplotlib.axes.Axes.imshow@3.4.3-3.5.0/matplotlib.axes.Axes.imshow#1YY/plt.imshow_X_@3.4.3-3.5.0_L4_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=[], gt_only=['(interpolation_stage, 11)'] |
| 9 | `matplotlib/matplotlib.gridspec.GridSpec@2.1.2-2.2.0/matplotlib.gridspec.GridSpec#1YY/gridspec.GridSpec_2__2_@2.1.2-2.2.0_L3_tempLst1.json` | mismatch | item 0 field (left, 2) mismatch: pred={'posChange': 3, 'replace': 'figure'}, gt={'posChange': 3, 'replace': 'figure=None'} |
| 10 | `networkx/networkx.linalg.graphmatrix.adjacency_matrix@2.5.1-2.6/networkx.linalg.graphmatrix.adjacency_matrix#1YY/nx.adjacency_matrix_G_@2.5.1-2.6_L4_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(weight, 3)'], gt_only=[] |
| 11 | `numpy/numpy.percentile@1.21.6-1.22.0/numpy.percentile#1YY/np.percentile_a___25__50__75__@1.21.6-1.22.0_L3_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(method, 5)'], gt_only=[] |
| 12 | `numpy/numpy.quantile@1.21.6-1.22.0/numpy.quantile#1YY/np.quantile_a__q_@1.21.6-1.22.0_L9_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(method, 5)'], gt_only=[] |
| 13 | `pandas/DataFrame.ewm@1.3.5-1.4.0/DataFrame.ewm#1YY/df.ewm_0.5_@1.3.5-1.4.0_L4_tempLst1.json` | mismatch | item 0 field (times, 8) mismatch: pred={'typeChange': "'str\|np.ndarray\|DataFrame\|Series\|None'"}, gt={'typeChange': 'str\|np.ndarray\|DataFrame\|Series\|None'} |
| 14 | `pandas/DataFrame.reset_index@1.4.4-1.5.0/DataFrame.reset_index#1YY/df.reset_index__@1.4.4-1.5.0_L4_tempLst1.json` | mismatch | item 0 field (allow_duplicates, 5) mismatch: pred={'addPos': 'allow_duplicates'}, gt={'addPos': 'allow_duplicates=<no_default>'} |
| 15 | `pandas/DataFrame.rolling@1.4.4-1.5.0/DataFrame.rolling#1YY/df.rolling_2_@1.4.4-1.5.0_L4_tempLst1.json` | mismatch | item 0 field (method, 7) mismatch: pred={'posChange': 8, 'replace': 'step'}, gt={'posChange': 8, 'replace': 'step=None'} |
| 16 | `pandas/DataFrame.to_stata@1.3.5-1.4.0/DataFrame.to_stata#1YY/df.to_stata__animals.dta__@1.3.5-1.4.0_L3_tempLst1.json` | mismatch | item 0 field (path, 0) mismatch: pred={'typeChange': "'FilePath\|WriteBuffer[bytes]'"}, gt={'typeChange': 'FilePath\|WriteBuffer[bytes]'} |
| 17 | `pandas/Series.ewm@1.3.5-1.4.0/Series.ewm#1YY/df.ewm_0.5_@1.3.5-1.4.0_L4_tempLst1.json` | mismatch | item 0 field (times, 8) mismatch: pred={'typeChange': "'str\|np.ndarray\|DataFrame\|Series\|None'"}, gt={'typeChange': 'str\|np.ndarray\|DataFrame\|Series\|None'} |
| 18 | `pandas/Series.rolling@1.4.4-1.5.0/Series.rolling#1YY/df.rolling_2_@1.4.4-1.5.0_L4_tempLst1.json` | mismatch | item 0 field (method, 7) mismatch: pred={'posChange': 8}, gt={'posChange': 8, 'replace': 'step=None'} |
| 19 | `pandas/Styler.background_gradient@1.2.5-1.3.0/Styler.background_gradient#1YY/df.style.background_gradient__@1.2.5-1.3.0_L13_tempLst1.json` | mismatch | item 0 field (axis, 3) mismatch: pred={'addPos': 'axis=0'}, gt={'typeChange': 'Axis\|None'} |
| 20 | `pandas/Styler.format@1.2.5-1.3.0/Styler.format#1YY/df.style.format____.2____@1.2.5-1.3.0_L4_tempLst1.json` | mismatch | item 0 field (na_rep, 2) mismatch: pred={}, gt={'typeChange': 'str\|None'} |
| 21 | `pandas/melt@1.0.5-1.1.0/melt#1YY/pd.melt_df_@1.0.5-1.1.0_L3_tempLst1.json` | mismatch | item 0 field (frame, 0) mismatch: pred={'typeChange': "'DataFrame'"}, gt={'typeChange': 'DataFrame'} |
| 22 | `pandas/read_csv@1.2.5-1.3.0/read_csv#1YY/pd.read_csv__._dev.csv__@1.2.5-1.3.0_L2_tempLst1.json` | mismatch | item 0 field (decimal, 34) mismatch: pred={'typeChange': "'str'"}, gt={} |
| 23 | `pandas/testing.assert_frame_equal@1.0.5-1.1.0/testing.assert_frame_equal#1YY/assert_frame_equal_df1__df1_@1.0.5-1.1.0_L5_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(check_freq, 13)'], gt_only=[] |
| 24 | `plotly/plotly.express.bar@4.14.3-5.0.0/plotly.express.bar#1YY/px.bar__@4.14.3-5.0.0_L3_tempLst1.json` | mismatch | item 0 field (color, 3) mismatch: pred={'posChange': 3}, gt={} |
| 25 | `plotly/plotly.express.bar_polar@4.14.3-5.0.0/plotly.express.bar_polar#1YY/px.bar_polar__@4.14.3-5.0.0_L3_tempLst1.json` | mismatch | item 0 field (hover_name, 4) mismatch: pred={'posChange': 5, 'replace': 'pattern_shape'}, gt={'posChange': 5, 'replace': 'pattern_shape=None'} |
| 26 | `plotly/plotly.express.bar_polar@4.3.0-4.4.0/plotly.express.bar_polar#1YY/px.bar_polar__@4.3.0-4.4.0_L3_tempLst1.json` | mismatch | item 0 field (log_r, 18) mismatch: pred={'posChange': 19, 'replace': 'range_theta'}, gt={'posChange': 19, 'replace': 'range_theta=None'} |
| 27 | `plotly/plotly.express.density_contour@5.1.0-5.2.1/plotly.express.density_contour#1YY/px.density_contour__@5.1.0-5.2.1_L3_tempLst1.json` | mismatch | item 0 field (log_y, 24) mismatch: pred={'posChange': 26, 'replace': 'log_y'}, gt={'posChange': 26, 'replace': "trendline_scope='trace'"} |
| 28 | `plotly/plotly.express.density_heatmap@5.4.0-5.5.0/plotly.express.density_heatmap#1YY/px.density_heatmap__@5.4.0-5.5.0_L3_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(text_auto, 30)'], gt_only=[] |
| 29 | `plotly/plotly.express.histogram@4.14.3-5.0.0/plotly.express.histogram#1YY/px.histogram__@4.14.3-5.0.0_L3_tempLst1.json` | mismatch | item 0 field (facet_row, 4) mismatch: pred={'posChange': 5, 'replace': 'pattern_shape'}, gt={'posChange': 5, 'replace': 'pattern_shape=None'} |
| 30 | `plotly/plotly.express.histogram@4.2.1-4.3.0/plotly.express.histogram#1YY/px.histogram__@4.2.1-4.3.0_L3_tempLst1.json` | mismatch | item 0 field (facet_col, 5) mismatch: pred={'posChange': 6}, gt={} |
| 31 | `plotly/plotly.express.histogram@5.4.0-5.5.0/plotly.express.histogram#1YY/px.histogram__@5.4.0-5.5.0_L3_tempLst1.json` | mismatch | item 0 field (title, 33) mismatch: pred={'posChange': 34, 'replace': 'text_auto'}, gt={'posChange': 34, 'replace': 'text_auto=False'} |
| 32 | `plotly/plotly.express.line@5.1.0-5.2.1/plotly.express.line#1YY/px.line__@5.1.0-5.2.1_L3_tempLst1.json` | mismatch | item 0 field (hover_name, 6) mismatch: pred={'posChange': 7, 'replace': 'symbol'}, gt={'posChange': 7, 'replace': 'symbol=None'} |
| 33 | `plotly/plotly.express.line_geo@5.1.0-5.2.1/plotly.express.line_geo#1YY/px.line_geo__@5.1.0-5.2.1_L3_tempLst1.json` | mismatch | item 0 field (animation_frame, 19) mismatch: pred={'posChange': 20, 'replace': 'symbol'}, gt={'posChange': 20, 'replace': 'symbol=None'} |
| 34 | `plotly/plotly.express.line_polar@4.3.0-4.4.0/plotly.express.line_polar#1YY/px.line_polar__@4.3.0-4.4.0_L3_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(height, 29)'], gt_only=[] |
| 35 | `plotly/plotly.express.line_polar@5.1.0-5.2.1/plotly.express.line_polar#1YY/px.line_polar__@5.1.0-5.2.1_L3_tempLst1.json` | mismatch | item 0 field (animation_frame, 10) mismatch: pred={'posChange': 11, 'replace': 'symbol'}, gt={'posChange': 11, 'replace': 'symbol=None'} |
| 36 | `plotly/plotly.express.line_ternary@5.1.0-5.2.1/plotly.express.line_ternary#1YY/px.line_ternary__@5.1.0-5.2.1_L3_tempLst1.json` | mismatch | item 0 field (hover_name, 7) mismatch: pred={'posChange': 8, 'replace': 'symbol'}, gt={'posChange': 8, 'replace': 'symbol=None'} |
| 37 | `plotly/plotly.express.scatter@5.1.0-5.2.1/plotly.express.scatter#1YY/px.scatter__@5.1.0-5.2.1_L3_tempLst1.json` | mismatch | item 0 field (log_y, 38) mismatch: pred={'posChange': 40, 'replace': 'log_y'}, gt={'posChange': 40, 'replace': "trendline_scope='trace'"} |
| 38 | `plotly/plotly.express.scatter_mapbox@4.3.0-4.4.0/plotly.express.scatter_mapbox#1YY/px.scatter_mapbox_df___centroid_lat____centroid_lon__@4.3.0-4.4.0_L3_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(center, 21)', '(mapbox_style, 22)'], gt_only=[] |
| 39 | `plotly/plotly.express.scatter_polar@4.3.0-4.4.0/plotly.express.scatter_polar#1YY/px.scatter_polar__@4.3.0-4.4.0_L3_tempLst1.json` | mismatch | item 0 field (log_r, 26) mismatch: pred={'posChange': 27, 'replace': 'log_r'}, gt={'posChange': 27, 'replace': 'range_theta=None'} |
| 40 | `plotly/plotly.express.strip@4.2.1-4.3.0/plotly.express.strip#1YY/px.strip__@4.2.1-4.3.0_L3_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(facet_col_wrap, 6)'], gt_only=[] |
| 41 | `plotly/plotly.express.sunburst@4.4.1-4.5.0/plotly.express.sunburst#1YY/px.sunburst__@4.4.1-4.5.0_L3_tempLst1.json` | mismatch | item 0 field (ids, 4) mismatch: pred={'posChange': 5, 'replace': 'path'}, gt={'posChange': 5, 'replace': 'path=None'} |
| 42 | `plotly/plotly.express.violin@4.2.1-4.3.0/plotly.express.violin#1YY/px.violin__@4.2.1-4.3.0_L3_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(facet_col_wrap, 6)'], gt_only=[] |
| 43 | `polars/polars.repeat@0.17.14-0.17.15/polars.repeat#1YY/pl.repeat__z___3_@0.17.14-0.17.15_L2_tempLst1.json` | mismatch | item 0 field (value, 0) mismatch: pred={'typeChange': "'PythonLiteral\|None'"}, gt={'typeChange': 'PythonLiteral\|None'} |
| 44 | `rich/rich.syntax.Syntax.from_path@11.0.0-11.1.0/rich.syntax.Syntax.from_path#1YY/Syntax.from_path__._example.py__@11.0.0-11.1.0_L2_tempLst1.json` | mismatch | item 0 field (theme, 2) mismatch: pred={'posChange': 3, 'replace': 'lexer'}, gt={'posChange': 3, 'replace': 'lexer=None'} |
| 45 | `scipy/scipy.stats.qmc.LatinHypercube@1.9.3-1.10.0/scipy.stats.qmc.LatinHypercube#1YY/qmc.LatinHypercube_d_@1.9.3-1.10.0_L7_tempLst1.json` | mismatch | item 0 field (optimization, 4) mismatch: pred={'typeChange': "Optional[Literal[('random-cd','lloyd')]]", 'posChange': 5}, gt={'typeChange': '"Optional[Literal[(\'random-cd\',\'lloyd\')]]"'} |
| 46 | `sklearn/calibration.CalibratedClassifierCV@1.1.3-1.2.0/calibration.CalibratedClassifierCV#1YY/CalibratedClassifierCV__@1.1.3-1.2.0_L6_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(estimator, 0)'], gt_only=[] |
| 47 | `sklearn/cluster.KMeans@0.22.2-0.23.0/cluster.KMeans#1YY/KMeans_2_@0.22.2-0.23.0_L4_tempLst1.json` | mismatch | item 0 field (algorithm, 10) mismatch: pred={'posChange': 11, 'pos2key': 'algorithm'}, gt={'pos2key': 'algorithm'} |
| 48 | `sklearn/ensemble.AdaBoostClassifier@1.1.3-1.2.0/ensemble.AdaBoostClassifier#1YY/AdaBoostClassifier__@1.1.3-1.2.0_L4_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(estimator, 0)'], gt_only=[] |
| 49 | `sklearn/ensemble.AdaBoostRegressor@1.1.3-1.2.0/ensemble.AdaBoostRegressor#1YY/AdaBoostRegressor__@1.1.3-1.2.0_L4_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(estimator, 0)'], gt_only=[] |
| 50 | `sklearn/ensemble.BaggingClassifier@1.1.3-1.2.0/ensemble.BaggingClassifier#1YY/BaggingClassifier__@1.1.3-1.2.0_L5_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(estimator, 0)'], gt_only=[] |
| 51 | `sklearn/ensemble.BaggingRegressor@1.1.3-1.2.0/ensemble.BaggingRegressor#1YY/BaggingRegressor__@1.1.3-1.2.0_L5_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(estimator, 0)'], gt_only=[] |
| 52 | `sklearn/linear_model.RANSACRegressor@1.0.2-1.1.0/linear_model.RANSACRegressor#1YY/RANSACRegressor__@1.0.2-1.1.0_L5_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(estimator, 0)'], gt_only=[] |
| 53 | `sklearn/sklearn.cluster.SpectralClustering@0.21.3-0.22/sklearn.cluster.SpectralClustering#1YY/SpectralClustering_5_@0.21.3-0.22_L4_tempLst1.json` | mismatch | item 0 field (eigen_solver, 1) mismatch: pred={'posChange': 1}, gt={} |
| 54 | `sklearn/sklearn.linear_model.BayesianRidge@0.21.3-0.22/sklearn.linear_model.BayesianRidge#1YY/linear_model.BayesianRidge__@0.21.3-0.22_L2_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(alpha_init, 6)', '(lambda_init, 7)'], gt_only=[] |
| 55 | `sklearn/sklearn.linear_model.PassiveAggressiveClassifier@0.18.1-0.19.0/sklearn.linear_model.PassiveAggressiveClassifier#1YY/PassiveAggressiveClassifier__@0.18.1-0.19.0_L2_tempLst1.json` | mismatch | item 0 field (n_iter, 2) mismatch: pred={'posChange': 12, 'replace': 'max_iter'}, gt={'posChange': 12, 'replace': 'max_iter=None'} |
| 56 | `tensorflow/tf.keras.losses.SparseCategoricalCrossentropy@2.9.3-2.10.0/tf.keras.losses.SparseCategoricalCrossentropy#1YY/tf.keras.losses.SparseCategoricalCrossentropy__@2.9.3-2.10.0_L2_tempLst1.json` | mismatch | item 0 field (reduction, 1) mismatch: pred={'posChange': 2, 'replace': 'ignore_class'}, gt={'posChange': 2, 'replace': 'ignore_class=None'} |
| 57 | `tensorflow/tf.string_split@1.13.2-1.14.0/tf.string_split#1YY/tf.string_split_string_tensor_@1.13.2-1.14.0_L4_tempLst1.json` | mismatch | item 0 keys mismatch: pred_only=['(delimiter, 3)'], gt_only=[] |
| 58 | `tornado/tornado.httpclient.HTTPRequest@3.0.2-3.1/tornado.httpclient.HTTPRequest#1YY/tornado.httpclient.HTTPRequest__http___httpbin.org_get__@3.0.2-3.1_L2_tempLst1.json` | mismatch | item 0 field (connect_timeout, 6) mismatch: pred={'posChange': 7, 'replace': 'auth_mode'}, gt={'posChange': 7, 'replace': 'auth_mode=None'} |
