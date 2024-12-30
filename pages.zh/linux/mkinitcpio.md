# mkinitcpio

> 生成初始 ramdisk 环境以启动基于指定预设的 Linux 内核。
> 更多信息：<https://manned.org/mkinitcpio.8>。

- 执行干运行（打印将要执行的操作而不实际执行）：

`mkinitcpio`

- 基于 `linux` 预设生成 ramdisk 环境：

`mkinitcpio --preset {{linux}}`

- 基于 `linux-lts` 预设生成 ramdisk 环境：

`mkinitcpio --preset {{linux-lts}}`

- 基于所有现有预设生成 ramdisk 环境（在 `/etc/mkinitcpio.conf` 更改后用于重新生成所有 initramfs 镜像）：

`mkinitcpio --allpresets`

- 使用替代配置文件生成 initramfs 镜像：

`mkinitcpio --config {{path/to/mkinitcpio.conf}} --generate {{path/to/initramfs.img}}`

- 为当前正在运行的内核以外的内核生成 initramfs 镜像（已安装的内核版本可以在 `/usr/lib/modules/` 中找到）：

`mkinitcpio --kernel {{kernel_version}} --generate {{path/to/initramfs.img}}`

- 列出所有可用的 hooks：

`mkinitcpio --listhooks`

- 显示特定 hook 的帮助：

`mkinitcpio --hookhelp {{hook_name}}`