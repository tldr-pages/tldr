# pacman --remove

> Kegunaan manajer paket Arch Linux.
> Informasi lebih lanjut: <https://man.archlinux.org/man/pacman.8>.

- Hapus paket beserta dependensinya:

`sudo pacman --remove --recursive {{nama_paket}}`

- Hapus paket beserta dependensi dan file konfigurasi-nya:

`sudo pacman --remove --recursive --nosave {{nama_paket}}`

- Hapus tanpa konfirmasi:

`sudo pacman --remove --noconfirm {{nama_paket}}`

- Hapus paket yatim piatu (diinstal sebagai dependensi namun tidak dibutuhkan oleh paket apa pun):

`sudo pacman --remove --recursive --nosave $(pacman --query --unrequired --deps --quiet)`

- Hapus paket dan semua paket yang bergantung pada paket tersebut:

`sudo pacman --remove --cascade {{nama_paket}}`

- Tampilkan daftar paket yang akan terpengaruh (tidak menghapus paket apa pun):

`pacman --remove --print {{nama_paket}}`

- Tampilkan bantuan untuk subperintah ini:

`pacman --remove --help`
