# debootstrap

> Membuat sistem Debian dasar.
> Informasi lebih lanjut: <https://wiki.debian.org/Debootstrap>.

- Membuat sistem Debian stable didalam direktori `debian-root`:

`sudo debootstrap stable {{jalan/ke/debian-root/}} http://deb.debian.org/debian`

- Membuat sistem minimal termasuk hanya paket yang diperlukan:

`sudo debootstrap --variant=minbase stable {{jalan/ke/debian-root/}}`

- Membuat sistem Ubuntu 20.04 didalam direktori `focal-root` dengan mirror lokal:

`sudo debootstrap focal {{jalan/ke/focal-root/}} {{file:///jalan/ke/mirror/}}`

- Berpindah ke sistem yang telah di bootstrap:

`sudo chroot {{jalan/ke/root}}`

- Memperlihatkan rilis Debian atau Ubuntu yang tersedia:

`ls /usr/share/debootstrap/scripts/`
