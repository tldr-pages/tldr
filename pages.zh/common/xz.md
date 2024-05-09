# xz

> 解压缩 XZ 和 LZMA 文件。
> 更多信息：<https://manned.org/xz>.

- 使用 xz 压缩文件：

`xz {{路径/到/文件}}`

- 解压 XZ 文件：

`xz --decompress {{路径/到/文件.xz}}`

- 使用 lzma 压缩文件：

`xz --format=lzma {{路径/到/文件}}`

- 解压 LZMA 文件：

`xz --decompress --format=lzma {{路径/到/文件.lzma}}`

- 解压文件并输出到 `stdout`（暗示 `--keep`）：

`xz --decompress --stdout {{路径/到/文件.xz}}`

- 压缩文件但不删除原文件：

`xz --keep {{路径/到/文件}}`

- 使用最快方式压缩文件：

`xz -0 {{路径/到/文件}}`

- 使用最好方式压缩文件：

`xz -9 {{路径/到/文件}}`
