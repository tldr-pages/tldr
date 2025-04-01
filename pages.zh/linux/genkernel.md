# genkernel

> Gentoo Linux 用于编译和安装内核的工具。
> 更多信息：<https://wiki.gentoo.org/wiki/Genkernel>。

- 自动编译并安装一个通用内核：

`sudo genkernel all`

- 仅构建和安装 bzImage|initramfs|kernel|ramdisk：

`sudo genkernel {{bzImage|initramfs|kernel|ramdisk}}`

- 在编译和安装前应用内核配置更改：

`sudo genkernel --menuconfig all`

- 生成具有自定义名称的内核：

`sudo genkernel --kernname={{custom_name}} all`

- 使用默认目录 `/usr/src/linux` 以外的内核源：

`sudo genkernel --kerneldir={{path/to/directory}} all`