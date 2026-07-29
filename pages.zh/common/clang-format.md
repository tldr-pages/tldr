# clang-format

> 自动格式化 C/C++/Java/JavaScript/Objective-C/Protobuf/C# 代码。
> 更多信息：<https://clang.llvm.org/docs/ClangFormat.html>。

- 格式化文件并将结果输出到 `stdout`：

`clang-format {{路径/到/文件}}`

- 原地格式化文件：

`clang-format -i {{路径/到/文件}}`

- 使用预定义的代码风格格式化文件：

`clang-format --style {{LLVM|GNU|Google|Chromium|Microsoft|Mozilla|WebKit}} {{路径/到/文件}}`

- 使用源文件上级目录中的 `.clang-format` 文件进行格式化：

`clang-format --style file {{路径/到/文件}}`

- 生成自定义 `.clang-format` 配置文件：

`clang-format --style {{LLVM|GNU|Google|Chromium|Microsoft|Mozilla|WebKit}} --dump-config > {{.clang-format}}`
