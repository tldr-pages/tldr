# qemu

> 通用机器仿真器和虚拟化工具。
> 支持多种 CPU 架构。
> 更多信息：<https://www.qemu.org>。

- 从模拟 i386 架构的镜像启动：

`qemu-system-i386 -hda {{image_name.img}}`

- 从模拟 x64 架构的镜像启动：

`qemu-system-x86_64 -hda {{image_name.img}}`

- 使用实时 ISO 镜像启动 QEMU 实例：

`qemu-system-i386 -hda {{image_name.img}} -cdrom {{os_image.iso}} -boot d`

- 为实例指定内存大小：

`qemu-system-i386 -m 256 -hda {{image_name.img}} -cdrom {{os-image.iso}} -boot d`

- 从物理设备启动（例如，从 USB 测试可启动介质）：

`qemu-system-i386 -hda {{/dev/storage_device}}`