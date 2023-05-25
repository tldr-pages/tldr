# 7za

> Pengarsip file dengan rasio kompresi yang tinggi.
> Serupa dengan `7z` namun mendukung lebih sedikit format file arsip dan dapat digunakan lintas sistem operasi.
> Informasi lebih lanjut: <https://manned.org/7za>.

- Meng[a]rsipkan sebuah file atau direktori:

`7za a {{jalan/menuju/arsip.7z}} {{jalan/menuju/file_atau_direktori}}`

- Mengenkripsi sebuah file arsip (termasuk nama-nama file yang terkandung di dalamnya):

`7za a {{jalan/menuju/arsip_terenkripsi.7z}} -p{{kata sandi}} -mhe=on {{jalan/menuju/arsip.7z}}`

- Mengekstrak sebuah file arsip dengan mempertahankan struktur direktori asli:

`7za x {{jalan/menuju/arsip.7z}}`

- Mengekstrak sebuah file arsip ke dalam direktori yang ditentukan:

`7za x {{jalan/menuju/arsip.7z}} -o{{jalan/menuju/direktori}}`

- Mengekstrak sebuah file arsip menuju stdout:

`7za x {{jalan/menuju/arsip.7z}} -so`

- Meng[a]rsipkan file atau direktori menggunakan format file arsip tertentu:

`7za a -t{{7z|bzip2|gzip|lzip|tar|zip}} {{jalan/menuju/arsip.7z}} {{jalan/menuju/file_atau_direktori}}`

- Me[l]ihat daftar isi dari sebuah file arsip:

`7za l {{jalan/menuju/arsip.7z}}`

- Mengetahui daftar format file arsip yang didukung:

`7za i`
