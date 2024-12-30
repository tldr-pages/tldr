# grub-set-default

> 设置 GRUB 的默认引导条目。
> 更多信息：<https://manned.org/grub-set-default>。

- 将默认引导条目设置为条目编号、名称或标识符：

`sudo grub-set-default {{entry_number}}`

- 将默认引导条目设置为替代引导目录的条目编号、名称或标识符：

`sudo grub-set-default --boot-directory {{/path/to/boot_directory}} {{entry_number}}`