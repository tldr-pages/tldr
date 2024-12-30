# wc

> 计数行、单词和字节。
> 更多信息：<https://www.gnu.org/software/coreutils/wc>。

- 计算文件中的所有行数：

`wc --lines {{path/to/file}}`

- 计算文件中的所有单词数：

`wc --words {{path/to/file}}`

- 计算文件中的所有字节数：

`wc --bytes {{path/to/file}}`

- 计算文件中的所有字符数（考虑多字节字符）：

`wc --chars {{path/to/file}}`

- 从 `stdin` 计算所有行、单词和字节数：

`{{find .}} | wc`

- 计算最长行的字符数：

`wc --max-line-length {{path/to/file}}`