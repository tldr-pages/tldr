# ksh

> Korn Shell, suatu penerjemah baris perintah yang kompatibel dengan Bash.
> Lihat juga: `!`, `^`.
> Informasi lebih lanjut: <https://manned.org/ksh>.

- Jalankan sesi interaktif baru:

`ksh`

- Jalankan kumpulan perintah secara spesifik:

`ksh -c "{{echo 'perintah ksh telah dijalankan'}}"`

- Jalankan suatu naskah/skrip perintah:

`ksh {{jalan/menuju/naskah.ksh}}`

- Periksa suatu naskah/skrip perintah untuk kesalahan sintaks tanpa menjalankan isi perintahnya:

`ksh -n {{jalan/menuju/naskah.ksh}}`

- Jalankan suatu naskah/skrip, dan tampilkan isi masing-masing perintah sebelum menjalankannya:

`ksh -x {{jalan/menuju/naskah.ksh}}`
