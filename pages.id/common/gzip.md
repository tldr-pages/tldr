# gzip

> Kompres/dekompres berkas/fail komputer dengan kompresi `gzip` (LZ77).
> Informasi lebih lanjut: <https://www.gnu.org/software/gzip/manual/gzip.html>.

- Kompres sebuah berkas, menggantinya dengan arsip `gzip`:

`gzip {{jalan/menuju/berkas}}`

- Dekompres sebuah berkas, menggantinya dengan versi asli yang tidak terkompres:

`gzip {{[-d|--decompress]}} {{jalan/menuju/berkas.gz}}`

- Tampilkan daftar nama dan persentase pengurangan beban untuk setiap berkas terkompres:

`gzip {{[-v|--verbose]}} {{jalan/menuju/berkas.gz}}`

- Kompres sebuah berkas dengan tetap mempertahankan berkas asli:

`gzip {{[-k|--keep]}} {{jalan/menuju/berkas}}`

- Kompres sebuah berkas dengan menentukan nama berkas output:

`gzip {{[-c|--stdout]}} {{jalan/menuju/berkas}} >{{jalan/menuju/berkas_terkompres.gz}}`

- Dekompres sebuah arsip `gzip` dengan menentukan nama berkas output:

`gzip {{[-cd|--stdout --decompress]}} {{jalan/menuju/berkas.gz}} >{{jalan/menuju/berkas_dekompres}}`

- Tentukan level kompresi. 1 berarti yang tercepat (kompresi rendah), 9 berarti yang terlambat (kompresi tinggi), 6 berarti default:

`gzip -{{1..9}} {{[-c|--stdout]}} {{jalan/menuju/berkas}} >{{jalan/menuju/berkas_terkompres.gz}}`

- Tampilkan daftar isi suatu berkas arsip:

`gzip {{[-l|--list]}} {{jalan/menuju/berkas.txt.gz}}`
