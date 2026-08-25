# ast-grep

> Cari, periksa, dan tuilis ulang kode menggunakan pola pencarian AST.
> Informasi lebih lanjut: <https://ast-grep.github.io/reference/cli.html>.

- Cari untuk suatu pola dalam kumpulan berkas:

`ast-grep run {{[-p|--pattern]}} '{{pola}}' {{jalan/menuju/berkas}}`

- Cari untuk suatu pola dalam bahasa pemrograman tertentu:

`ast-grep run {{[-p|--pattern]}} '{{pola}}' {{[-l|--lang]}} {{python}} {{jalan/menuju/direktori}}`

- Tulis ulang kode berdasarkan kriteria pola pencarian:

`ast-grep run {{[-p|--pattern]}} '{{pola}}' {{[-r|--rewrite]}} '{{kata_pengganti}}' {{jalan/menuju/berkas}}`

- Jalankan peraturan pencarian menurut suatu berkas konfigurasi:

`ast-grep scan {{[-r|--rule]}} {{jalan/menuju/peraturan.yml}} {{jalan/menuju/direktori}}`

- Lakukan proses pencarian dan penulisan ulang kode secara interaktif:

`ast-grep run {{[-p|--pattern]}} '{{pola}}' {{[-i|--interactive]}} {{jalan/menuju/direktori}}`

- Tampilkan bantuan untuk suatu subperintah:

`ast-grep {{run}} {{[-h|--help]}}`
