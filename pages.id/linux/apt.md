# apt

> Manajer paket untuk distribusi Linux berbasis Debian.
> Pengganti `apt-get` yang direkomendasikan ketika digunakan secara interaktif di Ubuntu versi 16.04 atau yang lebih baru.
> Lihat <https://wiki.archlinux.org/title/Pacman/Rosetta> untuk daftar perintah dalam manajer paket lain yang menyerupai perintah `apt`.
> Informasi lebih lanjut: <https://manned.org/apt.8>.

- Perbarui daftar paket yang tersedia dan versinya (direkomendasikan untuk menggunakan perintah ini sebelum perintah `apt` lainnya.):

`sudo apt update`

- Cari paket yang tersedia dengan nama atau deskripsi tertentu:

`apt search {{nama_atau_deskripsi_paket}}`

- Tampilkan informasi tentang suatu paket:

`apt show {{nama_paket}}`

- Pasang atau perbarui sebuah paket menuju versi terbaru:

`sudo apt install {{nama_paket}}`

- Hapus paket yang terpasang sebelumnya (gunakan `sudo apt purge` untuk sekaligus menghapus file konfigurasi yang dibuat oleh paket tersebut):

`sudo apt remove {{nama_paket}}`

- Perbarui seluruh paket yang terpasang ke versi terbaru:

`sudo apt upgrade`

- Tampilkan daftar semua paket yang tersedia di dalam repositori:

`apt list`

- Tampilkan daftar paket yang telah terpasang:

`apt list {{[-i|--installed]}}`
