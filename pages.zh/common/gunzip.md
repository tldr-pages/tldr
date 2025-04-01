# gunzip

> 从 `gzip` (`.gz`) 压缩包中解压文件。
> 更多信息：<https://manned.org/gunzip>。

- 从压缩包中解压文件，如果存在同名文件则替换：

`gunzip {{archive.tar.gz}}`

- 将文件解压到指定的目标路径：

`gunzip --stdout {{archive.tar.gz}} > {{archive.tar}}`

- 解压文件并保留原压缩包：

`gunzip --keep {{archive.tar.gz}}`

- 列出压缩文件的内容：

`gunzip --list {{file.txt.gz}}`

- 从 `stdin` 解压压缩包：

`cat {{path/to/archive.gz}} | gunzip`