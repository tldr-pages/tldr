# 切割

> 将一个文件分割成多个部分。
> 更多信息：<https://keith.github.io/xcode-man-pages/split.1.html>。

- 将一个文件分割，每个分割包含10行（最后一个分割除外）：

`split -l 10 {{path/to/file}}`

- 按正则表达式分割文件。匹配的行将成为下一个输出文件的第一行：

`split -p {{cat|^[dh]og}} {{path/to/file}}`

- 每个分割包含512字节（最后一个分割除外；使用512k表示千字节，使用512m表示兆字节）：

`split -b 512 {{path/to/file}}`

- 将一个文件分割成5个文件。文件被分割成每个部分大小相同（最后一个分割除外）：

`split -n 5 {{path/to/file}}`