# clang-format

> Tool to auto-format C/C++/Java/JavaScript/Objective-C/Protobuf/C# code.
> More information: <https://clang.llvm.org/docs/ClangFormat.html>.

- Format a file and print the result to stdout:

`clang-format {{path/to/file}}`

- Format a file in-place:

`clang-format -i {{path/to/file}}`

- Format a file using a predefined coding style:

`clang-format --style={{LLVM|Google|Chromium|Mozilla|WebKit}} {{path/to/file}}`

- Format a file using the `.clang-format` file in one of the parent directories of the source file:

`clang-format --style=file {{path/to/file}}`

- Generate a custom `.clang-format` file:

`clang-format --style={{LLVM|Google|Chromium|Mozilla|WebKit}} --dump-config > {{.clang-format}}`
