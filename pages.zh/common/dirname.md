# dirname

> 计算文件或目录路径的父目录。
> 更多信息：<https://www.gnu.org/software/coreutils/manual/html_node/dirname-invocation.html>。

- 计算给定路径的父目录：

`dirname {{path/to/file_or_directory}}`

- 计算多个路径的父目录：

`dirname {{path/to/file_or_directory1 path/to/file_or_directory2 ...}}`

- 使用 NUL 字符分隔输出而非换行符（与 `xargs` 结合使用时有用）：

`dirname {{[-z|--zero]}} {{path/to/file_or_directory1 path/to/file_or_directory2 ...}}`
