# objdump

> 查看目标文件的信息。
> 更多信息：<https://manned.org/objdump>.

- 显示文件头信息：

`objdump -f {{path/to/binary}}`

- 显示所有头信息：

`objdump -x {{path/to/binary}}`

- 显示可执行部分的反汇编输出：

`objdump -d {{path/to/binary}}`

- 使用 Intel 语法显示可执行部分的反汇编输出：

`objdump -M intel -d {{path/to/binary}}`

- 显示所有部分的完整二进制十六进制转储：

`objdump -s {{path/to/binary}}`