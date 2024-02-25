# apt-get

> Manajemen paket untuk Debian dan Ubuntu.
> Cari paket menggunakan `apt-cache`.
> Informasi lebih lanjut: <https://manpages.debian.org/latest/apt/apt-get.8.html>.

- Memperbarui daftar paket yang tersedia beserta versinya (hal ini direkomendasikan untuk dijalankan sebelum menjalankan perintah `apt-get` yang lain):

`apt-get update`

- Menginstal sebuah paket, atau memperbaruinya ke versi terbaru yang tersedia:

`apt-get install {{package}}`

- Menghapus sebuah paket:

`apt-get remove {{package}}`

- Menghapus sebuah paket dan file konfigurasinya:

`apt-get purge {{package}}`

- Memperbarui semua paket yang terinstal ke versi terbaru yang tersedia:

`apt-get upgrade`

- Membersihkan repositori lokal - menghapus file paket (`.deb`) yang sebelumnya gagal didownload dan tidak bisa di download lagi:

`apt-get autoclean`

- Menghapus semua paket yang tidak diperlukan lagi:

`apt-get autoremove`

- Memperbarui paket yang terinstal (mirip `upgrade`), tapi bedanya ini menghapus paket yang tidak dipakai lagi dan menginstal paket tambahan untuk memenuhi dependensi baru:

`apt-get dist-upgrade`
