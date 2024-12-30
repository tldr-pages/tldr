# logsave

> 将命令的输出保存到日志文件中。
> 更多信息：<https://manned.org/logsave>。

- 使用指定的参数执行命令，并将其输出保存到日志文件中：

`logsave {{path/to/logfile}} {{command}}`

- 从 `stdin` 获取输入并将其保存到日志文件中：

`logsave {{logfile}} -`

- 将输出附加到日志文件，而不是替换其当前内容：

`logsave -a {{logfile}} {{command}}`

- 显示详细输出：

`logsave -v {{logfile}} {{command}}`