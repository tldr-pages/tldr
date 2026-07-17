# apt-get

> Manajemen paket untuk Debian dan Ubuntu.
> Cari paket menggunakan `apt-cache`.
> Disarankan untuk menggunakan `apt` saat menggunakan perintah ini secara interaktif dalam Ubuntu versi 16.04 dan seterusnya.
> Informasi lebih lanjut: <https://manned.org/apt-get.8>.

- Perbarui daftar paket yang tersedia beserta versinya (direkomendasikan untuk menggunakan perintah ini sebelum perintah `apt-get` lainnya):

`sudo apt-get update`

- Pasang atau perbarui sebuah paket menuju versi terbaru:

`sudo apt-get install {{nama_paket}}`

- Hapus paket yang terpasang sebelumnya:

`sudo apt-get remove {{nama_paket}}`

- Hapus paket yang terpasang sebelumnya, beserta seluruh berkas konfigurasi yang dibentuk oleh paket tersebut:

`sudo apt-get purge {{nama_paket}}`

- Perbarui seluruh paket yang terpasang ke versi terbaru:

`sudo apt-get upgrade`

- Bersihkan repositori lokal, hapus berkas-berkas paket (`.deb`) yang sebelumnya gagal diunduh dan tak bisa diunduh kembali:

`sudo apt-get autoclean`

- Hapus seluruh paket yang tidak diperlukan kembali:

`sudo apt-get autoremove`

- Perbarui kumpulan paket yang terinstal (mirip `upgrade`), namun hapus paket yang tidak dipakai kembali dan pasang paket tambahan untuk memenuhi dependensi baru:

`sudo apt-get dist-upgrade`
