# pacaur

> 一个用于 Arch Linux 的工具，用于从 Arch 用户仓库构建和安装软件包。
> 更多信息：<https://github.com/rmarquis/pacaur>。

- 同步并更新所有软件包（包括 AUR）：

`pacaur -Syu`

- 仅同步并更新 AUR 软件包：

`pacaur -Syua`

- 安装一个新软件包（包括 AUR）：

`pacaur -S {{package}}`

- 移除一个软件包及其依赖项（包括 AUR 软件包）：

`pacaur -Rs {{package}}`

- 在软件包数据库中搜索关键词（包括 AUR）：

`pacaur -Ss {{keyword}}`

- 列出所有当前已安装的软件包（包括 AUR 软件包）：

`pacaur -Qs`