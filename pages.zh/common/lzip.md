# lzip

> 一个无损数据压缩工具，用户界面类似 `gzip` 或 `bzip2`。
> Lzip 使用简化的 "Lempel-Ziv-Markovchain-Algorithm" (LZMA) 流格式，提供 3 级完整性检查，以最大化互操作性和优化安全性。
> 更多信息：<https://www.nongnu.org/lzip>。

- 压缩文件，用压缩版本替换原文件：

`lzip {{path/to/file}}`

- 压缩文件，保留输入文件：

`lzip {{[-k|--keep]}} {{path/to/file}}`

- 以最佳压缩级别（级别=9）压缩文件：

`lzip {{[-k|--keep]}} {{path/to/file}} --best`

- 以最快速度（级别=0）压缩文件：

`lzip {{[-k|--keep]}} {{path/to/file}} --fast`

- 测试压缩文件的完整性：

`lzip {{[-t|--test]}} {{path/to/archive.lz}}`

- 解压缩文件，用未压缩版本替换原文件：

`lzip {{[-d|--decompress]}} {{path/to/archive.lz}}`

- 解压缩文件，保留压缩包：

`lzip {{[-d|--decompress]}} {{[-k|--keep]}} {{path/to/archive.lz}}`

- 列出压缩包中的文件并显示压缩统计信息：

`lzip {{[-l|--list]}} {{path/to/archive.lz}}`