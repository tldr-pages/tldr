# coredumpctl

> 检索和处理保存的核心转储和元数据。
> 更多信息: <https://www.freedesktop.org/software/systemd/man/coredumpctl.html>。

- 列出所有捕获的核心转储：

`coredumpctl list`

- 列出某个程序的捕获核心转储：

`coredumpctl list {{program}}`

- 显示与某个程序的 `PID` 匹配的核心转储信息：

`coredumpctl info {{PID}}`

- 使用某个程序的最后一个核心转储调用调试器：

`coredumpctl debug {{program}}`

- 将某个程序的最后一个核心转储提取到文件中：

`coredumpctl --output={{path/to/file}} dump {{program}}`