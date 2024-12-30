# lsinitrd

> 显示 initramfs 镜像的内容。
> 另见: `dracut`。
> 更多信息: <https://github.com/dracutdevs/dracut/blob/master/man/lsinitrd.1.asc>。

- 显示当前内核的 initramfs 镜像内容：

`lsinitrd`

- 显示指定内核的 initramfs 镜像内容：

`lsinitrd --kver {{kernel_version}}`

- 显示指定 initramfs 镜像的内容：

`lsinitrd {{path/to/initramfs.img}}`

- 列出包含在 initramfs 镜像中的模块：

`lsinitrd --mod`

- 将 initramfs 解压到当前目录：

`lsinitrd --unpack`