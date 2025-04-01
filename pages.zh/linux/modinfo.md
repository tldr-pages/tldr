# modinfo

> 获取有关 Linux 内核模块的信息。
> 参见：`kmod`，其他用于模块管理的命令。
> 更多信息：<https://manned.org/modinfo>.

- 列出内核模块的所有属性：

`modinfo {{kernel_module}}`

- 仅列出指定的属性：

`modinfo -F {{author|description|license|parm|filename}} {{kernel_module}}`
