# xmount

> 在多种输入和输出硬盘映像类型之间实时转换，并可选支持写入缓存。
> 使用 FUSE（用户空间文件系统）创建一个包含输入映像虚拟表示的虚拟文件系统。
> 更多信息：<https://manned.org/xmount>。

- 将 `.raw` 映像文件挂载到 DMG 容器文件中：

`xmount --in {{raw}} {{path/to/image.dd}} --out {{dmg}} {{mountpoint}}`

- 使用写入缓存支持将 EWF 映像文件挂载到 VHD 文件中以启动：

`xmount --cache {{path/to/cache.ovl}} --in {{ewf}} {{path/to/image.E??}} --out {{vhd}} {{mountpoint}}`

- 将第 1 分区（从扇区 2048 开始）挂载到新的 `.raw` 映像文件中：

`xmount --offset {{2048}} --in {{raw}} {{path/to/image.dd}} --out {{raw}} {{mountpoint}}`
