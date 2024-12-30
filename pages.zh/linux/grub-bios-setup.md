# grub-bios-setup

> 设置设备以使用BIOS配置的GRUB。
> 在大多数情况下，您应该使用`grub-install`而不是`grub-bios-setup`。
> 更多信息：<https://manned.org/grub-bios-setup.8>。

- 设置设备以使用GRUB启动：

`grub-bios-setup {{/dev/sdX}}`

- 即使检测到问题也要安装：

`grub-bios-setup --force {{/dev/sdX}}`

- 在特定目录中安装GRUB：

`grub-bios-setup --directory={{/boot/grub}} {{/dev/sdX}}`