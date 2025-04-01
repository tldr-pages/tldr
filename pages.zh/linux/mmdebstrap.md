# mmdebstrap

> 创建 Debian chroot 环境。
> `debootstrap` 的替代工具。
> 更多信息：<https://gitlab.mister-muffin.de/josch/mmdebstrap/>.

- 创建 Debian Stable 目录 chroot：

`sudo mmdebstrap stable {{path/to/debian-root/}}`

- 使用镜像创建 Debian Bookworm tarball chroot：

`mmdebstrap bookworm {{path/to/debian-bookworm.tar}} {{http://mirror.example.org/debian}}`

- 创建包含额外软件包的 Debian Sid tarball chroot：

`mmdebstrap sid {{path/to/debian-sid.tar}} --include={{pkg1,pkg2}}`