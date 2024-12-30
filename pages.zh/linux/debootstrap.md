# debootstrap

> 创建一个基本的 Debian 系统。
> 更多信息：<https://wiki.debian.org/Debootstrap>。

- 在 `debian-root` 目录中创建一个 Debian 稳定版系统：

`sudo debootstrap stable {{path/to/debian-root/}} http://deb.debian.org/debian`

- 创建一个仅包含所需软件包的最小系统：

`sudo debootstrap --variant=minbase stable {{path/to/debian-root/}}`

- 在 `focal-root` 目录中创建一个 Ubuntu 20.04 系统，并使用本地镜像：

`sudo debootstrap focal {{path/to/focal-root/}} {{file:///path/to/mirror/}}`

- 切换到一个引导的系统：

`sudo chroot {{path/to/root}}`

- 列出可用的版本：

`ls /usr/share/debootstrap/scripts/`