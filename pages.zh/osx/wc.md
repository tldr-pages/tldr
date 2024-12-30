# wc

> 统计行数、单词数或字节数。
> 更多信息：<https://keith.github.io/xcode-man-pages/wc.1.html>。

- 统计文件中的行数：

`wc -l {{path/to/file}}`

- 统计文件中的单词数：

`wc -w {{path/to/file}}`

- 统计文件中的字符数（字节数）：

`wc -c {{path/to/file}}`

- 统计文件中的字符数（考虑多字节字符集）：

`wc -m {{path/to/file}}`

- 使用 `stdin` 按顺序统计行数、单词数和字符数（字节数）：

`{{find .}} | wc`