# exa

> `ls` 的现代替代品（列出目录内容）。
> 更多信息：<https://github.com/ogham/exa>.

- 每行列出一个文件：

`exa --oneline`

- 列出所有文件，包括隐藏文件：

`exa --all`

- 以长格式列出所有文件（包括权限、所有权、大小和修改日期）：

`exa --long --all`

- 从大到小列出文件：

`exa --reverse --sort={{size}}`

- 显示三层深度的文件树：

`exa --long --tree --level={{3}}`

- 按修改日期排序列出文件（最早的在前）：

`exa --long --sort={{modified}}`

- 列出带有标题、图标和 Git 状态的文件：

`exa --long --header --icons --git`

- 不列出 `.gitignore` 中提到的文件：

`exa --git-ignore`
