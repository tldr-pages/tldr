# pamac

> 一个用于 GUI 软件包管理器 pamac 的命令行工具。
> 如果看不到 AUR 软件包，请在 `/etc/pamac.conf` 或 GUI 中启用 AUR。
> 更多信息：<https://wiki.manjaro.org/index.php/Pamac>。

- 安装新软件包：

`pamac install {{package_name}}`

- 卸载软件包及其不再需要的依赖项（孤儿包）：

`pamac remove --orphans {{package_name}}`

- 在软件包数据库中搜索软件包：

`pamac search {{package_name}}`

- 列出已安装的软件包：

`pamac list --installed`

- 检查软件包更新：

`pamac checkupdates`

- 升级所有软件包：

`pamac upgrade`
