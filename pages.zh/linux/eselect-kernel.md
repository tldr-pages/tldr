# eselect kernel

> 用于管理 `/usr/src/linux` 符号链接的 `eselect` 模块。
> 更多信息：<https://wiki.gentoo.org/wiki/Eselect#Kernel>.

- 列出可用的内核符号链接目标及其编号：

`eselect kernel list`

- 通过 `list` 命令中列出的名称或编号设置 `/usr/src/linux` 符号链接：

`eselect kernel set {{name|number}}`

- 显示当前内核符号链接指向的目标：

`eselect kernel show`

- 将内核符号链接设置为当前正在运行的内核：

`eselect kernel update`
