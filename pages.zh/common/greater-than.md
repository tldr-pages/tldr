# 输出重定向

> 将输出重定向到文件。
> 更多信息：<https://gnu.org/software/bash/manual/bash.html#Redirecting-Output>.

- 将标准输出重定向到文件：

`{{command}} > {{path/to/file}}`

- 将输出追加到文件：

`{{command}} >> {{path/to/file}}`

- 将标准输出和标准错误输出重定向到文件：

`{{command}} &> {{path/to/file}}`

- 将标准错误输出重定向到 `/dev/null` 以保持终端输出干净：

`{{command}} 2> /dev/null`

- 清空文件内容或创建一个新空文件：

`> {{path/to/file}}`
