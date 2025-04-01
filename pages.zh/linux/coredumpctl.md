# coredumpctl

> 检索并处理保存的核心转储和元数据。
> 更多信息：<https://www.freedesktop.org/software/systemd/man/coredumpctl.html>.

- 列出所有捕获的核心转储：

`coredumpctl`

- 列出指定程序的捕获核心转储：

`coredumpctl list {{program}}`

- 显示与指定 `PID` 程序匹配的核心转储信息：

`coredumpctl info {{PID}}`

- 使用最新的核心转储调用调试器：

`coredumpctl debug`

- 使用指定程序的最新核心转储调用调试器：

`coredumpctl debug {{program}}`

- 将指定程序的最新核心转储提取到文件中：

`coredumpctl --output {{path/to/file}} dump {{program}}`

- 跳过 debuginfod 和分页提示，并在使用 `gdb` 时打印回溯信息：

`coredumpctl debug --debugger-arguments "-iex 'set debuginfod enabled on' -iex 'set pagination off' -ex bt"`