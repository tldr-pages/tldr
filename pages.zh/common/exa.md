# exa

> `ls`（列出目录内容）的现代替代品。
> 更多信息：<https://the.exa.website>。

- 每行列出一个文件：

`exa --oneline`

- 列出所有文件，包括隐藏文件：

`exa --all`

- 所有文件的长格式列表（权限、所有权、大小和修改日期）：

`exa --long --all`

- 列出文件，最大的在顶部：

`exa --reverse --sort={{size}}`

- 显示文件树，深度为三层：

`exa --long --tree --level={{3}}`

- 按修改日期排序列出文件（最旧的在前）：

`exa --long --sort={{modified}}`

- 列出文件及其标题、图标和 Git 状态：

`exa --long --header --icons --git`

- 不列出在 `.gitignore` 中提到的文件：

`exa --git-ignore`