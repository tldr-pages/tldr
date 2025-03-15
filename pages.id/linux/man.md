# man

> Format dan tampilkan halaman manual.
> Informasi lebih lanjut: <https://manned.org/man>.

- Tampilkan halaman manual untuk sebuah perintah:

`man {{perintah}}`

- Tampilkan halaman manual untuk perintah dari bagian 7:

`man {{7}} {{perintah}}`

- Tampilkan semua bagian yang tersedia untuk suatu perintah:

`man -{{[-f|--whatis]}} {{perintah}}`

- Tampilkan jalur yang dicari untuk halaman manual:

`man {{[-w|--path]}}`

- Tampilkan lokasi sebuah halaman manual alih-alih halaman manual itu sendiri:

`man {{[-w|--where]}} {{perintah}}`

- Tampilkan halaman manual menggunakan locale tertentu:

`man {{[-L|--locale]}} {{locale}} {{perintah}}`

- Cari halaman manual yang berisi string pencarian:

`man {{[-k|--apropos]}} "{{string_pencarian}}"`
