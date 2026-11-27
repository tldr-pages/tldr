# 7zr

> Pengarsip berkas dengan rasio kompresi yang tinggi.
> Serupa dengan `7z` namun mendukung format berkas arsip 7z saja.
> Informasi lebih lanjut: <https://manned.org/7zr>.

- T[a]mbahkan sebuah berkas atau direktori ke dalam arsip baru atau saat ini:

`7zr a {{jalan/menuju/arsip.7z}} {{jalan/menuju/berkas_atau_direktori}}`

- Sandikan berkas arsip saat ini (beserta nama-nama berkas yang terkandung di dalamnya):

`7zr a {{jalan/menuju/arsip_terenkripsi.7z}} -p{{kata sandi}} -mhe={{on}} {{jalan/menuju/arsip.7z}}`

- E[x]trak berkas arsip dengan mempertahankan struktur direktori asli:

`7zr x {{jalan/menuju/arsip.7z}}`

- E[x]trak berkas arsip ke dalam direktori yang ditentukan:

`7zr x {{jalan/menuju/arsip.7z}} -o{{jalan/menuju/direktori}}`

- E[x]trak berkas arsip menuju `stdout`:

`7zr x {{jalan/menuju/arsip.7z}} -so`

- [l]ihat daftar isi suatu berkas arsip:

`7zr l {{jalan/menuju/arsip.7z}}`

- Atur tingkat kompresi pada berkas arsip (tingkat lebih tinggi akan mengurangi lebih banyak beban berkas, namun lebih lambat):

`7zr a {{jalan/menuju/arsip.7z}} -mx={{0|1|3|5|7|9}} {{jalan/menuju/berkas_atau_direktori}}`
