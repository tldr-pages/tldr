# addr2line

> 将二进制文件的地址转换为文件名和行号。
> 更多信息：<https://manned.org/addr2line>。

- 从可执行文件的指令地址显示源代码的文件名和行号：

`addr2line --exe={{path/to/executable}} {{address}}`

- 显示函数名、文件名和行号：

`addr2line --exe={{path/to/executable}} --functions {{address}}`

- 对C++代码的函数名进行解码：

`addr2line --exe={{path/to/executable}} --functions --demangle {{address}}`