# xargs

> 使用管道从另一个命令、文件等传递的参数执行命令。
> 输入被视为单个文本块，并在空格、制表符、换行符和文件结束处分割成单独的部分。
> 更多信息：<https://pubs.opengroup.org/onlinepubs/9699919799/utilities/xargs.html>。

- 使用输入数据作为参数运行命令：

`{{arguments_source}} | xargs {{command}}`

- 在输入数据上运行多个链式命令：

`{{arguments_source}} | xargs sh -c "{{command1}} && {{command2}} | {{command3}}"`

- 利用多线程压缩所有带有 `.log` 扩展名的文件（`-print0` 使用空字符分割文件名，`-0` 使用空字符作为分隔符）：

`find . -name '*.log' -print0 | xargs {{[-0|--null]}} {{[-P|--max-procs]}} {{4}} {{[-n|--max-args]}} 1 gzip`

- 每个参数执行一次命令：

`{{arguments_source}} | xargs {{-n|--max-args}} 1 {{command}}`

- 每行输入执行一次命令，用占位符（这里标记为 `_`）替换输入行：

`{{arguments_source}} | xargs -I _ {{command}} _ {{optional_extra_arguments}}`

- 并行运行最多 `max-procs` 个进程；默认值为 1。如果 `max-procs` 为 0，xargs 将同时运行尽可能多的进程：

`{{arguments_source}} | xargs {{[-P|--max-procs]}} {{max-procs}} {{command}}`
