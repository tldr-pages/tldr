# clang-check

> Check basic errors and work with Clang's Abstract Syntax Tree (AST).
> Part of Clang's LibTooling and is useful for debugging and analyzing C/C++ code.
> More information: <https://manned.org/clang-check>.

- Run default checks on a source file:

`clang-check {{path/to/file.cpp}} --`

- Dump the Abstract Syntax Tree for debugging:

`clang-check {{path/to/file.cpp}} -ast-dump --`

- Filter AST by Name:

`clang-check {{path/to/file.cpp}} -ast-dump -ast-dump-filter FunctionName`

- Pretty-Print AST:

`clang-check {{path/to/file.cpp}} -ast-print --`
