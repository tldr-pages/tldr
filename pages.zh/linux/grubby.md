# grubby

> 用于配置 `grub` 和 `zipl` 启动加载程序的工具。
> 更多信息：<https://manned.org/grubby.8>.

- 为所有内核菜单项添加内核启动参数：

`sudo grubby --update-kernel=ALL --args '{{quiet console=ttyS0}}'`

- 从默认内核的菜单项中移除现有参数：

`sudo grubby --update-kernel=DEFAULT --remove-args {{quiet}}`

- 列出所有内核菜单项：

`sudo grubby --info=ALL`
