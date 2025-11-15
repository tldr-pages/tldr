# dnf5

> Manajer paket untuk distribusi Linux RHEL, Fedora, dan CentOS (pengganti dnf5, yang juga dirancang sebagai pengganti yum).
> DNF5 adalah hasil penulisan ulang program manajemen paket DNF dalam C++ dengan performa yang lebih baik dan ukuran program yang lebih kecil.
> Lihat <https://wiki.archlinux.org/title/Pacman/Rosetta> untuk daftar perintah dalam manajer paket lain yang menyerupai perintah `dnf5`.
> Informasi lebih lanjut: <https://dnf5.readthedocs.io>.

- Perbarui seluruh paket yang terpasang ke versi terbaru:

`sudo dnf5 upgrade`

- Cari paket yang tersedia dengan kata-kata kunci tertentu:

`dnf5 search {{kata_kunci1 kata_kunci2 ...}}`

- Tampilkan informasi tentang suatu paket:

`dnf5 info {{paket}}`

- Pasang kumpulan paket (gunakan `-y` jawab untuk ya semua pertanyaan):

`sudo dnf5 install {{paket1 paket2 ...}}`

- Hapus kumpulan paket:

`sudo dnf5 remove {{paket1 paket2 ...}}`

- Tampilkan daftar semua paket yang telah terpasang:

`dnf5 list --installed`

- Temukan paket mana yang menyediakan perintah tertentu:

`dnf5 provides {{perintah}}`

- Hapus atau tandai data cache sebagai kedaluwarsa:

`sudo dnf5 clean all`
