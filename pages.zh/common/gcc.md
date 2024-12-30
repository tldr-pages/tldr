# gcc

> 预处理和编译 C 和 C++ 源文件，然后将它们汇编和链接在一起。
> 是 GCC（GNU 编译器集合）的一部分。
> 更多信息：<https://gcc.gnu.org>。

- 将多个源文件编译为可执行文件：

`gcc {{path/to/source1.c path/to/source2.c ...}} {{-o|--output}} {{path/to/output_executable}}`

- 激活所有错误和警告的输出：

`gcc {{path/to/source.c}} -Wall {{-o|--output}} {{output_executable}}`

- 显示常见警告，输出调试符号，并在不影响调试的情况下优化：

`gcc {{path/to/source.c}} -Wall {{-g|--debug}} -Og {{-o|--output}} {{path/to/output_executable}}`

- 从不同路径包含库：

`gcc {{path/to/source.c}} {{-o|--output}} {{path/to/output_executable}} -I{{path/to/header}} -L{{path/to/library}} -l{{library_name}}`

- 将源代码编译为汇编指令：

`gcc {{-S|--assemble}} {{path/to/source.c}}`

- 将源代码编译为目标文件而不链接：

`gcc {{-c|--compile}} {{path/to/source.c}}`

- 为性能优化已编译的程序：

`gcc {{path/to/source.c}} -O{{1|2|3|fast}} {{-o|--output}} {{path/to/output_executable}}`

- 显示版本：

`gcc --version`