# clang-format

> 自动格式化 C/C++/Java/JavaScript/Objective-C/Protobuf/C# 代码。
> 更多信息：<https://clang.llvm.org/docs/ClangFormat.html>.

- 格式化文件并将结果输出到 `stdout`：

`clang-format {{path/to/file}}`

- 在原地格式化文件：

`clang-format -i {{path/to/file}}`

- 使用预定义的编码风格格式化文件：

`clang-format --style {{LLVM|GNU|Google|Chromium|Microsoft|Mozilla|WebKit}} {{path/to/file}}`

- 使用源文件的父目录中的 `.clang-format` 文件来格式化文件：

`clang-format --style=file {{path/to/file}}`

- 生成自定义的 `.clang-format` 文件：

`clang-format --style {{LLVM|GNU|Google|Chromium|Microsoft|Mozilla|WebKit}} --dump-config > {{.clang-format}}`