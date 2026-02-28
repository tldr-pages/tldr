# apache2ctl

> Mengelola server web Apache HTTP.
> Perintah ini tersedia di sistem operasi berbasis Debian, untuk sistem operasi berbasis RHEL lihat `httpd`.
> Informasi lebih lanjut: <https://manned.org/apache2ctl>.

- Jalankan daemon Apache. Tampilkan pesan jika daemon sudah berjalan:

`sudo apache2ctl start`

- Hentikan daemon Apache:

`sudo apache2ctl stop`

- Jalankan ulang daemon Apache:

`sudo apache2ctl restart`

- Lakukan Uji sintaks dari file konfigurasi:

`sudo apache2ctl -t`

- Tampilkan daftar modul yang dimuat:

`sudo apache2ctl -M`
