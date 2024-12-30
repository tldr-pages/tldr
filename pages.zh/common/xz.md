# xz

> 压缩或解压XZ和LZMA文件。
> 更多信息：<https://manned.org/xz>。

- 使用xz压缩文件：

`xz {{path/to/file}}`

- 解压XZ文件：

`xz --decompress {{path/to/file.xz}}`

- 使用lzma压缩文件：

`xz --format=lzma {{path/to/file}}`

- 解压LZMA文件：

`xz --decompress --format=lzma {{path/to/file.lzma}}`

- 解压文件并写入`stdout`（隐含`--keep`）：

`xz --decompress --stdout {{path/to/file.xz}}`

- 压缩文件，但不删除原始文件：

`xz --keep {{path/to/file}}`

- 使用最快的压缩方式压缩文件：

`xz -0 {{path/to/file}}`

- 使用最佳压缩方式压缩文件：

`xz -9 {{path/to/file}}`