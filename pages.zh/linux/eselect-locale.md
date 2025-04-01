# eselect locale

> 用于管理 `LANG` 环境变量的 `eselect` 模块，`LANG` 设置了系统语言。
> 更多信息：<https://wiki.gentoo.org/wiki/Eselect#Locale>。

- 列出可用的区域设置：

`eselect locale list`

- 通过名称或从 `list` 命令中选择的索引来设置 `/etc/profile.env` 中的 `LANG` 环境变量：

`eselect locale set {{name|index}}`

- 显示 `/etc/profile.env` 中 `LANG` 的值：

`eselect locale show`