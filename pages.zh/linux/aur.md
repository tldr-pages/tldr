# aur

> 从 AUR 构建软件包并管理本地仓库。
> 注意：需要在 `/etc/pacman.conf` 中定义本地仓库，并且需要安装 `vifm` 才能完全正常工作。
> 更多信息：<https://github.com/aurutils/aurutils>。

- 在 AUR 数据库中搜索软件包：

`aur search {{keyword}}`

- 从 AUR 下载软件包及其依赖项，构建它们并将其添加到本地仓库：

`aur sync {{package}}`

- 列出本地仓库中可用的软件包：

`aur repo --list`

- 升级本地仓库软件包：

`aur sync --upgrades`

- 安装软件包而不在 Vim 中查看更改，并且不确认依赖项安装：

`aur sync --noview --noconfirm {{package}}`