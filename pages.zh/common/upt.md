# upt

> 统一的界面，用于管理各种操作系统上的软件包，例如 Windows、许多 Linux 发行版、macOS、FreeBSD，甚至 Haiku。
> 它需要安装本机操作系统的软件包管理器。
> 请参阅：`flatpak`、`brew`、`scoop`、`apt`、`dnf`.
> 更多信息：<https://github.com/sigoden/upt>.

- 更新可用软件包的列表：

`upt update`

- 搜索指定的软件包：

`upt search {{搜索软件包关键词}}`

- 显示某个软件包的信息：

`upt info {{软件包}}`

- 安装指定的软件包：

`upt install {{软件包}}`

- 移除指定的软件包：

`upt {{remove|uninstall}} {{软件包}}`

- 升级所有已安装的软件包：

`upt upgrade`

- 升级指定的软件包：

`upt upgrade {{软件包}}`

- 列出已安装的软件包：

`upt list`
