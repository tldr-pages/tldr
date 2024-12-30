# dracut

> 生成用于引导Linux内核的initramfs镜像。
> Dracut默认使用`/etc/dracut.conf`、`/etc/dracut.conf.d/*.conf`和`/usr/lib/dracut/dracut.conf.d/*.conf`中的配置文件选项。
> 更多信息：<https://github.com/dracutdevs/dracut/wiki>。

- 为当前内核生成一个initramfs镜像而不覆盖任何选项：

`dracut`

- 为当前内核生成一个initramfs镜像并覆盖现有的：

`dracut --force`

- 为特定内核生成一个initramfs镜像：

`dracut --kver {{kernel_version}}`

- 列出可用模块：

`dracut --list-modules`