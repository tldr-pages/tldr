# pacman --query

> Kegunaan manajer paket Arch Linux.
> Guarda anche: `pacman`.
> Informasi lebih lanjut: <https://man.archlinux.org/man/pacman.8>.

- Tampilkan daftar paket yang diinstal beserta versinya:

`pacman --query`

- Tampilkan daftar paket yang diinstal beserta versinya secara eksplisit:

`pacman --query --explicit`

- Temukan paket mana yang memiliki file:

`pacman --query --owns {{namafile}}`

- Tampilkan informasi paket yang diinstal:

`pacman --query --info {{nama_paket}}`

- Tampilkan daftar file yang dimiliki oleh paket:

`pacman --query --list {{nama_paket}}`

- Tampilkan daftar paket yatim piatu (diinstal sebagai dependensi namun tidak dibutuhkan oleh paket apa pun):

`pacman --query --unrequired --deps --quiet`

- Tampilkan daftar paket yang diinstal tidak ditemukan di tempat penyimpanan:

`pacman --query --foreign`

- Tampilkan daftar paket usang:

`pacman --query --upgrades`
