# clang++

> Compile C++ source files.
> Part of LLVM.
> More information: <https://clang.llvm.org/docs/UsersManual.html#command-line-options>.

- Compile a set of source code files into an executable binary:

`clang++ {{path/to/source1.cpp path/to/source2.cpp ...}} {{[-o|--output]}} {{path/to/output_executable}}`

- Activate output of all errors and warnings:

`clang++ {{path/to/source.cpp}} -Wall {{[-o|--output]}} {{output_executable}}`

- Show common warnings, debug symbols in output, and optimize without affecting debugging:

`clang++ {{path/to/source.cpp}} -Wall {{[-g|--debug]}} -Og {{[-o|--output]}} {{path/to/output_executable}}`

- Choose a language standard to compile for:

`clang++ {{path/to/source.cpp}} -std={{c++20}} {{[-o|--output]}} {{path/to/output_executable}}`

- Include libraries located at a different path than the source file:

`clang++ {{path/to/source.cpp}} {{[-o|--output]}} {{path/to/output_executable}} -I{{path/to/header_path}} -L{{path/to/library_path}} -l{{path/to/library_name}}`

- Compile source code into LLVM Intermediate Representation (IR):

`clang++ {{[-S|--assemble]}} -emit-llvm {{path/to/source.cpp}} {{[-o|--output]}} {{path/to/output.ll}}`

- Optimize the compiled program for performance:

`clang++ {{path/to/source.cpp}} -O{{1|2|3|fast}} {{[-o|--output]}} {{path/to/output_executable}}`

- Display version:

`clang++ --version`
