# qemu

> 通用机器模拟器和虚拟化器。
> 支持多种 CPU 架构。
> 更多信息：<https://www.qemu.org>.

- 启动镜像并模拟 i386 架构：

`qemu-system-i386 -hda {{镜像名称.img}}`

- 启动镜像并模拟 x64 架构：

`qemu-system-x86_64 -hda {{镜像名称.img}}`

- 使用现场 ISO 镜像启动 QEMU 实例：

`qemu-system-i386 -hda {{镜像名称.img}} -cdrom {{操作系统镜像.iso}} -boot d`

- 为实例指定 RAM 大小：

`qemu-system-i386 -m 256 -hda {{镜像名称.img}} -cdrom {{操作系统镜像.iso}} -boot d`

- 从物理设备启动（例如，从 USB 启动以测试可启动介质）：

`qemu-system-i386 -hda {{/dev/存储设备}}`
