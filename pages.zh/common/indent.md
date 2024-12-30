# indent

> 通过插入或删除空格来改变 C/C++ 程序的外观。
> 更多信息：<https://www.gnu.org/software/indent/>.

- 根据 Linux 风格指南格式化 C/C++ 源文件，自动备份原始文件，并用缩进版本替换：

`indent --linux-style {{path/to/source.c}} {{path/to/another_source.c}}`

- 根据 GNU 风格格式化 C/C++ 源文件，将缩进版本保存到不同的文件中：

`indent --gnu-style {{path/to/source.c}} -o {{path/to/indented_source.c}}`

- 根据 Kernighan & Ritchie (K&R) 风格格式化 C/C++ 源文件，不使用制表符，缩进 3 个空格，并在 120 个字符处换行：

`indent --k-and-r-style --indent-level3 --no-tabs --line-length120 {{path/to/source.c}} -o {{path/to/indented_source.c}}`