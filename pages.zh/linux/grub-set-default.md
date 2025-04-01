# grub-set-default

> 设置 GRUB 的默认启动项。
> 更多信息：<https://manned.org/grub-set-default>。

- 将默认启动项设置为启动项编号、名称或标识符：

`sudo grub-set-default {{entry_number}}`

- 将默认启动项设置为替代启动目录中的启动项编号、名称或标识符：

`sudo grub-set-default --boot-directory {{/path/to/boot_directory}} {{entry_number}}`
