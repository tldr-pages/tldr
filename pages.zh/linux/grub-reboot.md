# grub-reboot

> 为 GRUB 设置下次启动时的默认启动项。
> 更多信息：<https://manned.org/grub-reboot>。

- 设置下次启动时的默认启动项为启动项编号、名称或标识符：

`sudo grub-reboot {{entry_number}}`

- 为指定的启动目录设置下次启动时的默认启动项为启动项编号、名称或标识符：

`sudo grub-reboot --boot-directory {{/path/to/boot_directory}} {{entry_number}}`