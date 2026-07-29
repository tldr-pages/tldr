# nice

> 以自定义的调度优先级（niceness）执行程序。
> Niceness 值范围从 -20（最高优先级）到 19（最低优先级）。
> 注意：某些现代调度器会忽略 niceness 或限制其在 autogroups 内的效果。
> 更多信息：<https://www.gnu.org/software/coreutils/manual/html_node/nice-invocation.html>。

- 打印当前 niceness 值：

`nice`

- 将当前 niceness 值增加 10：

`nice nice`

- 以降低的优先级启动程序：

`nice -{{niceness_值}} {{命令}}`

- 以提高的优先级启动程序：

`sudo nice --{{niceness_值}} {{命令}}`

- 使用显式选项定义优先级：

`nice {{[-n|--adjustment]}} {{niceness_值}} {{命令}}`
