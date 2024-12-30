# nm

> 列出目标文件中的符号名称。
> 更多信息：<https://manned.org/nm>。

- 列出文件中的全局（外部）函数（以 T 为前缀）：

`nm -g {{path/to/file.o}}`

- 仅列出文件中的未定义符号：

`nm -u {{path/to/file.o}}`

- 列出所有符号，甚至调试符号：

`nm -a {{path/to/file.o}}`

- 解码 C++ 符号（使其可读）：

`nm --demangle {{path/to/file.o}}`