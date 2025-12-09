# htop

> Tampilkan informasi waktu nyata dinamis tentang proses yang berjalan. Versi `top` yang disempurnakan.
> Informasi lebih lanjut: <https://manned.org/htop>.

- Mulai `htop`:

`htop`

- Mulai `htop` dan tampilkan proses yang dimiliki oleh pengguna tertentu:

`htop {{[-u|--user]}} {{username}}`

- Tampilkan daftar proses beserta hierarki penugasannya dalam bentuk tampilan pohon untuk menunjukkan relasi proses induk beserta anak-anaknya:

`htop {{[-t|--tree]}}`

- Urutkan proses berdasarkan `sort_item` yang ditentukan (gunakan `htop --sort help` untuk opsi yang tersedia):

`htop {{[-s|--sort]}} {{sort_item}}`

- Jalankan `htop` dengan jangka waktu pemuatan ulang (refresh) data tertentu, dalam bentuk sepersepuluh detik (yakni 50 = 5 detik):

`htop {{[-d|--delay]}} {{50}}`

- Lihat perintah interaktif saat menjalankan htop:

`<?>`

- Alihkan tampilan menuju tab lain:

`<Tab>`

- Tampilkan bantuan:

`htop {{[-h|--help]}}`
