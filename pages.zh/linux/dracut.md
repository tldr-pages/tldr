# dracut

> 生成用于启动 Linux 内核的 initramfs 镜像。
> Dracut 默认使用 `/etc/dracut.conf`、`/etc/dracut.conf.d/*.conf` 和 `/usr/lib/dracut/dracut.conf.d/*.conf` 配置文件中的选项。
> 更多信息：<https://github.com/dracutdevs/dracut/wiki>.

- 为当前内核生成 initramfs 镜像，不覆盖任何选项：

`dracut`

- 为当前内核生成 initramfs 镜像并覆盖现有镜像：

`dracut --force`

- 为指定的内核生成 initramfs 镜像：

`dracut --kver {{kernel_version}}`

- 列出可用模块：

`dracut --list-modules`
