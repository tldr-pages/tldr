# eselect 配置文件

> 一个用于管理 `/etc/portage/make.profile` 符号链接的 `eselect` 模块，该链接设置系统配置文件。
> 更多信息：<https://wiki.gentoo.org/wiki/Eselect#Profile>。

- 列出可用的配置文件符号链接目标及其编号：

`eselect profile list`

- 通过名称或 `list` 命令中的编号设置 `/etc/portage/make.profile` 符号链接：

`eselect profile set {{name|number}}`

- 显示当前系统配置文件：

`eselect profile show`