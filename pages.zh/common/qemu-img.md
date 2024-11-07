# qemu-img

> 创建和操作 Quick Emulator 虚拟硬盘镜像。
> 更多信息：<https://qemu.readthedocs.io/en/master/tools/qemu-img.html>.

- 创建一个特定大小（以千兆字节为单位）的磁盘镜像：

`qemu-img create {{image_name.img}} {{gigabytes}}G`

- 显示有关磁盘镜像的信息：

`qemu-img info {{image_name.img}}`

- 增加或减少镜像大小：

`qemu-img resize {{image_name.img}} {{gigabytes}}G`

- 转储指定磁盘镜像的每个扇区的分配状态：

`qemu-img map {{image_name.img}}`

- 将 VMware 的 .vmdk 磁盘镜像转换为 KVM 的 .qcow2 磁盘镜像：

`qemu-img convert -f {{vmdk}} -O {{qcow2}} {{路径/到/文件/foo.vmdk}} {{路径/到/文件/foo.qcow2}}`
