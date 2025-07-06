# grep

> Cari pola teks tertentu pada kumpulan berkas menggunakan kata pencarian ekspresi reguler (regex).
> Informasi lebih lanjut: <https://www.gnu.org/software/grep/manual/grep.html>.

- Cari suatu berkas untuk teks yang mengikuti pola pencarian tertentu:

`grep "{{pola_pencarian}}" {{jalan/menuju/berkas}}`

- Cari berkas untuk teks string tertentu secara spesifik (dengan menghentikan pencarian berbasis ekspresi reguler):

`grep {{[-F|--fixed-strings]}} "{{teks_spesifik}}" {{jalan/menuju/berkas}}`

- Cari seluruh berkas selain berkas format biner di dalam suatu direktori secara rekursif (termasuk berkas-berkas di dalam subdirektori) dengan menunjukkan nomor barisan di mana pola tersebut ditemukan:

`grep {{[-rnI|--recursive --line-number --binary-files=without-match]}} "{{pola_pencarian}}" {{jalan/menuju/direktori}}`

- Gunakan sintaks ekspresi reguler tingkat lanjut (mendukung `?`, `+`, `{}`, `()`, dan `|`), dalam mode case-insensitive (tanpa menghiraukan perbedaan antara huruf kapital dan kecil):

`grep {{[-Ei|--extended-regexp --ignore-case]}} "{{pola_pencarian}}" {{jalan/menuju/berkas}}`

- Cetak 3 baris konteks isi berkas pada sekitar, sebelum, atau sesudah setiap hasil pencarian:

`grep {{--context|--before-context|--after-context}} 3 "{{pola_pencarian}}" {{jalan/menuju/berkas}}`

- Cetak nama berkas dan nomor baris di mana pola tersebut ditemukan dalam format teks berwarna:

`grep {{[-Hn|--with-filename --line-number]}} --color=always "{{pola_pencarian}}" {{jalan/menuju/berkas}}`

- Cari untuk barisan teks yang memenuhi kriteria pada pola pencarian, dan hanya cetak bagian teks yang memenuhi pola:

`grep {{[-o|--only-matching]}} "{{pola_pencarian}}" {{jalan/menuju/berkas}}`

- Cari `stdin` untuk barisan teks yang tidak memenuhi kriteria pada pola pencarian:

`cat {{jalan/menuju/berkas}} | grep {{[-v|--invert-match]}} "{{pola_pencarian}}"`
