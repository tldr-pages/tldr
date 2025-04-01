# gcc

> 预处理、编译 C 和 C++ 源文件，然后汇编并将它们链接在一起。
> 属于 GCC（GNU 编译器集合）的一部分。
> 更多信息：<https://gcc.gnu.org>。

- 编译多个源文件生成一个可执行文件：

`gcc {{path/to/source1.c path/to/source2.c ...}} {{[-o|--output]}} {{path/to/output_executable}}`

- 激活所有错误和警告的输出：

`gcc {{path/to/source.c}} -Wall {{[-o|--output]}} {{output_executable}}`

- 显示常见警告、在输出中包含调试符号，并优化而不影响调试：

`gcc {{path/to/source.c}} -Wall {{[-g|--debug]}} -Og {{[-o|--output]}} {{path/to/output_executable}}`

- 从不同的路径包含库：

`gcc {{path/to/source.c}} {{[-o|--output]}} {{path/to/output_executable}} -I{{path/to/header}} -L{{path/to/library}} -l{{library_name}}`

- 将源代码编译成汇编指令：

`gcc {{[-S|--assemble]}} {{path/to/source.c}}`

- 编译源代码生成目标文件但不进行链接：

`gcc {{[-c|--compile]}} {{path/to/source.c}}`

- 优化编译后的程序以提高性能：

`gcc {{path/to/source.c}} -O{{1|2|3|fast}} {{[-o|--output]}} {{path/to/output_executable}}`

- 显示版本：

`gcc --version`
