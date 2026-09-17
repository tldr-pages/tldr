# argos-translate

> Sebuah pustaka Python bersumber terbuka dengan alat baris perintah untuk melakukan alih bahasa secara luring.
> Informasi lebih lanjut: <https://argos-translate.readthedocs.io/en/latest/source/cli.html>.

- Pasang berkas penerjemah untuk alih bahasa dari bahasa Spanyol menuju Inggris:

`argospm install translate-es_en`

- Terjemahkan sebagian teks dari bahasa Spanyol (`es`) menuju Inggris (`en`) (Catatan: Program ini hanya mendukung kode bahasa dengan dua huruf):

`argos-translate --from-lang es --to-lang en {{un texto corto}}`

- Terjemahkan suatu berkas teks dari bahasa Inggris menuju Hindi:

`cat {{jalan/menuju/berkas.txt}} | argos-translate --from-lang en --to-lang hi`

- Tampilkan daftar seluruh pasangan penerjemah bahasa yang tersedia:

`argospm list`

- Tampilkan pasangan penerjemah yang tersedia untuk menerjemahkan teks bahasa Inggris menuju bahasa lain:

`argospm search --from-lang en`

- Perbarui berkas penerjemah bahasa yang terpasang:

`argospm update`

- Terjemahkan teks dari `ar` menuju `ru` (Catatan: Proses ini membutuhkan berkas penerjemah `translate-ar_en` dan `translate-en_ru` untuk terpasang terlebih dahulu):

`argos-translate --from-lang ar --to-lang ru {{صورة تساوي أكثر من ألف كلمة}}`
