# gunzip

> 从 `gzip` (`.gz`) 压缩包中提取文件。
> 更多信息：<https://manned.org/gunzip>。

- 从压缩包中提取文件，如存在则替换原文件：

`gunzip {{archive.tar.gz}}`

- 将文件提取到目标位置：

`gunzip --stdout {{archive.tar.gz}} > {{archive.tar}}`

- 提取文件并保留压缩包：

`gunzip --keep {{archive.tar.gz}}`

- 列出压缩文件的内容：

`gunzip --list {{file.txt.gz}}`

- 从 `stdin` 解压缩压缩包：

`cat {{path/to/archive.gz}} | gunzip`