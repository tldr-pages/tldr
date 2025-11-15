# clang

> 编译 C，C++ 以及 Objective-C 源文件。可以无缝替代 GCC。
> LLVM 项目的组件之一。
> 更多信息：<https://clang.llvm.org/docs/ClangCommandLineReference.html>.

- 将多个文件编译为可执行文件：

`clang {{源/文件/的路径1.c 源/文件/的路径2.c ...}} {{[-o|--output]}} {{可执行/文件/的路径}}`

- 打印所有错误和警告：

`clang {{源/文件/的路径.c}} -Wall {{[-o|--output]}} {{可执行文件}}`

- 打印普通警告和调试信息, 并在不影响调试的情况下优化：

`clang {{源/文件/的路径.c}} -Wall {{[-g|--debug]}} -Og {{[-o|--output]}} {{可执行/文件/的路径}}`

- 包含与源文件不在同一路径下的库：

`clang {{源/文件/的路径.c}} {{[-o|--output]}} {{可执行/文件/的路径}} -I{{头/文件/的目录}} -L{{库/的目录}} -l{{库的名字}}`

- 将源文件编译为 LLVM 中间表示（IR）：

`clang {{[-S|--assemble]}} -emit-llvm {{源/文件/的路径.c}} {{[-o|--output]}} {{IR/的/路径.ll}}`

- 将源文件编译成目标文件（.o）而不链接：

`clang {{[-c|--compile]}} {{源/文件/的路径1.c 源/文件/的路径2.c...}}`

- 优化编译后程序的性能:

`clang {{源/文件/的路径.c}} -O{{1|2|3|fast}} {{[-o|--output]}} {{可执行/文件/的路径}}`

- 打印版本信息：

`clang --version`
