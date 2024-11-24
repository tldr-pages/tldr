# htpasswd

> Buat dan atur isi berkas-berkas htpasswd untuk melindungi kumpulan direktori yang diakses oleh peladen web menggunakan metode autentikasi sederhana/basic.
> Informasi lebih lanjut: <https://httpd.apache.org/docs/current/programs/htpasswd.html>.

- Buat/timpa isi berkas htpasswd:

`htpasswd -c {{jalan/menuju/berkas}} {{username}}`

- Tambahkan atau mutakhirkan konfigurasi bagi suatu akun pengguna (dalam mengakses layanan web) ke dalam berkas htpasswd:

`htpasswd {{jalan/menuju/berkas}} {{username}}`

- Tambahkan suatu akun pengguna kepada berkas htpasswd dalam mode batch, dengan melewati proses pemasukkan kata sandi secara interaktif (untuk penggunaan dalam skrip syel):

`htpasswd -b {{jalan/menuju/berkas}} {{username}} {{kata_sandi}}`

- Hapus konfigurasi akses suatu akun pengguna dari isi suatu berkas htpasswd:

`htpasswd -D {{jalan/menuju/berkas}} {{username}}`

- Lakukan proses verifikasi kata sandi bagi suatu akun pengguna:

`htpasswd -v {{jalan/menuju/berkas}} {{username}}`

- Tampilkan suatu string berisikan username (akun pengguna, dalam plain text) dan kata sandi (dalam hash md5):

`htpasswd -nbm {{username}} {{kata_sandi}}`
