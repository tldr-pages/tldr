# 7zr

> Pengarsip file dengan rasio kompresi yang tinggi.
> Serupa dengan `7z` namun mendukung format file arsip 7z saja.
> Informasi lebih lanjut: <https://manned.org/7zr>.

- T[a]mbahkan sebuah file atau direktori ke dalam arsip baru atau saat ini:

`7zr a {{jalan/menuju/arsip.7z}} {{jalan/menuju/file_atau_direktori}}`

- Enkripsi file arsip saat ini (termasuk nama-nama file yang terkandung di dalamnya):

`7zr a {{jalan/menuju/arsip_terenkripsi.7z}} -p{{kata sandi}} -mhe={{on}} {{jalan/menuju/arsip.7z}}`

- E[x]trak file arsip dengan mempertahankan struktur direktori asli:

`7zr x {{jalan/menuju/arsip.7z}}`

- E[x]trak file arsip ke dalam direktori yang ditentukan:

`7zr x {{jalan/menuju/arsip.7z}} -o{{jalan/menuju/direktori}}`

- E[x]trak file arsip menuju `stdout`:

`7zr x {{jalan/menuju/arsip.7z}} -so`

- [l]ihat daftar isi dari sebuah file arsip:

`7zr l {{jalan/menuju/arsip.7z}}`

- Atur tingkat kompresi pada file arsip (tingkat lebih tinggi memproduksi file arsip lebih kecil dengan proses kompresi yang lebih lama):

`7zr a {{jalan/menuju/arsip.7z}} -mx={{0|1|3|5|7|9}} {{jalan/menuju/file_atau_direktori}}`
