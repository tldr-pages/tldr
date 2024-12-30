# ditto

> 复制文件和目录。
> 更多信息：<https://keith.github.io/xcode-man-pages/ditto.1.html>。

- 用源目录的内容覆盖目标目录的内容：

`ditto {{path/to/source_directory}} {{path/to/destination_directory}}`

- 为每个正在复制的文件在终端窗口打印一行：

`ditto -V {{path/to/source_directory}} {{path/to/destination_directory}}`

- 复制给定的文件或目录，同时保留原始文件权限：

`ditto -rsrc {{path/to/source_directory}} {{path/to/destination_directory}}`