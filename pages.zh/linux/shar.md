# shar

> 创建一个 shell 存档。
> 更多信息：<https://www.gnu.org/software/sharutils/manual/sharutils.html>。

- 创建一个 shell 脚本，执行时可以从自身提取给定的文件：

`shar --vanilla-operation {{path/to/file1 path/to/file2 ...}} > {{path/to/archive.sh}}`

- 压缩存档中的文件：

`shar --compactor {{xz}} {{path/to/file1 path/to/file2 ...}} > {{path/to/archive.sh}}`

- 将所有文件视为二进制文件（即对所有内容进行 `uuencode` 处理）：

`shar --uuencode {{path/to/file1 path/to/file2 ...}} > {{path/to/archive.sh}}`

- 将所有文件视为文本文件（即不对任何内容进行 `uuencode` 处理）：

`shar --text-files {{path/to/file1 path/to/file2 ...}} > {{path/to/archive.sh}}`

- 在存档的头部注释中包含名称和切割标记：

`shar --archive-name "{{My files}}" --cut-mark {{path/to/file1 path/to/file2 ...}} > {{path/to/archive.sh}}`