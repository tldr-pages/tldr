# indent

> 通过插入或删除空白来改变 C/C++ 程序的外观。
> 更多信息：<https://www.gnu.org/software/indent/manual/indent/Option-Summary.html>。

- 根据 Linux 风格指南格式化 C/C++ 源代码，自动备份原始文件，并用缩进后的版本替换：

`indent {{[-linux|--linux-style]}} {{path/to/source.c}} {{path/to/another_source.c}}`

- 根据 GNU 风格格式化 C/C++ 源代码，并将缩进后的版本保存到不同的文件：

`indent {{[-gnu|--gnu-style]}} {{path/to/source.c}} -o {{path/to/indented_source.c}}`

- 根据 Kernighan & Ritchie (K&R) 风格格式化 C/C++ 源代码，不使用制表符，每级缩进 3 个空格，并在 120 个字符处换行：

`indent {{[-kr|--k-and-r-style]}} {{[-il|--indent-level]}}3 {{[-nut|--no-tabs]}} {{[-l|--line-length]}}120 {{path/to/source.c}} -o {{path/to/indented_source.c}}`
