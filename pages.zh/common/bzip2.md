# bzip2

> 块排序文件压缩器。
> 另请参阅：`bzcat`、`bunzip2`、`bzip2recover`。
> 更多信息：<https://manned.org/bzip2>。

- 压缩文件：

`bzip2 {{路径/到/待压缩文件}}`

- 解压文件：

`bzip2 {{[-d|--decompress]}} {{路径/到/压缩文件.bz2}}`

- 解压文件到 `stdout`：

`bzip2 {{[-dc|--decompress --stdout]}} {{路径/到/压缩文件.bz2}}`

- 测试归档文件中每个文件的完整性：

`bzip2 {{[-t|--test]}} {{路径/到/压缩文件.bz2}}`

- 显示每个已处理文件的压缩率及详细信息：

`bzip2 {{[-v|--verbose]}} {{路径/到/压缩文件.bz2}}`

- 解压文件并覆盖现有文件：

`bzip2 {{[-f|--force]}} {{路径/到/压缩文件.bz2}}`

- 显示帮助信息：

`bzip2 {{[-h|--help]}}`
