# apk

> Alat manajemen paket Alpine Linux.
> Informasi lebih lanjut: <https://wiki.alpinelinux.org/wiki/Alpine_Package_Keeper>.

- Lakukan update indeks repositori dan upgrade semua paket:

`apk upgrade {{[-U|--update-cache]}}`

- Lakukan update indeks repositori saja:

`apk update`

- Lakukan install paket baru:

`apk add {{package}}`

- Lakukan hapus paket:

`apk del {{package}}`

- Perbaiki/Install ulang paket tanpa memodifikasi dependensi utama:

`apk fix {{package}}`

- Lakukan cari paket dengan kata kunci pada namanya dan tampilkan hasil beserta deskripsi:

`apk search {{[-v|--verbose]}} {{keyword}}`

- Lakukan cari paket dengan kata kunci pada deskripsinya:

`apk search {{[-d|--description]}} {{keyword}}`

- Tampilkan informasi tentang paket tertentu:

`apk info {{package}}`
