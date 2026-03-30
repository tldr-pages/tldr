# at

> Jalankan kumpulan perintah pada lain waktu.
> Hasil penugasan perintah akan dikirimkan menuju surel pengguna.
> Informasi lebih lanjut: <https://manned.org/at>.

- Buat perintah secara interaktif untuk dijalankan dalam 5 menit ke depan (gunakan `<Ctrl d>` jika selesai menulis):

`at now + 5 minutes`

- Buat perintah secara interaktif dan jalankan pada waktu tertentu:

`at {{hh:mm}}`

- Jalankan perintah yang dimasukkan ke dalam `stdin` pada hari ini pukul 10.00 pagi:

`echo "{{command}}" | at 1000`

- Jalankan perintah yang diatur dalam suatu berkas pada hari Selasa berikutnya:

`at -f {{jalan/menuju/berkas}} 9:30 PM Tue`

- Tampilkan seluruh pekerjaan terjadwal untuk pengguna saat ini (sama dengan perintah `atq`):

`at -l`

- Lihat rincian suatu pekerjaan:

`at -c {{nomor_pekerjaan}}`
