# clang

> 编译 C、C++ 和 Objective-C 源文件。可以用作 GCC 的替代品。
> 是 LLVM 的一部分。
> 更多信息：<https://clang.llvm.org/docs/ClangCommandLineReference.html>.

- 编译多个源文件为可执行文件：

`clang {{path/to/source1.c path/to/source2.c ...}} {{[-o|--output]}} {{path/to/output_executable}}`

- 激活所有错误和警告的输出：

`clang {{path/to/source.c}} -Wall {{[-o|--output]}} {{output_executable}}`

- 显示常见警告，在输出中包含调试符号，并优化但不影响调试：

`clang {{path/to/source.c}} -Wall {{[-g|--debug]}} -Og {{[-o|--output]}} {{path/to/output_executable}}`

- 包括来自不同路径的库：

`clang {{path/to/source.c}} {{[-o|--output]}} {{path/to/output_executable}} -I{{path/to/header}} -L{{path/to/library}} -l{{library_name}}`

- 将源代码编译为 LLVM 中间表示 (IR)：

`clang {{[-S|--assemble]}} -emit-llvm {{path/to/source.c}} {{[-o|--output]}} {{path/to/output.ll}}`

- 编译源代码为对象文件而不进行链接：

`clang {{[-c|--compile]}} {{path/to/source.c}}`

- 优化编译的程序以提高性能：

`clang {{path/to/source.c}} -O{{1|2|3|fast}} {{[-o|--output]}} {{path/to/output_executable}}`

- 显示版本：

`clang --version`