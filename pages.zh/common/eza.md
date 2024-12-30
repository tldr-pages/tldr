# eza

> 基于 `exa` 的现代、维护中的 `ls` 替代品。
> 更多信息：<https://github.com/eza-community/eza>。

- 每行列出一个文件：

`eza --oneline`

- 列出所有文件，包括隐藏文件：

`eza --all`

- 所有文件的详细格式列表（权限、所有者、大小和修改日期）：

`eza --long --all`

- 按大小从大到小列出文件：

`eza --reverse --sort={{size}}`

- 显示文件树，深度三层：

`eza --long --tree --level={{3}}`

- 按修改日期排序列出文件（最旧的在前）：

`eza --long --sort={{modified}}`

- 列出文件及其头部、图标和 Git 状态：

`eza --long --header --icons --git`

- 不列出 `.gitignore` 中提到的文件：

`eza --git-ignore`