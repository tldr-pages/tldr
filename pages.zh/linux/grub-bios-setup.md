# grub-bios-setup

> 为使用 BIOS 配置的 GRUB 设置设备。
> 在大多数情况下，你应该使用 `grub-install` 而不是 `grub-bios-setup`。
> 更多信息：<https://manned.org/grub-bios-setup.8>。

- 为使用 GRUB 引导设置设备：

`grub-bios-setup {{/dev/sdX}}`

- 即使检测到问题也进行安装：

`grub-bios-setup --force {{/dev/sdX}}`

- 在指定目录中安装 GRUB：

`grub-bios-setup --directory={{/boot/grub}} {{/dev/sdX}}`