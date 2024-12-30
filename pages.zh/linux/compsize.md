# compsize

> 计算 btrfs 文件系统上一组文件的压缩比。
> 另见 `btrfs filesystem` 以通过碎片整理重新压缩文件。
> 更多信息：<https://github.com/kilobyte/compsize>。

- 计算文件或目录的当前压缩比：

`sudo compsize {{path/to/file_or_directory}}`

- 不跨越文件系统边界：

`sudo compsize --one-file-system {{path/to/file_or_directory}}`

- 显示原始字节计数而不是人类可读的大小：

`sudo compsize --bytes {{path/to/file_or_directory}}`