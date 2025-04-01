# ouch

> 命令行工具，用于压缩和解压缩文件和目录。
> 更多信息：<https://crates.io/crates/ouch>。

- 解压缩特定文件：

`ouch decompress {{path/to/archive.tar.xz}}`

- 将文件解压缩到特定位置：

`ouch decompress {{path/to/archive.tar.xz}} --dir {{path/to/directory}}`

- 解压缩多个文件：

`ouch decompress {{path/to/archive1.tar path/to/archive2.tar.gz ...}}`

- 压缩文件：

`ouch compress {{path/to/file1 path/to/file2 ...}} {{path/to/archive.zip}}`