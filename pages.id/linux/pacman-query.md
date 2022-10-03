# pacman --query

> Kegunaan manajer paket Arch Linux.
> Informasi lebih lanjut: <https://man.archlinux.org/man/pacman.8>.

- Daftar paket yang diinstal beserta versinya:

`pacman --query`

- Daftar paket yang diinstal beserta versinya secara eksplisit:

`pacman --query --explicit`

- Temukan paket mana yang memiliki file:

`pacman --query --owns {{namafile}}`

- Tampilkan informasi paket yang diinstal:

`pacman --query --info {{nama_paket}}`

- Daftar file yang dimiliki oleh paket:

`pacman --query --list {{nama_paket}}`

- Daftar paket yatim piatu (diinstal sebagai dependensi namun tidak dibutuhkan oleh paket apa pun):

`pacman --query --unrequired --deps --quiet`

- Daftar paket yang diinstal tidak ditemukan di tempat penyimpanan:

`pacman --query --foreign`

- Daftar paket usang:

`pacman --query --upgrades`
