# nm

> 列出目标文件中的符号名称。
> 更多信息：<https://manned.org/nm>。

- 列出文件中的全局（外部）函数（以 T 开头）：

`nm -g {{path/to/file.o}}`

- 列出文件中仅未定义的符号：

`nm -u {{path/to/file.o}}`

- 列出所有符号，包括调试符号：

`nm -a {{path/to/file.o}}`

- 解析 C++ 符号（使其可读）：

`nm --demangle {{path/to/file.o}}`