# mmdebstrap

> Create a Debian chroot.
> Alternative to `debootstrap`.
> More information: <https://gitlab.mister-muffin.de/josch/mmdebstrap/>.

- Create a Debian Stable directory chroot:

`sudo mmdebstrap stable {{path/to/debian-root/}}`

- Create a Debian Bookworm tarball chroot using a mirror:

`mmdebstrap bookworm {{path/to/debian-bookworm.tar}} {{http://mirror.example.org/debian}}`

- Create a Debian Sid tarball chroot with additional packages:

`mmdebstrap sid {{path/to/debian-sid.tar}} --include={{pkg1,pkg2}}`
