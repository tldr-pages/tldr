# zstd

> 使用 Zstandard 压缩来压缩 / 解压文件。
> 更多信息：<https://github.com/facebook/zstd>.

- 将一个文件压缩到一个 `.zst` 后缀的压缩文件中：

`zstd {{file}}`

- 解压缩一个文件：

`zstd -d {{file}}.zst`

- 将文件解压缩到标准输出（stdout）：

`zstd -dc {{file}}.zst`

- 使用指定的压缩等级来压缩一个文件.0 = 最差，19 = 最好（默认等级是 3）：

`zstd -{{level}} {{file}}`

- 使用更多内存（解压或压缩时）来得到更高的压缩比：

`zstd --ultra -{{level}} {{file}}`
