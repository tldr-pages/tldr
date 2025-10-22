# sed

> Mengedit teks secara skrip.
> Lihat juga: `awk`, `ed`.
> Informasi lebih lanjut: <https://manned.org/sed.1posix>.

- Ganti semua kata `apple` (`regex` dasar) yang muncul dengan kata `mango` (`regex` dasar) di semua baris input dan cetak hasilnya ke `stdout`:

`{{command}} | sed 's/apple/mango/g'`

- Jalankan skrip tertentu [f]ile dan cetak hasilnya ke `stdout`:

`{{command}} | sed -f {{path/to/script.sed}}`

- Cetak hanya baris pertama saja ke `stdout`:

`{{command}} | sed -n '1p'`
