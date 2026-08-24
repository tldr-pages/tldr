# caddy

> Sebuah peladen web bersumber terbuka yang siap pakai untuk perusahaan, dengan HTTPS otomatis, dan ditulis dalam bahasa Go.
> Informasi lebih lanjut: <https://caddyserver.com/docs/command-line>.

- Jalankan Caddy sebagai proses latar depan (foreground):

`caddy run`

- Jalankan Caddy dengan konfigurasi Caddyfile tertentu:

`caddy run --config {{jalan/menuju/Caddyfile}}`

- Jalankan Caddy dalam latar belakang (background):

`caddy start`

- Hentikan suatu proses Caddy yang berjalan di latar belakang:

`caddy stop`

- Jalankan suatu peladen berkas sederhana dengan port spesifik, dengan fitur antarmuka penjelajah berkas:

`caddy file-server --listen :{{8000}} --browse`

- Jalankan suatu peladen proksi terbalik (reverse proxy):

`caddy reverse-proxy --from :{{80}} --to localhost:{{8000}}`
