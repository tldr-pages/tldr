# yaourt

> Arch Linux 用于从 Arch 用户仓库构建软件包的工具。
> 更多信息：<https://linuxcommandlibrary.com/man/yaourt>。

- 同步并更新所有软件包（包括 AUR）：

`yaourt -Syua`

- 安装一个新软件包（包括 AUR）：

`yaourt -S {{package}}`

- 移除一个软件包及其依赖（包括 AUR 软件包）：

`yaourt -Rs {{package}}`

- 在软件包数据库中搜索关键字（包括 AUR）：

`yaourt -Ss {{query}}`

- 列出已安装的软件包、版本和仓库（AUR 软件包将列在名为 'local' 的仓库下）：

`yaourt -Q`