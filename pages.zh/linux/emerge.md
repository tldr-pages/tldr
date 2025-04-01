# emerge

> Gentoo Linux 包管理工具。
> 关于其他包管理器的等效命令，请参见：<https://wiki.archlinux.org/title/Pacman/Rosetta>。
> 更多信息：<https://wiki.gentoo.org/wiki/Portage#emerge>。

- 同步所有包：

`sudo emerge --sync`

- 更新所有包，包括依赖项：

`sudo emerge {{[-avuDN|--ask --verbose --update --deep --newuse]}} @world`

- 恢复失败的更新，跳过失败的包：

`sudo emerge --resume --skipfirst`

- 安装新包，并请求确认：

`sudo emerge {{[-av|--ask --verbose]}} {{package}}`

- 删除包及其依赖项，并请求确认：

`sudo emerge {{[-avc|--ask --verbose --depclean]}} {{package}}`

- 删除孤儿包（作为依赖项安装但不再被任何包需要）：

`sudo emerge {{[-avc|--ask --verbose --depclean]}}`

- 在包数据库中搜索关键词：

`emerge {{[-S|--searchdesc]}} {{keyword}}`
