# dirname

> 计算文件或目录路径的父目录。
> 更多信息：<https://www.gnu.org/software/coreutils/dirname>。

- 计算给定路径的父目录：

`dirname {{path/to/file_or_directory}}`

- 计算多个路径的父目录：

`dirname {{path/to/file_or_directory1 path/to/file_or_directory2 ...}}`

- 用 NUL 字符分隔输出而不是换行符（在与 `xargs` 结合使用时很有用）：

`dirname --zero {{path/to/file_or_directory1 path/to/file_or_directory2 ...}}`