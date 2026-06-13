# apg

> Buat kata sandi secara acak dan kompleks.
> Informasi lebih lanjut: <https://manned.org/apg>.

- Buat sebuah kata sandi secara acak (panjang default bagi kata sandi adalah 8):

`apg`

- Buat sebuah kata sandi dengan minimum 1 simbol (S), 1 nomor (N), 1 huruf kapital (C), dan 1 huruf kecil (L):

`apg -M SNCL`

- Buat kata sandi dengan panjang 16 karakter:

`apg -m {{16}}`

- Buat kata sandi dengan panjang ma[x]imum 16 karakter:

`apg -x {{16}}`

- Buat sebuah kata sandi yang tidak mengandung kata yang terkandung di dalam suatu berkas kamus:

`apg -r {{jalan/menuju/berkas_kamus}}`
