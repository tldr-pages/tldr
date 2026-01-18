# pacman --upgrade

> Kegunaan manajer paket Arch Linux.
> Lihat juga: `pacman`.
> Informasi lebih lanjut: <https://manned.org/pacman.8>.

- Pasang suatu atau beberapa paket atau dari kumpulan berkas:

`sudo pacman -U {{jalan/menuju/paket1.pkg.tar.zst}} {{jalan/menuju/paket2.pkg.tar.zst}}`

- Pasang paket tanpa konfirmasi:

`sudo pacman -U --noconfirm {{jalan/menuju/paket.pkg.tar.zst}}`

- Timpa berkas-berkas sistem yang bentrok selama pemasangan paket:

`sudo pacman -U --overwrite {{jalan/menuju/berkas}} {{jalan/menuju/paket.pkg.tar.zst}}`

- Pasang paket, melewati pemeriksaan versi [d]ependensi:

`sudo pacman -Ud {{jalan/menuju/paket.pkg.tar.zst}}`

- Tampilkan ([p]rint) daftar paket yang akan terpengaruh (tidak menginstal paket apa pun):

`pacman -Up {{jalan/menuju/paket.pkg.tar.zst}}`

- Tampilkan bantuan:

`pacman -Uh`
