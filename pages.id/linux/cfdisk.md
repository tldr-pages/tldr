# cfdisk

> Atur tabel dan partisi alokasi penyimpanan pada perangkat penyimpanan keras menggunakan tampilan antarmuka teks interaktif berbasis curses.
> Informasi lebih lanjut: <https://manned.org/cfdisk>.

- Jalankan program pengalokasi partisi terhadap suatu perangkat penyimpanan keras:

`sudo cfdisk {{/dev/sdX}}`

- Buat kemudian kelola tabel partisi baru terhadap suatu perangkat penyimpanan keras:

`sudo cfdisk {{[-z|--zero]}} {{/dev/sdX}}`
