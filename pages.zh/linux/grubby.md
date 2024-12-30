# grubby

> 用于配置 `grub` 和 `zipl` 引导加载程序的工具。
> 更多信息：<https://manned.org/grubby.8>。

- 为所有内核菜单条目添加内核启动参数：

`sudo grubby --update-kernel=ALL --args '{{quiet console=ttyS0}}'`

- 从默认内核的条目中删除现有参数：

`sudo grubby --update-kernel=DEFAULT --remove-args {{quiet}}`

- 列出所有内核菜单条目：

`sudo grubby --info=ALL`