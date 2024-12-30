# strip

> 从可执行文件或目标文件中丢弃符号。
> 更多信息：<https://manned.org/strip>。

- 用剥离过的版本替换输入文件：

`strip {{path/to/file}}`

- 从文件中剥离符号，并将输出保存到特定文件：

`strip {{path/to/input_file}} -o {{path/to/output_file}}`

- 仅剥离调试符号：

`strip --strip-debug {{path/to/file.o}}`