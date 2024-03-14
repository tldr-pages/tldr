# bootctl

> 控制EFI固件启动设置并管理启动加载器。
> 更多信息：<https://manned.org/bootctl>。

- 显示系统固件和启动加载器的信息：

`bootctl status`

- 显示所有可用的启动加载器条目：

`bootctl list`

- 将系统固件设置为在下次启动时启动：

`sudo bootctl reboot-to-firmware true`

- 指定EFI系统分区（默认为`/efi/`，`/boot/`或`/boot/efi`）：

`bootctl --esp-path={{/path/to/efi_system_partition/}}`

- 将`systemd-boot`安装到EFI系统分区：

`sudo bootctl install`

- 从EFI系统分区移除所有已安装的`systemd-boot`版本：

`sudo bootctl remove`
