# gzip

> Kompres/dekompres berkas/fail komputer dengan kompresi `gzip` (LZ77).
> Informasi lebih lanjut: <https://www.gnu.org/software/gzip/manual/gzip.html>.

- Kompres sebuah berkas, menggantinya dengan arsip `gzip`:

`gzip {{lokasi/ke/berkas}}`

- Dekompres sebuah berkas, menggantinya dengan versi asli yang tidak terkompres:

`gzip {{[-d|--decompress]}} {{lokasi/ke/berkas.gz}}`

- Kompres sebuah berkas dengan tetap mempertahankan berkas asli:

`gzip {{[-k|--keep]}} {{lokasi/ke/berkas}}`

- Kompres sebuah berkas dengan menentukan nama berkas output:

`gzip {{[-c|--stdout]}} {{lokasi/ke/berkas}} > {{lokasi/ke/berkas_terkompres.gz}}`

- Dekompres sebuah arsip `gzip` dengan menentukan nama berkas output:

`gzip {{[-cd|--stdout --decompress]}} {{lokasi/ke/berkas.gz}} > {{lokasi/ke/berkas_dekompres}}`

- Tentukan level kompresi. 1 berarti yang tercepat (kompresi rendah), 9 berarti yang terlambat (kompresi tinggi), 6 berarti default:

`gzip -{{1..9}} {{[-c|--stdout]}} {{lokasi/ke/berkas}} > {{lokasi/ke/berkas_terkompres.gz}}`

- Tampilkan nama dan persentase reduksi untuk setiap berkas yang dikompres atau didekompres:

`gzip {{[-vd|--verbose --decompress]}} {{lokasi/ke/berkas.gz}}`
