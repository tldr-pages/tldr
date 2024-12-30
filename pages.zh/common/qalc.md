# qalc

> 强大且易于使用的命令行计算器。
> 另见：`bc`。
> 更多信息：<https://qalculate.github.io/manual/qalc.html>。

- 以交互模式启动：

`qalc {{--interactive}}`

- 以简洁模式启动（仅打印结果）：

`qalc --terse`

- 更新货币汇率：

`qalc --exrates`

- 非交互式地进行计算：

`qalc {{66+99|2^4|6英尺到厘米|1比特币到美元|20公里每小时到英里每小时|...}}`

- 列出所有支持的函数/前缀/单位/变量：

`qalc --{{list-functions|list-prefixes|list-units|list-variables}}`

- 从文件中执行命令：

`qalc --file {{path/to/file}}`