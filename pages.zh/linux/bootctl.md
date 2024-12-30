# bootctl

> 控制 EFI 固件启动设置和管理启动加载器。
> 更多信息：<https://manned.org/bootctl>。

- 显示系统固件和启动加载器的信息：

`bootctl status`

- 显示所有可用的启动加载器条目：

`bootctl list`

- 设置一个标志，以在下次启动时进入系统固件（类似于 `sudo systemctl reboot --firmware-setup`）：

`sudo bootctl reboot-to-firmware true`

- 指定 EFI 系统分区的路径（默认为 `/efi/`、`/boot/` 或 `/boot/efi`）：

`bootctl --esp-path={{/path/to/efi_system_partition/}}`

- 将 `systemd-boot` 安装到 EFI 系统分区：

`sudo bootctl install`

- 从 EFI 系统分区中删除所有已安装的 `systemd-boot` 版本：

`sudo bootctl remove`