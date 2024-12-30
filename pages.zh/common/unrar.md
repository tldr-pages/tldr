# unrar

> 解压 RAR 压缩文件。
> 更多信息：<https://manned.org/unrar>。

- 按原目录结构提取文件：

`unrar x {{compressed.rar}}`

- 按原目录结构将文件提取到指定路径：

`unrar x {{compressed.rar}} {{path/to/extract}}`

- 将文件提取到当前目录，丢失压缩包中的目录结构：

`unrar e {{compressed.rar}}`

- 测试压缩包内每个文件的完整性：

`unrar t {{compressed.rar}}`

- 列出压缩包内的文件而不解压缩：

`unrar l {{compressed.rar}}`