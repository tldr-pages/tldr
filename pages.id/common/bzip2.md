# bzip2

> Suatu program pengompres berkas berbasis pengurutan blok.
> Lihat juga: `bzcat`, `bunzip2`, `bzip2recover`.
> Informasi lebih lanjut: <https://manned.org/bzip2>.

- Kompres suatu berkas:

`bzip2 {{jalan/menuju/berkas_untuk_dikompres}}`

- Dekompres suatu berkas:

`bzip2 {{[-d|--decompress]}} {{jalan/menuju/berkas_terkompres.bz2}}`

- Dekompres suatu berkas menuju `stdout`:

`bzip2 {{[-dc|--decompress --stdout]}} {{jalan/menuju/berkas_terkompres.bz2}}`

- Ujikan keutuhan isi setiap berkas dalam suatu berkas arsip:

`bzip2 {{[-t|--test]}} {{jalan/menuju/berkas_terkompres.bz2}}`

- Tampilkan nilai rasio kompresi untuk setiap berkas yang terproses dalam suatu arsip secara terperinci:

`bzip2 {{[-v|--verbose]}} {{jalan/menuju/berkas_berkas_terkompres.bz2}}`

- Dekompres suatu berkas, dan gantikan isi berkas arsip tujuan secara paksa:

`bzip2 {{[-f|--force]}} {{jalan/menuju/berkas_terkompres.bz2}}`

- Tampilkan bantuan:

`bzip2 {{[-h|--help]}}`
