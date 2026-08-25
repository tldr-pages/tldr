# bash

> Bourne-Again SHell, suatu penerjemah baris perintah yang kompatibel dengan standar bahasa `sh`.
> Lihat juga: `zsh`, `!`.
> Informasi lebih lanjut: <https://www.gnu.org/software/bash/manual/bash.html#Invoking-Bash>.

- Jalankan sesi interaktif baru:

`bash`

- Jalankan sesi interaktif baru tanpa memuat perintah konfigurasi awal:

`bash --norc`

- Jalankan kumpulan perintah secara spesifik:

`bash -c "{{echo 'perintah bash telah dijalankan'}}"`

- Jalankan suatu naskah/skrip perintah:

`bash {{jalan/menuju/naskah.sh}}`

- Jalankan suatu naskah/skrip, dan tampilkan isi masing-masing perintah sebelum menjalankannya:

`bash -x {{jalan/menuju/naskah.sh}}`

- Jalankan suatu naskah/skrip dan segera berhenti jika terdapat galat/[e]rror perdana:

`bash -e {{jalan/menuju/naskah.sh}}`

- Jalankan kumpulan perintah dari `stdin`:

`{{echo "echo 'perintah bash telah dijalankan'"}} | bash`

- Jalankan sesi interaktif baru dengan pembatasan administratif:

`bash {{[-r|--restricted]}}`
