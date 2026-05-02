# eza

> 基于 `exa` 构建的现代化、持续维护的 `ls` 替代品。
> 更多信息：<https://github.com/eza-community/eza>。

- 每行列出一个文件：

`eza {{[-1|--oneline]}}`

- 列出所有文件，包括隐藏文件：

`eza {{[-a|--all]}}`

- 以长格式列出所有文件（包含权限、所有者、大小和修改日期）：

`eza {{[-al|--all --long]}}`

- 列出文件，最大的排在最上面：

`eza {{[-r|--reverse]}} {{[-s|--sort]}} {{size}}`

- 显示文件树，深度为三层：

`eza {{[-lT|--long --tree]}} {{[-L|--level]}} {{3}}`

- 按修改日期排序列出文件（从最旧的开始）：

`eza {{[-l|--long]}} {{[-s|--sort]}} {{modified}}`

- 列出文件及其表头、图标和 Git 状态：

`eza {{[-lh|--long --header]}} --icons --git`

- 不列出 `.gitignore` 中提到的文件：

`eza --git-ignore`
