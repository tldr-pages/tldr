# psalm

> Suatu alat analisis kode statis yang dapat dimanfaatkan untuk mencari kesalahan pada aplikasi berbasis PHP.
> Informasi lebih lanjut: <https://psalm.dev>.

- Buat sebuah berkas konfigurasi Psalm baru:

`psalm --init`

- Periksa kesalahan pada direktori saat ini:

`psalm`

- Periksa kesalahan pada suatu direktori atau berkas:

`psalm {{jalan/menuju/berkas_atau_direktori}}`

- Periksa kesalahan menggunakan suatu berkas konfigurasi:

`psalm --config {{jalan/menuju/psalm.xml}}`

- Lampirkan penemuan-penemuan informasional ke dalam luaran hasil pengecekan:

`psalm --show-info`

- Periksa suatu proyek dan tampilkan hasil statistika:

`psalm --stats`

- Periksa suatu proyek secara paralel denan 4 thread pemrosesan:

`psalm --threads {{4}}`
