# ping

> Kirim kumpulan paket ICMP ECHO_REQUEST (sebagai pesan "ping") ke host dalam jaringan.
> Informasi lebih lanjut: <https://manned.org/ping>.

- Ping suatu host:

`ping {{host}}`

- Ping suatu host dengan jumlah pengulangan yang ditetapkan:

`ping -c {{jumlah}} {{host}}`

- Ping suatu host, dengan menentukan interval dalam sekian detik di antara permintaan (asalnya 1 detik):

`ping -i {{detik}} {{host}}`

- Ping suatu host tanpa mencoba untuk melihat alamat dari nama-nama simbolis:

`ping -n {{host}}`

- Ping suatu host dan membunyikan bel saat paket diterima (jika terminal anda mendukungnya):

`ping -a {{host}}`

- Tampilkan juga pesan jika tidak ada respon yang diterima:

`ping -O {{host}}`

- Ping suatu host dengan jumlah pengulangan yang ditetapkan, batas timeout (`-W`) untuk setiap balasan, serta batas waktu (`-w`) eksekusi bagi keseluruhan proses ping berjalan:

`ping -c {{jumlah}} -W {{detik}} -w {{detik}} {{host}}`
