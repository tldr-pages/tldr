# eza

> 现代的、维护良好的 `ls` 替代工具，基于 `exa` 构建。
> 更多信息：<https://github.com/eza-community/eza>.

- 列出目录中的文件，每个文件占一行：

`eza --oneline`

- 列出包含隐藏文件的所有文件：

`eza --all`

- 以长格式（权限、所有者、大小和修改日期）列出所有文件：

`eza --long --all`

- 列出文件，按大小从大到小排序：

`eza --reverse --sort={{size}}`

- 显示三级深度的文件树：

`eza --long --tree --level={{3}}`

- 列出文件，按修改日期排序（最早的在前）：

`eza --long --sort={{modified}}`

- 列出文件，显示其标题、图标和 Git 状态：

`eza --long --header --icons --git`

- 不列出在 `.gitignore` 中提到的文件：

`eza --git-ignore`
