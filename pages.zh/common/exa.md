# exa

> `ls` 的现代替代品（列出目录内容）。
> 注意：`exa` 已不再维护。请改用 `eza`。
> 另请参阅：`eza`。
> 更多信息：<https://github.com/ogham/exa#command-line-options>。

- 每行列出一个文件：

`exa {{[-1|--oneline]}}`

- 列出所有文件，包括隐藏文件：

`exa {{[-a|--all]}}`

- 以长格式列出所有文件（包含权限、所有者、大小和修改日期）：

`exa {{[-al|--all --long]}}`

- 列出文件，最大的排在最上面：

`exa {{[-r|--reverse]}} {{[-s|--sort]}} {{size}}`

- 显示文件树，深度为三层：

`exa {{[-lT|--long --tree]}} {{[-L|--level]}} {{3}}`

- 按修改日期排序列出文件（从最旧的开始）：

`exa {{[-l|--long]}} {{[-s|--sort]}} {{modified}}`

- 列出文件及其表头、图标和 Git 状态：

`exa {{[-lh|--long --header]}} --icons --git`

- 不列出 `.gitignore` 中提到的文件：

`exa --git-ignore`
