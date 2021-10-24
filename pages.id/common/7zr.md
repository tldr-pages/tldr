# 7zr

> Pengarsip file dengan rasio kompresi yang tinggi.
> Serupa dengan `7z` namun mendukung format file arsip `.7z` saja.
> Informasi lebih lanjut: <https://www.7-zip.org>.

- Meng[a]rsipkan sebuah file atau direktori:

`7zr a {{jalan/menuju/arsip.7z}} {{jalan/menuju/file_atau_direktori}}`

- Mengenkripsi sebuah file arsip (termasuk nama-nama file yang terkandung di dalamnya):

`7zr a {{jalan/menuju/arsip_terenkripsi.7z}} -p{{kata sandi}} -mhe=on {{jalan/menuju/arsip.7z}}`

- Mengekstrak sebuah file arsip dengan mempertahankan struktur direktori asli:

`7zr x {{jalan/menuju/arsip.7z}}`

- Mengekstrak sebuah file arsip ke dalam direktori yang ditentukan:

`7zr x {{jalan/menuju/arsip.7z}} -o{{jalan/menuju/direktori}}`

- Mengekstrak sebuah file arsip menuju stdout:

`7zr x {{jalan/menuju/arsip.7z}} -so`

- Me[l]ihat daftar isi dari sebuah file arsip:

`7zr l {{jalan/menuju/arsip.7z}}`

- Mengetahui daftar format file arsip yang didukung:

`7zr i`
