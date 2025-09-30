# qalc

> 强大且易用的命令行计算器。
> 请参阅：`bc`。
> 更多信息：<https://qalculate.github.io/manual/qalc.html>.

- 以交互模式启动：

`qalc {{--interactive}}`

- 以简洁模式启动（仅输出结果）：

`qalc --terse`

- 更新货币兑换率：

`qalc --exrates`

- 非交互地执行计算：

`qalc {{66+99|2^4|6 feet to cm|1 bitcoin to USD|20 kmph to mph|...}}`

- 列出所有支持的函数/前缀/单位/变量：

`qalc --{{list-functions|list-prefixes|list-units|list-variables}}`

- 从文件中执行命令：

`qalc --file {{路径/到/文件}}`
