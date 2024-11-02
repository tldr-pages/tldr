# htop

> Tampilkan informasi waktu nyata dinamis tentang proses yang berjalan. Versi `top` yang disempurnakan.
> Informasi lebih lanjut: <https://htop.dev/>.

- Mulai `htop`:

`htop`

- Mulai `htop` dan tampilkan proses yang dimiliki oleh pengguna tertentu:

`htop --user {{username}}`

- Tampilkan daftar proses beserta hierarki penugasannya dalam bentuk tampilan pohon untuk menunjukkan relasi proses induk beserta anak-anaknya:

`htop --tree`

- Urutkan proses berdasarkan `sort_item` yang ditentukan (gunakan `htop --sort help` untuk opsi yang tersedia  ):

`htop --sort {{sort_item}}`

- Jalankan `htop` dengan jangka waktu pemuatan ulang (refresh) data tertentu, dalam bentuk sepersepuluh detik (yakni 50 = 5 detik):

`htop --delay {{50}}`

- Lihat perintah interaktif saat menjalankan htop:

`?`

- Alihkan tampilan menuju tab lain:

`tab`

- Tampilkan bantuan:

`htop --help`
