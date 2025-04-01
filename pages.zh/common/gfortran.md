# gfortran

> 预处理和编译 Fortran 源文件，然后将它们汇编并链接在一起。
> 更多信息：<https://gcc.gnu.org/wiki/GFortran>。

- 将多个源文件编译成可执行文件：

`gfortran {{path/to/source1.f90 path/to/source2.f90 ...}} -o {{path/to/output_executable}}`

- 显示常见警告，输出中包含调试符号，并优化而不影响调试：

`gfortran {{path/to/source.f90}} -Wall -g -Og -o {{path/to/output_executable}}`

- 从不同的路径包含库：

`gfortran {{path/to/source.f90}} -o {{path/to/output_executable}} -I{{path/to/mod_and_include}} -L{{path/to/library}} -l{{library_name}}`

- 将源代码编译成汇编指令：

`gfortran -S {{path/to/source.f90}}`

- 将源代码编译成对象文件但不链接：

`gfortran -c {{path/to/source.f90}}`