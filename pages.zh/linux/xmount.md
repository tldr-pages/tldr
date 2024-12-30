# xmount

> 通过可选的写缓存支持，动态转换多种输入和输出硬盘映像类型。
> 使用 FUSE（用户空间文件系统）创建一个虚拟文件系统，该系统包含输入映像的虚拟表示。
> 更多信息：<https://manned.org/xmount>。

- 将 `.raw` 映像文件挂载到 DMG 容器文件中：

`xmount --in {{raw}} {{path/to/image.dd}} --out {{dmg}} {{mountpoint}}`

- 带有写缓存支持的 EWF 映像文件挂载到 VHD 文件中以便启动：

`xmount --cache {{path/to/cache.ovl}} --in {{ewf}} {{path/to/image.E??}} --out {{vhd}} {{mountpoint}}`

- 将第一个分区从扇区 2048 挂载到一个新的 `.raw` 映像文件中：

`xmount --offset {{2048}} --in {{raw}} {{path/to/image.dd}} --out {{raw}} {{mountpoint}}`