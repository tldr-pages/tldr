# rg

> Ripgrep 是一个递归行导向的搜索工具。
> 旨在成为 `grep` 的更快替代品。
> 更多信息：<https://github.com/BurntSushi/ripgrep>。

- 在当前目录递归搜索正则表达式：

`rg {{正则表达式}}`

- 在当前目录中递归搜索正则表达式，包括隐藏文件和 `.gitignore` 中列出的文件：

`rg --no-ignore --hidden {{正则表达式}}`

- 仅在特定子目录中搜索正则表达式：

`rg {{正则表达式}} {{子目录集合}}`

- 在匹配 glob 的文件中搜索正则表达式（例如 `README.*`）：

`rg {{正则表达式}} --glob {{glob}}`

- 搜索匹配正则表达式的文件名：

`rg --files | rg {{正则表达式}}`

- 仅列出匹配的文件（在管道传输到其他命令时非常有用）：

`rg --files-with-matches {{正则表达式}}`

- 显示不匹配给定正则表达式的行：

`rg --invert-match {{正则表达式}}`

- 搜索字面字符串模式：

`rg --fixed-strings -- {{字符串}}`