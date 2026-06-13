# pacman --remove

> Kegunaan manajer paket Arch Linux.
> Lihat juga: `pacman`.
> Informasi lebih lanjut: <https://manned.org/pacman.8>.

- Hapus paket beserta dependensinya:

`sudo pacman -Rs {{nama_paket}}`

- Hapus paket beserta dependensi dan file konfigurasi-nya:

`sudo pacman -Rsn {{nama_paket}}`

- Hapus tanpa konfirmasi:

`sudo pacman -R --noconfirm {{nama_paket}}`

- Hapus paket yatim piatu (diinstal sebagai dependensi namun tidak dibutuhkan oleh paket apa pun):

`sudo pacman -Rsn $(pacman -Qdtq)`

- Hapus paket dan semua paket yang bergantung pada paket tersebut:

`sudo pacman -Rc {{nama_paket}}`

- Tampilkan daftar paket yang akan terpengaruh (tidak menghapus paket apa pun):

`pacman -Rp {{nama_paket}}`

- Tampilkan bantuan untuk subperintah ini:

`pacman -Rh`
