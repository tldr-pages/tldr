# mksquashfs

> 创建或追加文件和目录到 squashfs 文件系统。
> 更多信息：<https://manned.org/mksquashfs>.

- 创建或追加文件和目录到 squashfs 文件系统（默认使用 `gzip` 压缩）：

`mksquashfs {{path/to/file_or_directory1 path/to/file_or_directory2 ...}} {{filesystem.squashfs}}`

- 创建或追加文件和目录到 squashfs 文件系统，使用特定的压缩算法：

`mksquashfs {{path/to/file_or_directory1 path/to/file_or_directory2 ...}} {{filesystem.squashfs}} -comp {{gzip|lzo|lz4|xz|zstd|lzma}}`

- 创建或追加文件和目录到 squashfs 文件系统，排除某些文件或目录：

`mksquashfs {{path/to/file_or_directory1 path/to/file_or_directory2 ...}} {{filesystem.squashfs}} -e {{file|directory1 file|directory2 ...}}`

- 创建或追加文件和目录到 squashfs 文件系统，排除以 gzip 结尾的文件：

`mksquashfs {{path/to/file_or_directory1 path/to/file_or_directory2 ...}} {{filesystem.squashfs}} -wildcards -e "{{*.gz}}"`

- 创建或追加文件和目录到 squashfs 文件系统，排除匹配正则表达式的文件：

`mksquashfs {{path/to/file_or_directory1 path/to/file_or_directory2 ...}} {{filesystem.squashfs}} -regex -e "{{regular_expression}}"`
