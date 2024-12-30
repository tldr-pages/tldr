# yay

> Yet Another Yogurt: 从Arch用户仓库构建和安装软件包。
> 另见 `pacman`。
> 更多信息：<https://github.com/Jguer/yay>。

- 交互式搜索并安装来自仓库和AUR的软件包：

`yay {{package_name|search_term}}`

- 同步并更新所有来自仓库和AUR的软件包：

`yay`

- 仅同步和更新AUR软件包：

`yay -Sua`

- 从仓库和AUR安装新软件包：

`yay -S {{package}}`

- 移除已安装的软件包及其依赖项和配置文件：

`yay -Rns {{package}}`

- 在仓库和AUR中搜索软件包数据库中的关键字：

`yay -Ss {{keyword}}`

- 移除孤立软件包（作为依赖项安装但不被任何软件包所需）：

`yay -Yc`

- 显示已安装软件包和系统健康状况的统计信息：

`yay -Ps`