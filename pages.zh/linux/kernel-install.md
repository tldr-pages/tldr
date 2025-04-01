# kernel-install

> 向 `/boot` 添加和移除内核和 initrd 镜像。
> 更多信息：<https://manned.org/kernel-install.8>.

- 向引导程序分区添加内核和 initramfs 镜像：

`sudo kernel-install add {{kernel-version}} {{kernel-image}} {{path/to/initrd-file ...}}`

- 从引导程序分区移除内核：

`sudo kernel-install remove {{kernel-version}}`

- 显示已配置或自动检测到的各种路径和参数：

`sudo kernel-install inspect {{kernel-image}}`
