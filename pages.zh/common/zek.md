# zek

> 从 XML 生成一个 Go 结构体。
> 更多信息：<https://github.com/miku/zek#usage>.

- 从 `stdin` 中给定的 XML 生成一个 Go 结构体，并将输出显示在 `stdout` 上：

`cat {{路径/到/输入.xml}} | zek`

- 从 `stdin` 中给定的 XML 生成一个 Go 结构体，并将输出发送到文件：

`curl -s {{https://url/to/xml}} | zek -o {{路径/到/输出.go}}`

- 从 `stdin` 中给定的 XML 生成一个示例 Go 程序，并将输出发送到文件：

`cat {{路径/到/输入.xml}} | zek -p -o {{路径/到/输出.go}}`
