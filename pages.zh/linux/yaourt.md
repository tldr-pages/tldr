# yaourt

> Arch Linux 中用于从 Arch User Repository 中构建软件包的工具。
> 更多信息：<https://linuxcommandlibrary.com/man/yaourt>.

- 同步并更新所有软件包（包括 AUR）：

`yaourt -Syua`

- 安装一个新的软件包（包括 AUR）：

`yaourt -S {{软件包}}`

- 移除一个软件包和它的依赖（包括 AUR 软件包）：

`yaourt -Rs {{软件包}}`

- 在软件包数据库中搜索一个关键字（包括 AUR）：

`yaourt -Ss {{软件包}}`

- 列出已安装的软件包、版本和仓库（AUR 软件包将被列在 'local' 仓库下）：

`yaourt -Q`
