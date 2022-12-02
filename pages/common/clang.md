# clang

> Compiler for C, C++, and Objective-C source files. Can be used as a drop-in replacement for GCC.
> More information: <https://clang.llvm.org/docs/ClangCommandLineReference.html>.

- Compile a source code file into an executable binary:

`clang {{path/to/source.c}} -o {{path/to/executable}}`

- Activate output of all errors and warnings:

`clang {{path/to/source.c}} -Wall -o {{path/to/executable}}`

- Include libraries located at a different path than the source file:

`clang {{path/to/source.c}} -o {{path/to/executable}} -I{{header_path}} -L{{library_path}} -l{{library_name}}`

- Compile source code into LLVM Intermediate Representation (IR):

`clang -S -emit-llvm {{path/to/file.c}} -o {{path/to/file.ll}}`

- Compile source code without linking:

`clang -c {{path/to/source.c}}`
