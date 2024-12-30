# zek

> 从 XML 生成 Go 结构体。
> 更多信息：<https://github.com/miku/zek>。

- 从 `stdin` 中给定的 XML 生成 Go 结构体，并在 `stdout` 上显示输出：

`cat {{path/to/input.xml}} | zek`

- 从 `stdin` 中给定的 XML 生成 Go 结构体，并将输出发送到文件：

`curl -s {{https://url/to/xml}} | zek -o {{path/to/output.go}}`

- 从 `stdin` 中给定的 XML 生成示例 Go 程序，并将输出发送到文件：

`cat {{path/to/input.xml}} | zek -p -o {{path/to/output.go}}`