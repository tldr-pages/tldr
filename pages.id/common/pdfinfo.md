# pdfinfo

> Penampil informasi berkas Portable Document Format (PDF).
> Informasi lebih lanjut: <https://www.xpdfreader.com/pdfinfo-man.html>.

- Cetak informasi berkas PDF:

`pdfinfo {{jalan/ke/berkas.pdf}}`

- Tentukan kata sandi pengguna (user password) untuk berkas PDF guna melewati batasan keamanan:

`pdfinfo -upw {{kata_sandi}} {{jalan/ke/berkas.pdf}}`

- Tentukan kata sandi pemilik (owner password) untuk berkas PDF guna melewati batasan keamanan:

`pdfinfo -opw {{kata_sandi}} {{jalan/ke/berkas.pdf}}`
