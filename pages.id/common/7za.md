# 7za

> Pengarsip berkas dengan rasio kompresi yang tinggi.
> Serupa dengan `7z` namun mendukung lebih sedikit format berkas arsip dan dapat digunakan lintas sistem operasi.
> Informasi lebih lanjut: <https://manned.org/7za>.

- T[a]mbahkan sebuah berkas atau direktori ke dalam arsip baru atau saat ini:

`7za a {{jalan/menuju/arsip.7z}} {{jalan/menuju/berkas_atau_direktori}}`

- Sandikan berkas arsip saat ini (beserta nama-nama berkas yang terkandung di dalamnya):

`7za a {{jalan/menuju/arsip_terenkripsi.7z}} -p{{kata sandi}} -mhe={{on}} {{jalan/menuju/arsip.7z}}`

- E[x]trak berkas arsip dengan mempertahankan struktur direktori asli:

`7za x {{jalan/menuju/arsip.7z}}`

- E[x]trak berkas arsip ke dalam direktori yang ditentukan:

`7za x {{jalan/menuju/arsip.7z}} -o{{jalan/menuju/direktori}}`

- E[x]trak berkas arsip menuju `stdout`:

`7za x {{jalan/menuju/arsip.7z}} -so`

- [a]rsipkan berkas atau direktori menggunakan format arsip tertentu:

`7za a -t{{7z|bzip2|gzip|lzip|tar|...}} {{jalan/menuju/arsip.7z}} {{jalan/menuju/berkas_atau_direktori}}`

- [l]ihat daftar isi dari sebuah berkas arsip:

`7za l {{jalan/menuju/arsip.7z}}`

- Atur tingkat kompresi pada berkas arsip (tingkat lebih tinggi akan mengurangi lebih banyak beban berkas, namun lebih lambat):

`7za a {{jalan/menuju/arsip.7z}} -mx={{0|1|3|5|7|9}} {{jalan/menuju/berkas_atau_direktori}}`
