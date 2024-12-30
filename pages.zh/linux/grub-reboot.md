# grub-reboot

> 为GRUB设置下次启动的默认启动项。
> 更多信息：<https://manned.org/grub-reboot>。

- 将下次启动的默认启动项设置为条目编号、名称或标识符：

`sudo grub-reboot {{entry_number}}`

- 将下次启动的默认启动项设置为替代启动目录的条目编号、名称或标识符：

`sudo grub-reboot --boot-directory {{/path/to/boot_directory}} {{entry_number}}`