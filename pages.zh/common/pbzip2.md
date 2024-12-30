# pbzip2

> `bzip2` 文件压缩器的并行实现。
> 另请参阅：`bzip2`、`tar`。
> 更多信息：<https://manned.org/pbzip2>。

- 压缩文件：

`pbzip2 {{path/to/file}}`

- 使用指定数量的处理器压缩文件：

`pbzip2 -p{{4}} {{path/to/file}}`

- [d]解压文件：

`pbzip2 --decompress {{path/to/compressed_file.bz2}}`

- 显示帮助：

`pbzip2 -h`