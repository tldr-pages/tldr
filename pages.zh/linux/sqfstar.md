# sqfstar

> 从 tar 归档文件创建 squashfs 文件系统。
> 更多信息：<https://manned.org/sqfstar>。

- 从未压缩的 tar 归档文件创建 squashfs 文件系统（默认使用 `gzip` 压缩）：

`sqfstar {{filesystem.squashfs}} < {{archive.tar}}`

- 从使用 `gzip` 压缩的 tar 归档文件创建 squashfs 文件系统，并使用特定算法压缩文件系统：

`zcat {{archive.tar.gz}} | sqfstar -comp {{gzip|lzo|lz4|xz|zstd|lzma}} {{filesystem.squashfs}}`

- 从使用 `xz` 压缩的 tar 归档文件创建 squashfs 文件系统，排除某些文件：

`xzcat {{archive.tar.xz}} | sqfstar {{filesystem.squashfs}} {{file1 file2 ...}}`

- 从使用 `zstd` 压缩的 tar 归档文件创建 squashfs 文件系统，排除以 `.gz` 结尾的文件：

`zstdcat {{archive.tar.zst}} | sqfstar {{filesystem.squashfs}} "{{*.gz}}"`

- 从使用 `lz4` 压缩的 tar 归档文件创建 squashfs 文件系统，排除匹配正则表达式的文件：

`lz4cat {{archive.tar.lz4}} | sqfstar {{filesystem.squashfs}} -regex "{{regular_expression}}"`
