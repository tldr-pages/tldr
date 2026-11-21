# xz

> Kompres atau dekompres berkas-berkas XZ dan LZMA.
> Informasi lebih lanjut: <https://manned.org/xz>.

- Kompres suatu berkas menuju format XZ:

`xz {{jalan/menuju/berkas}}`

- Dekompres suatu berkas XZ:

`xz {{[-d|--decompress]}} {{jalan/menuju/berkas.xz}}`

- Kompres suatu berkas menggunakan algoritma LZMA:

`xz {{[-F|--format]}} lzma {{jalan/menuju/berkas}}`

- Dekompres suatu berkas LZMA:

`xz {{[-d|--decompress]}} {{[-F|--format]}} lzma {{jalan/menuju/berkas.lzma}}`

- Dekompres suatu berkas dan tuliskan isinya ke dalam `stdout` (sehingga opsi `--keep` juga digunakan):

`xz {{[-d|--decompress]}} {{[-c|--stdout]}} {{jalan/menuju/berkas.xz}}`

- Kompres suatu berkas, namun jangan hapus berkas asal yang telah terkompres:

`xz {{[-k|--keep]}} {{jalan/menuju/berkas}}`

- Kompres suatu berkas menggunakan tingkat kompresi tercepat:

`xz -0 {{jalan/menuju/berkas}}`

- Kompres suatu berkas menggunakan tingkat kompresi terbaik/terpadat:

`xz -9 {{jalan/menuju/berkas}}`
