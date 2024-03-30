# clang++

> Compiles C++ source files.
> Part of LLVM.
> More information: <https://clang.llvm.org>.

- Compile a source code file into an executable binary:

`clang++ {{path/to/source.cpp}} -o {{path/to/output_executable}}`

- Display (almost) all errors and warnings:

`clang++ {{path/to/source.cpp}} -Wall -o {{path/to/output_executable}}`

- Choose a language standard to compile with:

`clang++ {{path/to/source.cpp}} -std={{c++20}} -o {{path/to/output_executable}}`

- Include libraries located at a different path than the source file:

`clang++ {{path/to/source.cpp}} -o {{path/to/output_executable}} -I{{path/to/header_path}} -L{{path/to/library_path}} -l{{path/to/library_name}}`

- Compile source code into LLVM Intermediate Representation (IR):

`clang++ -S -emit-llvm {{path/to/source.cpp}} -o {{path/to/output.ll}}`

- Optimize the compiled program for performance:

`clang++ {{path/to/source.cpp}} -O{{1|2|3|fast}} -o {{path/to/output_executable}}`
