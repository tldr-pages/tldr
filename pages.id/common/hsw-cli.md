# hsw-cli

> Alat baris perintah untuk mengakses dompet digital Handshake melalui koneksi REST API.
> Informasi lebih lanjut: <https://github.com/handshake-org/hs-client>.

- Buka akses terhadap suatu dompet digital (nilai timeout dalam hitungan detik):

`hsw-cli unlock {{kata_sandi}} {{timeout}}`

- Kunci dompet saat ini:

`hsw-cli lock`

- Tampilkan informasi terhadap dompet saat ini:

`hsw-cli get`

- Tampilkan saldo dompet saat ini:

`hsw-cli balance`

- Tampilkan riwayat transaksi yang menggunakan dompet saat ini:

`hsw-cli history`

- Kirim suatu transaksi dengan suatu nominal koin menuju suatu alamat dompet tujuan:

`hsw-cli send {{alamat_tujuan}} {{1.05}}`

- Tampilkan daftar transaksi yang berstatus tertunda (pending) yang melibatkan dompet ini:

`hsw-cli pending`

- Tampilkan informasi rincian suatu transaksi:

`hsw-cli tx {{hash_transaksi}}`
