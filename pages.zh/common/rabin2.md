# rabin2

> 获取有关二进制文件（ELF、PE、Java CLASS、Mach-O）的信息 - 符号、节、链接的库等。
> 随 `radare2` 一起分发。
> 更多信息：<https://manned.org/rabin2>.

- 显示二进制文件的概要信息（架构、类型、字节序）：

`rabin2 -I {{path/to/binary}}`

- 显示链接的库：

`rabin2 -l {{path/to/binary}}`

- 显示从库导入的符号：

`rabin2 -i {{path/to/binary}}`

- 显示二进制文件中包含的字符串：

`rabin2 -z {{path/to/binary}}`

- 以 JSON 格式显示输出：

`rabin2 -j -I {{path/to/binary}}`