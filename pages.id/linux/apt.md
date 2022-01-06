# apt

> Manajer paket untuk distribusi Linux berbasis Debian.
> Pengganti `apt-get` yang direkomendasikan ketika digunakan secara interaktif di Ubuntu versi 16.04 atau yang lebih baru.
> Informasi lebih lanjut: <https://manpages.debian.org/latest/apt/apt.8.html>.

- Memperbarui daftar paket yang tersedia dan versinya (direkomendasikan untuk menggunakan perintah ini sebelum perintah `apt` lainnya.):

`sudo apt update`

- Mencari paket yang tersedia dengan nama atau deskripsi tertentu:

`apt search {{nama_atau_deskripsi_paket}}`

- Memperlihatkan informasi tentang suatu paket:

`apt show {{nama_paket}}`

- Menginstal sebuah paket, atau memperbarui paket ke versi terbaru:

`sudo apt install {{nama_paket}}`

- Menghapus sebuah paket (gunakan `sudo apt purge` untuk menghapus paket beserta file konfigurasinya):

`sudo apt remove {{nama_paket}}`

- Memperbarui seluruh paket yang terpasang ke versi terbaru:

`sudo apt upgrade`

- Memperlihatkan daftar semua paket yang tersedia di dalam repositori:

`apt list`

- Memperlihatkan daftar paket yang telah terpasang:

`apt list --installed`
