# script

> 记录所有终端输出到一个 typescript 文件。
> 更多信息：<https://manned.org/script>.

- 记录新会话到当前目录中的名为 `typescript` 的文件：

`script`

- 停止记录：

`exit`

- 记录新会话到自定义文件路径：

`script {{path/to/session.out}}`

- 追加到现有文件：

`script {{[-a|--append]}} {{logfile.log}}`

- 记录时间信息（数据输出到 `stderr`）：

`script {{[-t|--timing]}} 2> {{path/to/timing_file}}`

- 立即写入数据：

`script {{[-f|--flush]}} {{path/to/file}}`

- 静默执行，不显示开始和结束消息：

`script {{[-q|--quiet]}} {{logfile.log}}`

- 显示帮助：

`script {{[-h|--help]}}`
