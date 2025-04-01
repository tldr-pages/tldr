# rg

> Ripgrep，一个递归的行导向搜索工具。
> 力求成为比 `grep` 更快的替代方案。
> 更多信息：<https://github.com/BurntSushi/ripgrep>。

- 在当前目录中递归搜索正则表达式：

`rg {{regular_expression}}`

- 在当前目录中递归搜索正则表达式，包括隐藏文件和 `.gitignore` 中列出的文件：

`rg --no-ignore --hidden {{regular_expression}}`

- 仅在指定子目录中搜索正则表达式：

`rg {{regular_expression}} {{set_of_subdirs}}`

- 在匹配特定模式（例如 `README.*`）的文件中搜索正则表达式：

`rg {{regular_expression}} --glob {{glob}}`

- 搜索与正则表达式匹配的文件名：

`rg --files | rg {{regular_expression}}`

- 仅列出匹配的文件（在传递给其他命令时很有用）：

`rg --files-with-matches {{regular_expression}}`

- 显示不匹配给定正则表达式的行：

`rg --invert-match {{regular_expression}}`

- 搜索字符串模式（字面量）：

`rg --fixed-strings -- {{string}}`
