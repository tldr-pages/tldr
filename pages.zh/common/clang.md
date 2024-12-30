# clang

> 编译 C、C++ 和 Objective-C 源文件。可以作为 GCC 的直接替代品。
> 是 LLVM 的一部分。
> 更多信息：<https://clang.llvm.org/docs/ClangCommandLineReference.html>。

- 将多个源文件编译为可执行文件：

`clang {{path/to/source1.c path/to/source2.c ...}} {{-o|--output}} {{path/to/output_executable}}`

- 激活所有错误和警告的输出：

`clang {{path/to/source.c}} -Wall {{-o|--output}} {{output_executable}}`

- 显示常见警告，输出调试符号，并在不影响调试的情况下优化：

`clang {{path/to/source.c}} -Wall {{-g|--debug}} -Og {{-o|--output}} {{path/to/output_executable}}`

- 从不同路径包含库：

`clang {{path/to/source.c}} {{-o|--output}} {{path/to/output_executable}} -I{{path/to/header}} -L{{path/to/library}} -l{{library_name}}`

- 将源代码编译为 LLVM 中间表示 (IR)：

`clang {{-S|--assemble}} -emit-llvm {{path/to/source.c}} {{-o|--output}} {{path/to/output.ll}}`

- 将源代码编译为目标文件而不链接：

`clang {{-c|--compile}} {{path/to/source.c}}`

- 针对性能优化已编译的程序：

`clang {{path/to/source.c}} -O{{1|2|3|fast}} {{-o|--output}} {{path/to/output_executable}}`

- 显示版本：

`clang --version`