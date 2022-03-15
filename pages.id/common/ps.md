# ps

> Informasi tentang proses-proses yang berlangsung.
> Informasi lebih lanjut: <https://manned.org/ps>.

- Menampilkan daftar semua proses yang berlangsung:

`ps aux`

- Menampilkan daftar semua proses yang berlangsung termasuk _string_ perintah secara utuh:

`ps auxww`

- Mencari proses yang sesuai dengan _string_:

`ps aux | grep {{string}}`

- Menampilkan daftar semua proses pengguna yang berlangsung dengan format tambahan yang utuh:

`ps --user $(id -u) -F`

- Menampilkan daftar semua proses pengguna yang berlangsung sebagai pohon:

`ps --user $(id -u) f`

- Mengambil induk PID dari sebuah proses:

`ps -o ppid= -p {{pid}}`

- Sortir proses berdasarkan konsumsi memori:

`ps --sort size`
