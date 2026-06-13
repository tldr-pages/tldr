# pacman --query

> Kegunaan manajer paket Arch Linux.
> Lihat juga: `pacman`.
> Informasi lebih lanjut: <https://manned.org/pacman.8>.

- Tampilkan daftar paket yang diinstal beserta versinya:

`pacman -Q`

- Tampilkan daftar paket yang diinstal beserta versinya secara eksplisit:

`pacman -Qe`

- Temukan paket mana yang memiliki file:

`pacman -Qo {{namafile}}`

- Tampilkan informasi paket yang diinstal:

`pacman -Qi {{nama_paket}}`

- Tampilkan daftar file yang dimiliki oleh paket:

`pacman -Ql {{nama_paket}}`

- Tampilkan daftar paket yatim piatu (diinstal sebagai dependensi namun tidak dibutuhkan oleh paket apa pun):

`pacman -Qdtq`

- Tampilkan daftar paket yang diinstal tidak ditemukan di tempat penyimpanan:

`pacman -Qm`

- Tampilkan daftar paket usang:

`pacman -Qu`
