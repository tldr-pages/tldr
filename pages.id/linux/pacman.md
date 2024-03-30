# pacman

> Kegunaan manajer paket Arch Linux.
> Guarda anche: `pacman-database`, `pacman-deptest`, `pacman-files`, `pacman-key`, `pacman-mirrors`, `pacman-query`, `pacman-remove`, `pacman-sync`, `pacman-upgrade`.
> Lihat <https://wiki.archlinux.org/title/Pacman/Rosetta> untuk daftar perintah dalam manajer paket lain yang menyerupai perintah `pacman`.
> Informasi lebih lanjut: <https://man.archlinux.org/man/pacman.8>.

- Sinkronkan dan perbarui semua paket:

`sudo pacman -Syu`

- Pasang suatu paket baru:

`sudo pacman -S {{paket}}`

- Hapus paket beserta dependensinya:

`sudo pacman -Rs {{paket}}`

- Cari pangkalan data untuk nama-nama paket yang mengandung suatu berkas secara spesifik:

`pacman -F "{{nama_berkas}}"`

- Tampilkan daftar paket dan versi yang diinstal:

`pacman -Q`

- Tampilkan daftar paket dan versi yang diinstal secara eksplisit:

`pacman -Qe`

- Tampilkan daftar paket yatim piatu (diinstal sebagai dependensi namun tidak dibutuhkan oleh paket apa pun):

`pacman -Qtdq`

- Kosongkan seluruh cache pacman:

`sudo pacman -Scc`
