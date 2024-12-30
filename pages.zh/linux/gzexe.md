# gzexe

> 在保持可执行文件可执行的同时压缩它们。
> 备份原始文件，在其名称后附加 `~`，并创建一个解压和执行其中二进制文件的 shell 脚本。
> 更多信息：<https://manned.org/gzexe.1>。

- 就地压缩可执行文件：

`gzexe {{path/to/executable}}`

- 就地解压压缩的可执行文件（即将 shell 脚本转换回未压缩的二进制文件）：

`gzexe -d {{path/to/compressed_executable}}`