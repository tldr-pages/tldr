# astyle

> Program indenter, formatter, dan beautifier untuk berkas kode bahasa pemrograman C, C++, C#, dan Java.
> Setelah dijalankan, berkas asli akan disalin menuju nama berkas yang ditambahkan dengan akhiran ".orig".
> Informasi lebih lanjut: <https://manned.org/astyle>.

- Terapkan pengayaan penulisan 4 karakter spasi per indent tanpa mengubah format kode:

`astyle {{berkas_sumber}}`

- Terapkan pengayaan penulisan kode Java dengan posisi kurung kurawal terpasang:

`astyle {{[-A2|--style=java]}} {{jalan/menuju/berkas}}`

- Terapkan pengayaan penulisan kode allman dengan posisi kurung kurawal dalam baris terpisah:

`astyle {{[-A1|--style=allman]}} {{jalan/menuju/berkas}}`

- Terapkan indentasi kustom menggunakan karakter spasi. Pilih jumlah antara 2 dan 20 karakter:

`astyle {{[-s|--indent=spaces=]}}{{jumlah_karakter_spasi}} {{jalan/menuju/berkas}}`

- Terapkan indentasi kustom menggunakan karakter tab. Pilih jumlah antara 2 dan 20 karakter:

`astyle {{[-t|--indent=tab=]}}{{jumlah_karakter_tab}} {{jalan/menuju/berkas}}`
