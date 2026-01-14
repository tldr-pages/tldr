# aria2c

> Utilitas unduhan cepat.
> Mendukung HTTP(S), FTP, SFTP, BitTorrent, dan Metalink.
> Lihat juga: `axel`.
> Informasi lebih lanjut: <https://aria2.github.io/manual/en/html/aria2c.html>.

- Unduh URI ke suatu berkas:

`aria2c "{{url}}"`

- Unduh berkas yang ditunjuk oleh URI yang ditentukan dengan nama keluaran yang ditentukan:

`aria2c {{[-o|--out]}} {{jalan/menuju/berkas}} "{{url}}"`

- Unduh beberapa berkas (berbeda) secara paralel:

`aria2c {{[-Z|--force-sequential=true]}} {{"url1" "url2" ...}}`

- Unduh berkas yang sama dari kumpulan sumber mirror dan lakukan verifikasi atas berkas yang diunduh:

`aria2c --checksum {{sha-256}}={{hash}} {{"url1" "url2" ...}}`

- Unduh URI yang tercantum dalam suatu berkas dengan unduhan paralel terbatas:

`aria2c {{[-i|--input-file]}} {{jalan/menuju/berkas}} {{[-j|--max-concurrent-downloads]}} {{jumlah_unduhan}}`

- Unduh dengan berbagai koneksi:

`aria2c {{[-s|--split]}} {{jumlah_koneksi}} "{{url}}"`

- Unduh berkas dari peladen FTP dengan username pengguna dan kata sandi:

`aria2c --ftp-user {{username}} --ftp-passwd {{kata_sandi}} "{{url}}"`

- Batasi kecepatan unduh dalam bytes/detik:

`aria2c --max-download-limit {{kecepatan}} "{{url}}"`
