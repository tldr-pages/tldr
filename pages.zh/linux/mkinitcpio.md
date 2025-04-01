# mkinitcpio

> 生成基于指定预设的启动 Linux 内核所需的初始 RAM 磁盘环境。
> 更多信息：<https://manned.org/mkinitcpio.8>.

- 执行干运行（打印将要执行的操作，但不实际执行）：

`mkinitcpio`

- 基于 `linux` 预设生成 RAM 磁盘环境：

`mkinitcpio --preset {{linux}}`

- 基于 `linux-lts` 预设生成 RAM 磁盘环境：

`mkinitcpio --preset {{linux-lts}}`

- 基于所有现有预设生成 RAM 磁盘环境（用于在 `/etc/mkinitcpio.conf` 文件更改后重新生成所有 initramfs 镜像）：

`mkinitcpio --allpresets`

- 使用替代配置文件生成 initramfs 镜像：

`mkinitcpio --config {{path/to/mkinitcpio.conf}} --generate {{path/to/initramfs.img}}`

- 为当前运行的内核以外的内核生成 initramfs 镜像（已安装的内核版本可以在 `/usr/lib/modules/` 中找到）：

`mkinitcpio --kernel {{kernel_version}} --generate {{path/to/initramfs.img}}`

- 列出所有可用的钩子：

`mkinitcpio --listhooks`

- 显示特定钩子的帮助信息：

`mkinitcpio --hookhelp {{hook_name}}`