# egrep

> Cari pola teks tertentu pada kumpulan berkas menggunakan kata pencarian ekspresi reguler (regex) tingkat lanjut (mendukung `?`, `+`, `{}`, `()`, dan `|`).
> Informasi lebih lanjut: <https://manned.org/egrep>.

- Cari suatu berkas untuk teks yang mengikuti pola pencarian tertentu:

`egrep "{{pola_pencarian}}" {{jalan/menuju/berkas}}`

- Cari lebih dari satu berkas untuk teks yang mengikuti pola pencarian tertentu:

`egrep "{{pola_pencarian}}" {{jalan/menuju/berkas1 jalan/menuju/berkas2 ...}}`

- Cari isi `stdin` untuk teks yang mengikuti pola pencarian tertentu:

`cat {{jalan/menuju/berkas}} | egrep {{pola_pencarian}}`

- Cetak nama berkas dan nomor baris di mana pola tersebut ditemukan:

`egrep --with-filename --line-number "{{pola_pencarian}}" {{jalan/menuju/berkas}}`

- Cari seluruh berkas selain berkas format biner di dalam suatu direktori secara rekursif (termasuk berkas-berkas di dalam subdirektori) dengan menunjukkan nomor barisan di mana pola tersebut ditemukan:

`egrep --recursive --binary-files={{without-match}} "{{pola_pencarian}}" {{jalan/menuju/direktori}}`

- Cari untuk barisan teks yang tidak memenuhi kriteria pada pola pencarian:

`egrep --invert-match "{{pola_pencarian}}" {{jalan/menuju/berkas}}`
