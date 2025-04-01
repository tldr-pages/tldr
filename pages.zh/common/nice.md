# nice

> 以自定义的调度优先级（niceness）执行程序。
> 优先级范围从 -20（最高优先级）到 19（最低优先级）。
> 更多信息：<https://www.gnu.org/software/coreutils/manual/html_node/nice-invocation.html>.

- 以更改的优先级启动程序：

`nice -{{niceness_value}} {{command}}`

- 使用明确的选项定义优先级：

`nice {{[-n|--adjustment]}} {{niceness_value}} {{command}}`
