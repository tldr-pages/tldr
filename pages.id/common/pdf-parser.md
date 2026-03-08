# pdf-parser

> Mengidentifikasi elemen-elemen fundamental dari sebuah berkas PDF tanpa merendernya (rendering).
> Informasi lebih lanjut: <https://blog.didierstevens.com/programs/pdf-tools/>.

- Menampilkan statistik untuk sebuah berkas PDF:

`pdf-parser {{[-a|--stats]}} {{jalan/ke/berkas.pdf}}`

- Menampilkan objek dengan tipe tertentu (/Font, /URI, ...) dalam sebuah berkas PDF:

`pdf-parser {{[-t|--type]}} {{/tipe_objek}} {{jalan/ke/berkas.pdf}}`

- Mencari string (untaian teks) dalam objek-objek tidak langsung (indirect objects):

`pdf-parser {{[-s|--search]}} {{string_pencarian}} {{jalan/ke/berkas.pdf}}`
