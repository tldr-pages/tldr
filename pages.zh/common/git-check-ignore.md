# git check-ignore

> 分析和调试 Git 忽略/排除（".gitignore"）文件。
> 更多信息：<https://git-scm.com/docs/git-check-ignore>。

- 检查文件或目录是否被忽略：

`git check-ignore {{path/to/file_or_directory}}`

- 检查多个文件或目录是否被忽略：

`git check-ignore {{path/to/file_or_directory1 path/to/file_or_directory2 ...}}`

- 从 `stdin` 读取每行一个路径名：

`git check-ignore --stdin < {{path/to/file_list}}`

- 不检查索引（用于调试为什么路径被跟踪而未被忽略）：

`git check-ignore --no-index {{path/to/file_or_directory1 path/to/file_or_directory2 ...}}`

- 包括每个路径的匹配模式详情：

`git check-ignore --verbose {{path/to/file_or_directory1 path/to/file_or_directory2 ...}}`