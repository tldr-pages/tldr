# lzop

> 使用 LZO 压缩算法压缩或解压缩文件。
> 更多信息：<https://www.lzop.org/>.

- 将文件压缩成一个新的 `.lzo` 后缀的文件：

`lzop {{path/to/file}}`

- 解压缩文件：

`lzop -d {{path/to/file.lzo}}`

- 压缩文件，同时指定压缩级别。0 = 最差，9 = 最佳（默认级别为 3）：

`lzop -{{level}} {{path/to/file}}`