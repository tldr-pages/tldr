# nim

> Nim 编译器。
> 处理、编译和链接 Nim 语言源文件。
> 更多信息：<https://nim-lang.org/docs/nimc.html>。

- 编译源文件：

`nim compile {{path/to/file.nim}}`

- 编译并运行源文件：

`nim compile -r {{path/to/file.nim}}`

- 编译源文件并启用发布优化：

`nim compile -d:release {{path/to/file.nim}}`

- 构建优化以减少文件大小的发布二进制文件：

`nim compile -d:release --opt:size {{path/to/file.nim}}`

- 为模块生成 HTML 文档（输出将放置在当前目录中）：

`nim doc {{path/to/file.nim}}`

- 检查文件的语法和语义：

`nim check {{path/to/file.nim}}`
