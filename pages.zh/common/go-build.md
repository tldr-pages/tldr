# go build

> 编译 Go 源代码。
> 更多信息：<https://golang.org/cmd/go/#hdr-Compile_packages_and_dependencies>。

- 编译一个 'package main' 文件（输出将是没有扩展名的文件名）：

`go build {{path/to/main.go}}`

- 编译，指定输出文件名：

`go build -o {{path/to/binary}} {{path/to/source.go}}`

- 编译一个包：

`go build -o {{path/to/binary}} {{path/to/package}}`

- 编译一个主包为可执行文件，并启用数据竞争检测：

`go build -race -o {{path/to/executable}} {{path/to/main/package}}`