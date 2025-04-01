# aur

> 从 AUR 构建软件包并管理本地仓库。
> 注意：需要在 `/etc/pacman.conf` 中定义本地仓库，并安装 `vifm` 才能完全发挥功能。
> 更多信息：<https://github.com/aurutils/aurutils>.

- 在 AUR 数据库中搜索软件包：

`aur search {{keyword}}`

- 从 AUR 下载软件包及其依赖项，构建它们并添加到本地仓库：

`aur sync {{package}}`

- 列出本地仓库中的可用软件包：

`aur repo {{[-l|--list]}}`

- 升级本地仓库中的软件包：

`aur sync {{[-u|--upgrades]}}`

- 安装软件包时不使用 Vim 查看更改，并不确认依赖项安装：

`aur sync --noview {{[-n|--noconfirm]}} {{package}}`
