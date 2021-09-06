# logsave

> 将一个命令的输出保存在日志文件中。
> 更多信息：<https://manned.org/logsave>.

- 使用指定的参数执行命令并将其输出保存到日志文件中：

`logsave {{path/to/logfile}} {{command}}`

- 从标准输入中获取输入并将其保存在日志文件中：

`logsave {{logfile}} -`

- 将输出追加到日志文件，而不是替换其当前内容：

`logsave -a {{logfile}} {{command}}`

- 显示详细输出：

`logsave -v {{logfile}} {{command}}`
