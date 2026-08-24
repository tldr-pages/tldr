# aide

> Advanced Intrusion Detection Environment untuk memvalidasi integritas file.
> Informasi lebih lanjut: <https://manned.org/aide>.

- Lakukan inisialisasi database:

`sudo aide {{[-i|--init]}}`

- Periksa database untuk mencari inkonsistensi:

`sudo aide {{[-C|--check]}}`

- Bandingkan dua database berdasarkan definisi dalam file konfigurasi:

`sudo aide {{[-E|--compare]}}`

- Periksa dan perbarui database secara non-interaktif:

`sudo aide {{[-u|--update]}}`

- Tentukan file konfigurasi untuk menimpa `aide.conf` bawaan:

`sudo aide {{[-c|--config]}} {{path/ke/config_file}}`

- Gunakan `regex` untuk membatasi AIDE pada string tertentu:

`sudo aide {{[-l|--limit]}} {{regex}}`

- Kirimkan hasil reporter ke sebuah URL:

`sudo aide {{[-r|--report]}} {{reporterurl}}`
