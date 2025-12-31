# clang

> Compile C, C++, and Objective-C source files. Can be used as a drop-in replacement for GCC.
> Part of LLVM.
> More information: <https://clang.llvm.org/docs/ClangCommandLineReference.html>.

- Compile multiple source files into an executable:

`clang {{path/to/source1.c path/to/source2.c ...}} {{[-o|--output]}} {{path/to/output_executable}}`

- Activate output of all errors and warnings:

`clang {{path/to/source.c}} -Wall {{[-o|--output]}} {{output_executable}}`

- Show common warnings, debug symbols in output, and optimize without affecting debugging:

`clang {{path/to/source.c}} -Wall {{[-g|--debug]}} -Og {{[-o|--output]}} {{path/to/output_executable}}`

- Include libraries from a different path:

`clang {{path/to/source.c}} {{[-o|--output]}} {{path/to/output_executable}} -I{{path/to/header}} -L{{path/to/library}} -l{{library_name}}`

- Compile source code into LLVM Intermediate Representation (IR):

`clang {{[-S|--assemble]}} -emit-llvm {{path/to/source.c}} {{[-o|--output]}} {{path/to/output.ll}}`

- Compile source code into an object file without linking:

`clang {{[-c|--compile]}} {{path/to/source.c}}`

- Optimize the compiled program for performance:

`clang {{path/to/source.c}} -O{{1|2|3|fast}} {{[-o|--output]}} {{path/to/output_executable}}`

- Display version:

`clang --version`
