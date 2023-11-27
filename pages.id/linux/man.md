# man

> Format dan tampilkan halaman manual.
> Informasi lebih lanjut: <https://manned.org/man>.

- Tampilkan halaman manual untuk sebuah perintah:

`man {{perintah}}`

- Tampilkan halaman manual untuk perintah dari bagian 7:

`man {{7}} {{perintah}}`

- Tampilkan semua bagian yang tersedia untuk suatu perintah:

`man --whatis {{perintah}}`

- Tampilkan jalur yang dicari untuk halaman manual:

`man --path`

- Tampilkan lokasi sebuah halaman manual alih-alih halaman manual itu sendiri:

`man --where {{perintah}}`

- Tampilkan halaman manual menggunakan locale tertentu:

`man --locale={{locale}} {{perintah}}`

- Cari halaman manual yang berisi string pencarian:

`man --apropos "{{string_pencarian}}"`
