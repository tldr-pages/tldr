# rg

> Ripgrep，一款递归的行导向搜索工具。
> 旨在成为 `grep` 的更快替代品。
> 更多信息：<https://github.com/BurntSushi/ripgrep/blob/master/GUIDE.md>。

- 在当前目录中递归搜索匹配模式的内容（`regex`）：

`rg {{模式}}`

- 在指定文件或目录中递归搜索匹配模式的内容：

`rg {{模式}} {{路径/到/文件或目录}}`

- 搜索字面字符串模式：

`rg {{[-F|--fixed-strings]}} -- {{字符串}}`

- 包含隐藏文件以及 `.gitignore` 中列出的条目：

`rg {{[-.|--hidden]}} --no-ignore {{模式}}`

- 仅搜索文件名匹配通配符（glob）模式的文件（例如 `README.*`）：

`rg {{模式}} {{[-g|--glob]}} {{文件名通配符模式}}`

- 递归列出当前目录中匹配模式的文件名：

`rg --files | rg {{模式}}`

- 仅列出匹配的文件（适用于管道传递给其他命令）：

`rg {{[-l|--files-with-matches]}} {{模式}}`

- 显示不匹配该模式的行：

`rg {{[-v|--invert-match]}} {{模式}}`
