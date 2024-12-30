# xargs

> 使用来自另一个命令、文件等的管道参数执行命令。
> 输入被视为一个单一的文本块，并在空格、制表符、换行符和文件结尾处分割成单独的部分。
> 更多信息：<https://pubs.opengroup.org/onlinepubs/9699919799/utilities/xargs.html>。

- 使用输入数据作为参数运行命令：

`{{arguments_source}} | xargs {{command}}`

- 对输入数据运行多个链式命令：

`{{arguments_source}} | xargs sh -c "{{command1}} && {{command2}} | {{command3}}"`

- 使用多线程对所有扩展名为 `.log` 的文件进行 gzip 压缩（`-print0` 使用空字符分割文件名，`-0` 将其作为分隔符）：

`find . -name '*.log' -print0 | xargs -0 -P {{4}} -n 1 gzip`

- 每个参数执行一次命令：

`{{arguments_source}} | xargs -n1 {{command}}`

- 每行输入执行一次命令，用输入行替换占位符（此处标记为 `_`）的任何出现：

`{{arguments_source}} | xargs -I _ {{command}} _ {{optional_extra_arguments}}`

- 同时运行最多 `max-procs` 个进程；默认值为 1。如果 `max-procs` 为 0，xargs 将尽可能多地同时运行进程：

`{{arguments_source}} | xargs -P {{max-procs}} {{command}}`