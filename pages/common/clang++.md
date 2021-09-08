# clang++

> Compiles C++ source files.
> Part of LLVM.
> More information: <https://clang.llvm.org>.

- Compile a source code file into an executable binary:

`clang++ {{source.cpp}} -o {{output_executable}}`

- Display (almost) all errors and warnings:

`clang++ {{source.cpp}} -Wall -o {{output_executable}}`

- Choose a language standard to compile for:

`clang++ {{source.cpp}} -std={{c++20}} -o {{output_executable}}`

- Include libraries located at a different path than the source file:

`clang++ {{source.cpp}} -o {{output_executable}} -I{{header_path}} -L{{library_path}} -l{{library_name}}`

- Compile source code into LLVM Intermediate Representation (IR):

`clang++ -S -emit-llvm {{source.cpp}} -o {{output.ll}}`
