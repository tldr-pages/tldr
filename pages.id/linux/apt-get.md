# apt-get

> Manajemen paket untuk Debian dan Ubuntu.
> Cari paket menggunakan `apt-cache`.
> Informasi lebih lanjut: <https://manpages.debian.org/latest/apt/apt-get.8.html>.

- Perbarui daftar paket yang tersedia beserta versinya (hal ini direkomendasikan untuk dijalankan sebelum menjalankan perintah `apt-get` yang lain):

`apt-get update`

- Pasang sebuah paket, atau perbarui ke versi terbaru yang tersedia:

`apt-get install {{paket}}`

- Hapus sebuah paket:

`apt-get remove {{paket}}`

- Hapus sebuah paket dan file konfigurasinya:

`apt-get purge {{paket}}`

- Perbarui semua paket yang terpasang ke versi terbaru yang tersedia:

`apt-get upgrade`

- Bersihkan repositori lokal, hapus file paket (`.deb`) yang sebelumnya gagal diunduh dan tidak bisa diunduh kembali:

`apt-get autoclean`

- Hapus semua paket yang tidak diperlukan kembali:

`apt-get autoremove`

- Perbarui paket yang terinstal (mirip `upgrade`), namun hapus paket yang tidak dipakai kembali dan pasang paket tambahan untuk memenuhi dependensi baru:

`apt-get dist-upgrade`
