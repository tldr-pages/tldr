# gitsome

> 一个基于终端的 GitHub 接口，通过 `gh` 命令访问。
> 它还为 `git` 命令提供菜单式自动补全建议。
> 更多信息：<https://github.com/donnemartin/gitsome>.

- 进入 gitsome shell（可选），启用 Git（和 gh）命令的自动补全和交互式帮助：

`gitsome`

- 使用当前账户设置 GitHub 集成：

`gh configure`

- 列出当前账户的通知（如同在 <https://github.com/notifications> 看到的）：

`gh notifications`

- 列出当前账户的星标仓库，使用给定的搜索字符串过滤：

`gh starred "{{python 3}}"`

- 查看给定 GitHub 仓库的最近活动：

`gh feed {{tldr-pages/tldr}}`

- 查看给定 GitHub 用户的最近活动，使用默认分页器（如 `less`）：

`gh feed {{torvalds}} -p`
