# apt

> Manajer paket untuk distribusi Linux berbasis Debian.
> Pengganti apt-get yang direkomendasikan ketika digunakan secara interaktif di Ubuntu versi 16.04 atau yang lebih baru.
> Informasi lebih lanjut: <https://manpages.debian.org/latest/apt/apt.8.html>.

- Memperbarui daftar paket yang tersedia dan versinya (direkomendasikan untuk menggunakan perintah ini sebelum perintah `apt` lainnya.):

`sudo apt update`

- Mencari paket:

`apt search {{paket}}`

- Memperlihatkan paket yang tersedia:

`apt show {{paket}}`

- Menginstal sebuah paket, atau memperbarui paket ke versi terbaru:

`sudo apt install {{paket}}`

- Menghapus sebuah paket (menggunakan `purge` juga menghapus file konfigurasi):

`sudo apt remove {{paket}}`

- Memperbarui paket yang terinstal ke versi terbaru:

`sudo apt upgrade`

- Memperlihatkan daftar semua paket:

`apt list`

- Memperlihatkan daftar paket yang terinstal:

`apt list --installed`
