# apropos

> Lakukan pencarian nama dan deskripsi perintah dalam buku panduan program baris perintah (`manpages`).
> Informasi lebih lanjut: <https://manned.org/apropos>.

- Cari daftar dokumentasi perintah yang mengandung kata dengan format kata kunci ekspresi reguler (regex):

`apropos {{ekspresi_reguler}}`

- Jangan pangkas tampilan teks hasil pencarian menurut panjang jendela terminal:

`apropos -l {{ekspresi_reguler}}`

- Cari daftar dokumentasi perintah yang mengandung seluruh ([a]ll) kriteria kata dalam bentuk ekspresi reguler (regex):

`apropos {{ekspresi_reguler_1}} -a {{ekspresi_reguler_2}} -a {{ekspresi_reguler_3}}`
