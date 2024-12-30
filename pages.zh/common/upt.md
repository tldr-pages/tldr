# upt

> 统一的界面，用于管理各种操作系统上的软件包，如 Windows、许多 Linux 发行版、macOS、FreeBSD 甚至 Haiku。
> 它需要安装本地操作系统的软件包管理器。
> 另见：`flatpak`、`brew`、`scoop`、`apt`、`dnf`。
> 更多信息：<https://github.com/sigoden/upt>。

- 更新可用软件包列表：

`upt update`

- 搜索给定的软件包：

`upt search {{search_term}}`

- 显示软件包信息：

`upt info {{package}}`

- 安装给定的软件包：

`upt install {{package}}`

- 删除给定的软件包：

`upt {{remove|uninstall}} {{package}}`

- 升级所有已安装的软件包：

`upt upgrade`

- 升级给定的软件包：

`upt upgrade {{package}}`

- 列出已安装的软件包：

`upt list`