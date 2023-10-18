# pacman --upgrade

> Kegunaan manajer paket Arch Linux.
> Guarda anche: `pacman`.
> Informasi lebih lanjut: <https://man.archlinux.org/man/pacman.8>.

- Instal satu paket atau lebih dari file:

`sudo pacman --upgrade {{jalan/menuju/paket1.pkg.tar.zst}} {{jalan/menuju/paket2.pkg.tar.zst}}`

- Instal paket tanpa konfirmasi:

`sudo pacman --upgrade --noconfirm {{jalan/menuju/paket.pkg.tar.zst}}`

- Timpa file yang bentrok selama pemasangan paket:

`sudo pacman --upgrade --overwrite {{jalan/menuju/file}} {{jalan/menuju/paket.pkg.tar.zst}}`

- Instal paket, melewati pemeriksaan versi dependensi:

`sudo pacman --upgrade --nodeps {{jalan/menuju/paket.pkg.tar.zst}}`

- Tampilkan daftar paket yang akan terpengaruh (tidak menginstal paket apa pun):

`pacman --upgrade --print {{jalan/menuju/paket.pkg.tar.zst}}`

- Tampilkan bantuan:

`pacman --upgrade --help`
