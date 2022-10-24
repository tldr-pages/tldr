# ping

> Mengirim paket-paket ICMP ECHO_REQUEST ke host dalam jaringan.
> Informasi lebih lanjut: <https://manned.org/ping>.

- Ping host:

`ping {{host}}`

- Ping host dalam jumlah kali tertentu:

`ping -c {{jumlah}} {{host}}`

- Ping host, dengan menentukan interval dalam sekian detik di antara request (asalnya 1 detik):

`ping -i {{jumlah-detik}} {{host}}`

- Ping host tanpa mencoba untuk melihat alamat dari nama-nama simbolis:

`ping -n {{host}}`

- Ping host dan membunyikan bel saat paket diterima (jika terminal anda mendukungnya):

`ping -a {{host}}`

- Menampilkan juga pesan jika tidak ada respon yang diterima:

`ping -O {{host}}`
