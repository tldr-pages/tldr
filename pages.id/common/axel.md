# axel

> Akselerator proses pengunduhan.
> Mendukung protokol HTTP, HTTPS, FTP, dan FTPS.
> Lihat juga: `aria2c`.
> Informasi lebih lanjut: <https://manned.org/axel>.

- Unduh isi suatu alamat URL menuju berkas:

`axel {{url}}`

- Unduh dan tentukan nama akhir berkas:

`axel {{url}} {{[-o|--output]}} {{jalan/menuju/berkas}}`

- Tentukan jumlah koneksi saluran yang dipakai untuk mengunduh:

`axel {{[-n|--num-connections]}} {{jumlah}} {{url}}`

- Tentukan jumlah sumber mirror yang dipakai untuk mencari dan mengunduh:

`axel {{[-S|--search=]}}{{jumlah}} {{url}}`

- Batasi laju kecepatan pengunduhan (dalam bita per detik):

`axel {{[-s|--max-speed]}} {{kecepatan}} {{url}}`

- Hanya gunakan protokol IPv4 saat berhubungan dengan host:

`axel {{[-4|--ipv4]}} {{url}}`

- Batasi luaran program menuju `stdout` dan gunakan suatu nilai user-agent kustom saat mengunduh:

`axel {{[-q|--quiet]}} {{[-U|--user-agent]}} {{"Mozilla/5.0"}} {{url}}`
