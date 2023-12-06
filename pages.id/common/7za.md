# 7za

> Pengarsip file dengan rasio kompresi yang tinggi.
> Serupa dengan `7z` namun mendukung lebih sedikit format file arsip dan dapat digunakan lintas sistem operasi.
> Informasi lebih lanjut: <https://manned.org/7za>.

- T[a]mbahkan sebuah file atau direktori ke dalam arsip baru atau saat ini:

`7za a {{jalan/menuju/arsip.7z}} {{jalan/menuju/file_atau_direktori}}`

- Enkripsi file arsip saat ini (termasuk nama-nama file yang terkandung di dalamnya):

`7za a {{jalan/menuju/arsip_terenkripsi.7z}} -p{{kata sandi}} -mhe={{on}} {{jalan/menuju/arsip.7z}}`

- E[x]trak file arsip dengan mempertahankan struktur direktori asli:

`7za x {{jalan/menuju/arsip.7z}}`

- E[x]trak file arsip ke dalam direktori yang ditentukan:

`7za x {{jalan/menuju/arsip.7z}} -o{{jalan/menuju/direktori}}`

- E[x]trak file arsip menuju `stdout`:

`7za x {{jalan/menuju/arsip.7z}} -so`

- [a]rsipkan file atau direktori menggunakan format file arsip tertentu:

`7za a -t{{7z|bzip2|gzip|lzip|tar|...}} {{jalan/menuju/arsip.7z}} {{jalan/menuju/file_atau_direktori}}`

- [l]ihat daftar isi dari sebuah file arsip:

`7za l {{jalan/menuju/arsip.7z}}`

- Atur tingkat kompresi pada file arsip (tingkat lebih tinggi memproduksi file arsip lebih kecil dengan proses kompresi yang lebih lama):

`7za a {{jalan/menuju/arsip.7z}} -mx={{0|1|3|5|7|9}} {{jalan/menuju/file_atau_direktori}}`
