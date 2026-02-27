# apk

> Alat manajemen paket Alpine Linux.
> Informasi lebih lanjut: <https://wiki.alpinelinux.org/wiki/Alpine_Package_Keeper>.

- Perbarui indeks repositori dan upgrade semua paket:

`apk upgrade {{[-U|--update-cache]}}`

- Perbarui indeks repositori saja:

`apk update`

- Pasang suatu paket baru:

`apk add {{package}}`

- Hapus pemasangan paket:

`apk del {{package}}`

- Perbaiki/pasang ulang paket tanpa memodifikasi dependensi utama:

`apk fix {{package}}`

- Cari paket dengan kata kunci pada namanya dan tampilkan hasil beserta deskripsi:

`apk search {{[-v|--verbose]}} {{keyword}}`

- Cari paket dengan kata kunci pada deskripsinya:

`apk search {{[-d|--description]}} {{keyword}}`

- Tampilkan informasi tentang paket tertentu:

`apk info {{package}}`
