# wc

> 计数行、单词或字节。
> 更多信息：<https://www.gnu.org/software/coreutils/manual/html_node/wc-invocation.html>.

- 计数文件中的行数：

`wc {{[-l|--lines]}} {{路径/到/文件}}`

- 计数文件中的单词数：

`wc {{[-w|--words]}} {{路径/到/文件}}`

- 计数文件中的字节数：

`wc {{[-c|--bytes]}} {{路径/到/文件}}`

- 计数文件中的字符数（考虑所有多字节的字符）：

`wc {{[-m|--chars]}} {{路径/到/文件}}`

- 使用 `stdin`，按顺序计数行、单词和字节：

`{{find .}} | wc`

- 计算最长行的长度（字符数）：

`wc {{[-L|--max-line-length]}} {{路径/到/文件}}`
