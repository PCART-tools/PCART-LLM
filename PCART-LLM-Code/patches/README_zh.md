# main.diff 说明

语言 / Language: **中文** | [English](README.md)

本目录根下对应的补丁文件是 [main.diff](./main.diff)。它描述的是 [PCART-original/main.py](../PCART-original/main.py) 到 [PCART-modified/main.py](../PCART-modified/main.py) 的差异。

## 补丁覆盖内容

- 在调用 `isCompatible()` 之前补充构造 `context`，把 `apiCall`、旧新版本号、匹配结果、`jsonPrefix`、配置路径等额外信息一起透传下去。
- 将报告输出从单一 `Report/` 扩展为同时归档到 `Log/Report/{subDir}/`。
- 将错误日志输出从单一 `Report/{projName}_fixed_log.txt` 扩展为同步写入 `Log/findDiffer/{subDir}/`。

## 补丁意义

- 让 `main.py` 成为默认规则模式与 LLM 模式的统一入口。
- 让结果与错误日志按配置目录分层保存，更适合批量实验与问题回溯。
