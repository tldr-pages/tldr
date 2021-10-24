# clang

> Compiler for C, C++, and Objective-C source files. Can be used as a drop-in replacement for GCC.
> More information: <https://clang.llvm.org/docs/ClangCommandLineReference.html>.

- Compile a source code file into an executable binary:

`clang {{input_source.c}} -o {{output_executable}}`

- Activate output of all errors and warnings:

`clang {{input_source.c}} -Wall -o {{output_executable}}`

- Include libraries located at a different path than the source file:

`clang {{input_source.c}} -o {{output_executable}} -I{{header_path}} -L{{library_path}} -l{{library_name}}`

- Compile source code into LLVM Intermediate Representation (IR):

`clang -S -emit-llvm {{file.c}} -o {{file.ll}}`

- Compile source code without linking:

`clang -c {{input_source.c}}`
