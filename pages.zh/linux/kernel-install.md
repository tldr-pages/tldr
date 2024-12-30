# kernel-install

> 将内核和初始化ramdisk（initrd）镜像添加到 `/boot` 或从中删除。
> 更多信息：<https://manned.org/kernel-install.8>。

- 将内核和初始化文件系统（initramfs）镜像添加到引导加载程序分区：

`sudo kernel-install add {{kernel-version}} {{kernel-image}} {{path/to/initrd-file ...}}`

- 从引导加载程序分区中删除内核：

`sudo kernel-install remove {{kernel-version}}`

- 显示已配置或自动检测的各种路径和参数：

`sudo kernel-install inspect {{kernel-image}}`