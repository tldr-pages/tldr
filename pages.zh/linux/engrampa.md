# engrampa

> 在 MATE 桌面环境中将文件打包为 zip/tar 文件。
> 另请参见：`zip`，`tar`。
> 更多信息：<https://github.com/mate-desktop/engrampa>。

- 启动 Engrampa：

`engrampa`

- 打开特定的归档文件：

`engrampa {{path/to/archive1.tar path/to/archive2.tar ...}}`

- 递归归档特定文件和/或目录：

`engrampa --add-to={{path/to/compressed.tar}} {{path/to/file_or_directory1 path/to/file_or_directory2 ...}}`

- 从归档中提取文件和/或目录到特定路径：

`engrampa --extract-to={{path/to/directory}} {{path/to/archive1.tar path/to/archive2.tar ...}}`