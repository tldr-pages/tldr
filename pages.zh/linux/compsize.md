# compsize

> 计算 btrfs 文件系统中一组文件的压缩比。
> 有关通过解碎片重新压缩文件的信息，请参阅 `btrfs filesystem`。
> 更多信息：<https://github.com/kilobyte/compsize>。

- 计算文件或目录的当前压缩比：

`sudo compsize {{path/to/file_or_directory}}`

- 不跨越文件系统边界：

`sudo compsize --one-file-system {{path/to/file_or_directory}}`

- 显示原始字节计数，而不是人类可读的大小：

`sudo compsize --bytes {{path/to/file_or_directory}}`