# dnf

> Manajer paket untuk distribusi Linux RHEL, Fedora, dan CentOS (pengganti yum).
> Lihat <https://wiki.archlinux.org/title/Pacman/Rosetta> untuk daftar perintah dalam manajer paket lain yang menyerupai perintah `dnf`.
> Informasi lebih lanjut: <https://dnf.readthedocs.io>.

- Perbarui seluruh paket yang terpasang ke versi terbaru:

`sudo dnf upgrade`

- Cari paket yang tersedia dengan kata kunci tertentu:

`dnf search {{kata_kunci1 kata_kunci2 ...}}`

- Tampilkan informasi tentang suatu paket:

`dnf info {{paket}}`

- Pasang sebuah paket (gunakan `-y` jawab untuk ya semua pertanyaan):

`sudo dnf install {{paket1 paket2 ...}}`

- Hapus sebuah paket:

`sudo dnf remove {{paket1 paket2 ...}}`

- Tampilkan daftar semua paket yang telah terpasang:

`dnf list --installed`

- Temukan paket mana yang menyediakan perintah tertentu:

`dnf provides {{perintah}}`

- Lihat informasi riwayat penugasan `dnf`:

`dnf history`
