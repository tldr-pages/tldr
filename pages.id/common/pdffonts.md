# pdffonts

> Penampil informasi fon (font) berkas Portable Document Format (PDF).
> Informasi lebih lanjut: <https://www.xpdfreader.com/pdffonts-man.html>.

- Cetak informasi fon berkas PDF:

`pdffonts {{jalan/ke/berkas.pdf}}`

- Tentukan kata sandi pengguna (user password) untuk berkas PDF guna melewati batasan keamanan:

`pdffonts -upw {{kata_sandi}} {{jalan/ke/berkas.pdf}}`

- Tentukan kata sandi pemilik (owner password) untuk berkas PDF guna melewati batasan keamanan:

`pdffonts -opw {{kata_sandi}} {{jalan/ke/berkas.pdf}}`

- Cetak informasi tambahan mengenai lokasi fon yang akan digunakan saat berkas PDF dirasterisasi (rasterized):

`pdffonts -loc {{jalan/ke/berkas.pdf}}`

- Cetak informasi tambahan mengenai lokasi fon yang akan digunakan saat berkas PDF dikonversi ke PostScript:

`pdffonts -locPS {{jalan/ke/berkas.pdf}}`
