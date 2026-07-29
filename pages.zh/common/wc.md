# wc

> 统计行数、单词数和字节数。
> 更多信息：<https://www.gnu.org/software/coreutils/manual/html_node/wc-invocation.html>。

- 统计文件中的所有行数：

`wc {{[-l|--lines]}} {{路径/到/文件}}`

- 统计文件中的所有单词数：

`wc {{[-w|--words]}} {{路径/到/文件}}`

- 统计文件中的所有字节数：

`wc {{[-c|--bytes]}} {{路径/到/文件}}`

- 统计文件中的所有字符数（考虑多字节字符）：

`wc {{[-m|--chars]}} {{路径/到/文件}}`

- 从 `stdin` 统计所有行数、单词数和字节数：

`{{find .}} | wc`

- 统计文件中最长行的字符长度：

`wc {{[-L|--max-line-length]}} {{路径/到/文件}}`
