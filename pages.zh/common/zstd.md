# zstd

> 使用 Zstandard 压缩对文件进行压缩或解压缩。
> 更多信息：<https://github.com/facebook/zstd>。

- 将文件压缩为一个新的 `.zst` 后缀文件：

`zstd {{path/to/file}}`

- 解压缩文件：

`zstd --decompress {{path/to/file.zst}}`

- 解压缩到 `stdout`：

`zstd --decompress --stdout {{path/to/file.zst}}`

- 压缩文件时指定压缩级别，其中 1=最快，19=最慢，3=默认：

`zstd -{{level}} {{path/to/file}}`

- 使用更多内存（压缩和解压缩均需）解锁更高的压缩级别（最高可达 22）：

`zstd --ultra -{{level}} {{path/to/file}}`