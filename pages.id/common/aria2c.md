# aria2c

> Utilitas unduhan cepat.
> Mendukung HTTP(S), FTP, SFTP, BitTorrent, dan Metalink.
> Informasi lebih lanjut: <https://aria2.github.io>.

- Unduh URI ke sebuah file:

`aria2c "{{url}}"`

- Unduh file yang ditunjuk oleh URI yang ditentukan dengan nama keluaran yang ditentukan:

`aria2c --out={{nama_file}} "{{url}}"`

- Unduh beberapa file (berbeda) secara paralel:

`aria2c --force-sequential {{false}} "{{url1 url2 ...}}"`

- Unduh dari berbagai sumber dengan setiap URI menunjuk ke file yang sama:

`aria2c "{{url1 url2 ...}}"`

- Unduh URI yang tercantum dalam file dengan unduhan paralel terbatas:

`aria2c --input-file={{nama_file}} --max-concurrent-downloads={{jumlah_unduhan}}`

- Unduh dengan banyak koneksi:

`aria2c --split={{jumlah_koneksi}} "{{url}}"`

- Unduhan FTP dengan nama pengguna dan kata sandi:

`aria2c --ftp-user={{nama_pengguna}} --ftp-passwd={{kata_sandi}} "{{url}}"`

- Batasi kecepatan unduh dalam bytes/detik:

`aria2c --max-download-limit={{kecepatan}} "{{url}}"`
