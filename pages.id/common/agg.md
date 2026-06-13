# agg

> Buat berkas gambar GIF dari suatu sesi rekaman `asciinema`.
> Informasi lebih lanjut: <https://docs.asciinema.org/manual/agg/usage/>.

- Buat suatu berkas GIF:

`agg {{jalan/menuju/demo.cast}} {{jalan/menuju/demo.gif}}`

- Buat berkas GIF yang memuat panjang 80 kolom dan tinggi 25 baris:

`agg --cols 80 --rows 25 {{jalan/menuju/demo.cast}} {{jalan/menuju/demo.gif}}`

- Buat berkas GIF dengan ukuran font 24 piksel:

`agg --font-size 24 {{jalan/menuju/demo.cast}} {{jalan/menuju/demo.gif}}`

- Tampilkan informasi bantuan:

`agg {{[-h|--help]}}`
