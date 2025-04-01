# lzop

> 使用 LZO 压缩或解压文件。
> 更多信息：<https://www.lzop.org/>.

- 将文件压缩成带有 `.lzo` 后缀的新文件：

`lzop {{path/to/file}}`

- 解压文件：

`lzop -d {{path/to/file.lzo}}`

- 压缩文件时指定压缩级别。0 = 最低，9 = 最高（默认级别为 3）：

`lzop -{{level}} {{path/to/file}}`