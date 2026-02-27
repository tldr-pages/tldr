# apachectl

> Kontrol server HTTP Apache.
> Informasi lebih lanjut: <https://manned.org/apachectl>.

- Jalankan peladen:

`sudo apachectl start`

- Jalankan ulang peladen:

`sudo apachectl restart`

- Hentikan peladen:

`sudo apachectl stop`

- Lakukan uji validitas file konfigurasi:

`apachectl configtest`

- Periksa status server (membutuhkan browser lynx):

`apachectl status`

- Lakukan muat ulang konfigurasi tanpa memutus koneksi:

`sudo apachectl graceful`

- Tampilkan konfigurasi lengkap Apache (tidak selalu didukung):

`apachectl -S`

- Tampilkan bantuan:

`apachectl -h`
