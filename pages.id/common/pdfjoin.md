# pdfjoin

> Utilitas penggabungan PDF berbasis pdfjam.
> Informasi lebih lanjut: <https://github.com/pdfjam/pdfjam-extras>.

- Gabungkan dua berkas PDF menjadi satu dengan akhiran (suffix) bawaan "joined":

`pdfjoin {{jalan/ke/berkas1.pdf}} {{jalan/ke/berkas2.pdf}}`

- Gabungkan halaman pertama dari setiap berkas yang diberikan menjadi satu:

`pdfjoin {{jalan/ke/berkas1.pdf jalan/ke/berkas2.pdf ...}} {{1}} --outfile {{berkas_keluaran}}`

- Simpan halaman 3 sampai 5 diikuti dengan halaman 1 ke sebuah berkas PDF baru dengan akhiran kustom:

`pdfjoin {{jalan/ke/berkas.pdf}} {{3-5,1}} --suffix {{diatur_ulang}}`

- Gabungkan sub-rentang (subrange) halaman dari dua berkas PDF:

`pdfjoin /{{jalan/ke/berkas1.pdf}} {{2-}} {{berkas2}} {{last-3}} --outfile {{berkas_keluaran}}`
