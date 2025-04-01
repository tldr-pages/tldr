# eselect profile

> 一个用于管理 `/etc/portage/make.profile` 符号链接的 `eselect` 模块，该链接用于设置系统配置文件。
> 更多信息：<https://wiki.gentoo.org/wiki/Eselect#Profile>。

- 列出可用的配置文件符号链接目标及其编号：

`eselect profile list`

- 通过名称或编号（从 `list` 命令中获取）设置 `/etc/portage/make.profile` 符号链接：

`eselect profile set {{name|number}}`

- 显示当前的系统配置文件：

`eselect profile show`
