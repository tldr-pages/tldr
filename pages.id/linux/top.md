# top

> Tampilkan informasi waktu nyata dinamis tentang proses yang berjalan.
> Lihat juga: `htop`, `atop`, `glances`, `btop`, `btm`.
> Informasi lebih lanjut: <https://manned.org/top>.

- Jalankan `top`:

`top`

- Jangan tampilkan proses-proses yang sedang diam atau tidak bernyawa (zombie):

`top {{[-i|--idle-toggle]}}`

- Hanya tampilkan kumpulan proses yang dipunyai oleh suatu pengguna:

`top {{[-u|--filter-only-euser]}} {{nama_pengguna}}`

- Urutkan daftar proses berdasarkan urutan data dalam kolom tertentu:

`top {{[-o|--sort-override]}} {{nama_kolom}}`

- Tampilkan daftar thread individu untuk suatu proses:

`top {{[-Hp|--threads-show --pid]}} {{id_proses}}`

- Hanya tampilkan daftar proses yang memiliki nomor induk (PID) tertentu, masing-masing dipisah dengan tanda koma (Umumnya Anda tidak akan mengetahui daftar PID untuk proses-proses berjalan. Perintah contoh ini secara otomatis mengambil daftar PID berdasarkan nama proses yang diketahui):

`top {{[-p|--pid]}} $(pgrep {{[-d|--delimiter]}} ',' {{nama_proses}})`

- Tampilkan bantuan mengenai perintah-perintah interaktif:

`<?>`
