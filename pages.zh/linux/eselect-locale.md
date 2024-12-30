# 选择语言环境

> 一个用于管理 `LANG` 环境变量的 `eselect` 模块，该变量设置系统语言。
> 更多信息：<https://wiki.gentoo.org/wiki/Eselect#Locale>。

- 列出可用的语言环境：

`eselect locale list`

- 通过名称或索引设置 `/etc/profile.env` 中的 `LANG` 环境变量，索引来自 `list` 命令：

`eselect locale set {{name|index}}`

- 显示 `/etc/profile.env` 中 `LANG` 的值：

`eselect locale show`