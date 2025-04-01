# clang++

> 编译 C++ 源文件。
> 属于 LLVM 项目。
> 更多信息：<https://clang.llvm.org>。

- 将一组源代码文件编译成可执行二进制文件：

`clang++ {{path/to/source1.cpp path/to/source2.cpp ...}} {{[-o|--output]}} {{path/to/output_executable}}`

- 激活所有错误和警告的输出：

`clang++ {{path/to/source.cpp}} -Wall {{[-o|--output]}} {{output_executable}}`

- 显示常见的警告，输出调试符号，并进行不影响调试的优化：

`clang++ {{path/to/source.cpp}} -Wall {{[-g|--debug]}} -Og {{[-o|--output]}} {{path/to/output_executable}}`

- 选择一个语言标准进行编译：

`clang++ {{path/to/source.cpp}} -std={{c++20}} {{[-o|--output]}} {{path/to/output_executable}}`

- 包含位于不同于源文件路径的库：

`clang++ {{path/to/source.cpp}} {{[-o|--output]}} {{path/to/output_executable}} -I{{path/to/header_path}} -L{{path/to/library_path}} -l{{path/to/library_name}}`

- 将源代码编译成 LLVM 中间表示 (IR)：

`clang++ {{[-S|--assemble]}} -emit-llvm {{path/to/source.cpp}} {{[-o|--output]}} {{path/to/output.ll}}`

- 为性能优化编译的程序：

`clang++ {{path/to/source.cpp}} -O{{1|2|3|fast}} {{[-o|--output]}} {{path/to/output_executable}}`

- 显示版本：

`clang++ --version`