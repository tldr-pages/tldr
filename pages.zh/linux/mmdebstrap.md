# mmdebstrap

> 创建一个 Debian chroot。
> `debootstrap` 的替代方案。
> 更多信息：<https://gitlab.mister-muffin.de/josch/mmdebstrap/>.

- 创建一个 Debian Stable 目录 chroot：

`sudo mmdebstrap stable {{path/to/debian-root/}}`

- 使用镜像创建一个 Debian Bookworm tarball chroot：

`mmdebstrap bookworm {{path/to/debian-bookworm.tar}} {{http://mirror.example.org/debian}}`

- 创建一个带有额外软件包的 Debian Sid tarball chroot：

`mmdebstrap sid {{path/to/debian-sid.tar}} --include={{pkg1,pkg2}}`