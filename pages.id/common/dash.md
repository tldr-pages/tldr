# dash

> Debian Almquist Shell, suatu implementasi `sh` berstandar POSIX (tidak kompatibel dengan Bash).
> Informasi lebih lanjut: <https://manned.org/dash>.

- Jalankan sesi interaktif baru:

`dash`

- Jalankan kumpulan perintah secara spesifik:

`dash -c "{{echo 'perintah dash telah dijalankan'}}"`

- Jalankan suatu naskah/skrip perintah:

`dash {{jalan/menuju/naskah.sh}}`

- Jalankan sesi interaktif baru dengan mengeluarkan kembali isi perintah masukan sebelum menjalankannya:

`dash -n {{jalan/menuju/naskah.sh}}`

- Jalankan suatu naskah/skrip, dan tampilkan isi masing-masing perintah sebelum menjalankannya:

`dash -x {{jalan/menuju/naskah.sh}}`

- Jalankan suatu naskah/skrip dan segera berhenti jika terdapat galat/[e]rror perdana:

`dash -e {{jalan/menuju/naskah.sh}}`

- Jalankan kumpulan perintah dari `stdin`:

`{{echo "echo 'perintah dash telah dijalankan'"}} | dash`
