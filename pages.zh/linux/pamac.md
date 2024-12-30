# pamac

> 一个用于图形界面包管理器 pamac 的命令行工具。
> 如果您无法看到 AUR 包，请在 `/etc/pamac.conf` 或 GUI 中启用它。
> 更多信息：<https://wiki.manjaro.org/index.php/Pamac>。

- 安装一个新包：

`pamac install {{package_name}}`

- 移除一个包及其不再需要的依赖（孤儿包）：

`pamac remove --orphans {{package_name}}`

- 在包数据库中搜索一个包：

`pamac search {{package_name}}`

- 列出已安装的包：

`pamac list --installed`

- 检查包更新：

`pamac checkupdates`

- 升级所有包：

`pamac upgrade`