# gitsome

> 一款基于终端的 GitHub 界面，通过 `gh` 命令访问。
> 它还为 `git` 命令提供菜单样式的自动补全建议。
> 更多信息：<https://github.com/donnemartin/gitsome>。

- 进入 gitsome shell（可选），以启用 Git（和 gh）命令的自动补全和交互式帮助：

`gitsome`

- 设置与当前账户的 GitHub 集成：

`gh configure`

- 列出当前账户的通知（如在 <https://github.com/notifications> 中所见）：

`gh notifications`

- 列出当前账户的星标仓库，按给定搜索字符串过滤：

`gh starred "{{python 3}}"`

- 查看给定 GitHub 仓库的最近活动动态：

`gh feed {{tldr-pages/tldr}}`

- 使用默认分页工具（例如 `less`）查看给定 GitHub 用户的最近活动动态：

`gh feed {{torvalds}} -p`