# xed

> 在 Xcode 中打开文件进行编辑。
> 更多信息：<https://keith.github.io/xcode-man-pages/xed.1.html>。

- 在 Xcode 中打开文件：

`xed {{path/to/file1 path/to/file2 ...}}`

- 在 Xcode 中打开文件（如果文件不存在则创建）：

`xed --create {{path/to/file1 path/to/file2 ...}}`

- 在 Xcode 中打开文件并跳转到第 75 行：

`xed --line 75 {{path/to/file}}`