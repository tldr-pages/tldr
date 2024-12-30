# genkernel

> Gentoo Linux 工具，用于编译和安装内核。
> 更多信息：<https://wiki.gentoo.org/wiki/Genkernel>。

- 自动编译和安装通用内核：

`sudo genkernel all`

- 仅构建和安装 bzImage|initramfs|内核|ramdisk：

`sudo genkernel {{bzImage|initramfs|kernel|ramdisk}}`

- 在编译和安装之前对内核配置进行更改：

`sudo genkernel --menuconfig all`

- 生成一个自定义名称的内核：

`sudo genkernel --kernname={{custom_name}} all`

- 使用默认目录 `/usr/src/linux` 之外的内核源：

`sudo genkernel --kerneldir={{path/to/directory}} all`