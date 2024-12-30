# unlink

> 从文件系统中删除文件链接。
> 如果链接是文件的最后一个链接，则文件内容将丢失。
> 更多信息：<https://www.gnu.org/software/coreutils/unlink>。

- 如果指定的文件是最后一个链接，则删除该文件：

`unlink {{path/to/file}}`