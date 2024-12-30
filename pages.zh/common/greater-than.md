# 大于

> 将输出重定向到文件。
> 更多信息：<https://gnu.org/software/bash/manual/bash.html#Redirecting-Output>。

- 将 `stdout` 重定向到文件：

`{{command}} > {{path/to/file}}`

- 附加到文件：

`{{command}} >> {{path/to/file}}`

- 将 `stdout` 和 `stderr` 都重定向到文件：

`{{command}} &> {{path/to/file}}`

- 将 `stderr` 重定向到 `/dev/null` 以保持终端输出干净：

`{{command}} 2> /dev/null`

- 清空文件内容或创建一个新的空文件：

`> {{path/to/file}}`