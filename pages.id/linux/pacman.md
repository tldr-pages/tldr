# pacman

> Kegunaan manajer paket Arch Linux.
> Guarda anche: `pacman-database`, `pacman-deptest`, `pacman-files`, `pacman-key`,  `pacman-mirrors`, `pacman-query`, `pacman-remove`, `pacman-sync`, `pacman-upgrade`.
> Informasi lebih lanjut: <https://man.archlinux.org/man/pacman.8>.

- Sinkronkan dan perbarui semua paket:

`sudo pacman -Syu`

- Instal paket baru:

`sudo pacman -S {{nama_paket}}`

- Hapus paket beserta dependensinya:

`sudo pacman -Rs {{nama_paket}}`

- Cari paket dalam database berdasarkan regular expression atau kata kunci:

`pacman -Ss "{{pola_pencarian}}"`

- Tampilkan daftar paket dan versi yang diinstal:

`pacman -Q`

- Tampilkan daftar paket dan versi yang diinstal secara eksplisit:

`pacman -Qe`

- Tampilkan daftar paket yatim piatu (diinstal sebagai dependensi namun tidak dibutuhkan oleh paket apa pun):

`pacman -Qtdq`

- Kosongkan seluruh cache pacman:

`sudo pacman -Scc`
