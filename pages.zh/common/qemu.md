# qemu

> 通用机器模拟器和虚拟机。
> 支持多种 CPU 架构。
> 更多信息：<https://www.qemu.org>.

- 使用 i386 架构从镜像启动：

`qemu-system-i386 -hda {{image_name.img}}`

- 使用 x64 架构从镜像启动：

`qemu-system-x86_64 -hda {{image_name.img}}`

- 使用实时 ISO 镜像启动 QEMU 实例：

`qemu-system-i386 -hda {{image_name.img}} -cdrom {{os_image.iso}} -boot d`

- 为实例指定 RAM 大小：

`qemu-system-i386 -m 256 -hda {{image_name.img}} -cdrom {{os-image.iso}} -boot d`

- 从物理设备启动（例如，从 USB 启动以测试可启动介质）：

`qemu-system-i386 -hda {{/dev/storage_device}}`
