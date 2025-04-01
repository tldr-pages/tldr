# abrt-action-analyze-backtrace

> 分析 C/C++ 回溯信息。
> 生成重复哈希、回溯评分，并识别崩溃函数。
> 将数据保存为问题目录中的新元素 `duphash`、`rating`、`crash_function`。
> 更多信息：<https://manned.org/abrt-action-analyze-backtrace>。

- 分析当前工作目录的回溯信息：

`abrt-action-analyze-backtrace`

- 分析特定目录的回溯信息：

`abrt-action-analyze-backtrace -d {{path/to/directory}}`

- 详细分析回溯信息：

`abrt-action-analyze-backtrace -v`
