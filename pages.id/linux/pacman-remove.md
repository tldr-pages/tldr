# pacman --remove

> Kegunaan manajer paket Arch Linux.
> Informasi lebih lanjut: <https://manned.org/pacman.8>.

- Hapus paket beserta dependensinya:

`sudo pacman -Rs {{paket}}`

- Hapus paket beserta dependensi dan file konfigurasi-nya:

`sudo pacman -Rsn {{paket}}`

- Hapus tanpa konfirmasi:

`sudo pacman -R --noconfirm {{paket}}`

- Hapus paket yatim piatu (diinstal sebagai dependensi namun tidak dibutuhkan oleh paket apa pun):

`sudo pacman -Rsn $(pacman -Qdtq)`

- Hapus paket dan semua paket yang bergantung pada paket tersebut:

`sudo pacman -Rc {{paket}}`

- Tampilkan daftar paket yang akan terpengaruh (tidak menghapus paket apa pun):

`pacman -Rp {{paket}}`

- Tampilkan bantuan untuk subperintah ini:

`pacman -Rh`
