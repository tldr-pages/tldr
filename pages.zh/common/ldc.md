# ldc

> 使用 LLVM 作为后端的 D 语言编译器。
> 更多信息：<https://wiki.dlang.org/Using_LDC>。

- 将源代码文件编译为可执行二进制文件：

`ldc2 {{path/to/source.d}} -of={{path/to/output_executable}}`

- 编译源代码文件但不进行链接：

`ldc2 -c {{path/to/source.d}}`

- 选择目标架构和操作系统：

`ldc -mtriple={{architecture_OS}} -c {{path/to/source.d}}`

- 显示帮助信息：

`ldc2 -h`

- 显示完整帮助信息：

`ldc2 -help-hidden`