# gzexe

> 压缩可执行文件的同时保持其可执行性。
> 备份原始文件，在文件名后追加 `~`，并创建一个 shell 脚本，用于解压缩并执行其中的二进制文件。
> 更多信息：<https://manned.org/gzexe.1>。

- 就地压缩可执行文件：

`gzexe {{path/to/executable}}`

- 就地解压缩已压缩的可执行文件（即将 shell 脚本转换回未压缩的二进制文件）：

`gzexe -d {{path/to/compressed_executable}}`