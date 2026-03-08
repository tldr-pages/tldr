# pdfseparate

> Utilitas pengekstrak halaman berkas Portable Document Format (PDF).
> Informasi lebih lanjut: <https://manned.org/pdfseparate>.

- Ekstrak halaman-halaman dari berkas PDF dan buat berkas PDF terpisah untuk setiap halaman:

`pdfseparate {{jalan/ke/berkas_sumber.pdf}} {{jalan/ke/berkas_tujuan-%d.pdf}}`

- Tentukan halaman pertama/awal untuk ekstraksi:

`pdfseparate -f {{3}} {{jalan/ke/berkas_sumber.pdf}} {{jalan/ke/berkas_tujuan-%d.pdf}}`

- Tentukan halaman terakhir untuk ekstraksi:

`pdfseparate -l {{10}} {{jalan/ke/berkas_sumber.pdf}} {{jalan/ke/berkas_tujuan-%d.pdf}}`
