# pigz

> 多线程 zlib 压缩工具。
> 更多信息：<https://github.com/madler/pigz>。

- 使用默认选项压缩文件：

`pigz {{path/to/file}}`

- 使用最佳压缩方法压缩文件：

`pigz -9 {{path/to/file}}`

- 使用无压缩和 4 个处理器压缩文件：

`pigz -0 -p{{4}} {{path/to/file}}`

- 使用 tar 压缩目录：

`tar cf - {{path/to/directory}} | pigz > {{path/to/file.tar.gz}}`

- 解压文件：

`pigz -d {{archive.gz}}`

- 列出归档文件的内容：

`pigz -l {{archive.tar.gz}}`