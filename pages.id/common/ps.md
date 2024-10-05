# ps

> Tampilkan informasi tentang proses-proses yang berlangsung.
> Informasi lebih lanjut: <https://manned.org/ps>.

- Tampilkan daftar seluruh proses yang berlangsung:

`ps aux`

- Tampilkan daftar seluruh proses yang berlangsung termasuk string perintah secara utuh:

`ps auxww`

- Cari proses berdasarkan teks/string kriteria (penambahan kurung siku akan mencegah `grep` untuk mencocokkan dirinya sendiri):

`ps aux | grep {{[s]tring}}`

- Tampilkan daftar seluruh proses dari pengguna saat ini dengan format tambahan ekstra:

`ps --user $(id -u) -F`

- Tampilkan daftar seluruh proses dari pengguna saat ini dalam format pohon:

`ps --user $(id -u) f`

- Mengambil induk PID dari sebuah proses:

`ps -o ppid= -p {{pid}}`

- Sortir proses berdasarkan konsumsi memori:

`ps --sort size`
