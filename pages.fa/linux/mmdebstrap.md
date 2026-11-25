# mmdebstrap

> ایجاد chroot مربوط به Debian.
> جایگزینی برای `debootstrap`.
> اطلاعات بیشتر: <https://gitlab.mister-muffin.de/josch/mmdebstrap/>.

- ایجاد chroot دایرکتوری Debian Stable:

`sudo mmdebstrap stable {{path/to/debian-root}}/`

- ایجاد chroot به‌صورت tarball برای Debian Bookworm با استفاده از آینه:

`mmdebstrap bookworm {{path/to/debian-bookworm.tar}} {{http://mirror.example.org/debian}}`

- ایجاد chroot به‌صورت tarball برای Debian Sid با بسته‌های اضافی:

`mmdebstrap sid {{path/to/debian-sid.tar}} --include={{pkg1,pkg2}}`
