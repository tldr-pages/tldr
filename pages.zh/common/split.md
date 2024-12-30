# 拆分

> 将文件拆分成多个部分。
> 更多信息：<https://www.gnu.org/software/coreutils/split>。

- 拆分一个文件，每个拆分包含10行（最后一个拆分除外）：

`split -l 10 {{path/to/file}}`

- 将文件拆分为5个文件。文件被拆分成每个部分大小相同（最后一个拆分除外）：

`split -n 5 {{path/to/file}}`

- 每个拆分包含512字节的文件（最后一个拆分除外；使用512k表示千字节，512m表示兆字节）：

`split -b 512 {{path/to/file}}`

- 每个拆分最多包含512字节，且不拆断行：

`split -C 512 {{path/to/file}}`