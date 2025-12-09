# addr2line

> 将二进制文件地址转换成文件名和行数。
> 更多信息：<https://manned.org/addr2line>.

- 显示可执行文件的指令地址对应源代码的文件名和行数：

`addr2line --exe={{可执行文件路径}} {{地址}}`

- 显示函数名、文件名和行数：

`addr2line --exe={{可执行文件路径}} --functions {{地址}}`

- 将 C++ 代码函数名符号重组：

`addr2line --exe={{可执行文件地址}} --functions --demangle {{地址}}`
