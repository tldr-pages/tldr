# lzip

> 一种无损数据压缩工具，其用户界面类似于 `gzip` 或 `bzip2`。
> Lzip 使用简化版的 "Lempel-Ziv-Markovchain-Algorithm" (LZMA) 流格式，并提供 3 因子完整性检查，以最大限度地提高互操作性和优化安全性。
> 更多信息：<https://www.nongnu.org/lzip>。

- 压缩文件，并用压缩版本替换它：

`lzip {{path/to/file}}`

- 压缩文件，保留输入文件：

`lzip -k {{path/to/file}}`

- 使用最佳压缩率压缩文件（级别=9）：

`lzip -k {{path/to/file}} --best`

- 以最快速度压缩文件（级别=0）：

`lzip -k {{path/to/file}} --fast`

- 测试压缩文件的完整性：

`lzip --test {{path/to/archive.lz}}`

- 解压文件，并用原始未压缩版本替换它：

`lzip -d {{path/to/archive.lz}}`

- 解压文件，保留归档文件：

`lzip -d -k {{path/to/archive.lz}}`

- 列出归档中的文件并显示压缩统计信息：

`lzip --list {{path/to/archive.lz}}`