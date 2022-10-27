# go build

> 编译 Go 源代码。
> 更多信息：<https://golang.org/cmd/go/#hdr-Compile_packages_and_dependencies>.

- 编译‘package main’文件（输出为不带扩展名的文件名）：

`go build {{路径/到/main.go}}`

- 编译，并指定输出文件名：

`go build -o {{路径/到/二进制文件}} {{路径/到/源文件.go}}`

- 编译一个包：

`go build -o {{路径/到/二进制文件}} {{路径/到/包}}`

- 编译 main 包为可执行文件，并开启数据竞态检测：

`go build -race -o {{路径/到/可执行文件}} {{路径/到/main/包}}`
