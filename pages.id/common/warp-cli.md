# warp-cli

> Program command-line resmi untuk layanan Cloudflare WARP.
> WARP adalah sebuah layanan jaringan privat virtual (VPN) yang mengenkripsi lalu lintas jaringan demi meningkatkan privasi, keamanan, dan kecepatan.
> Lihat juga: `fastd`, `ivpn`, `mozillavpn`, `mullvad`.
> Informasi lebih lanjut: <https://developers.cloudflare.com/warp-client/>.

- Daftarkan perangkat ini ke dalam jaringan WARP (harus dijalankan pada pertama kali):

`warp-cli registration new`

- Hubungkan perangkat ini ke dalam jaringan WARP:

`warp-cli connect`

- Putuskan perangkat ini dari jaringan WARP:

`warp-cli disconnect`

- Tampilkan status koneksi WARP saat ini:

`warp-cli status`

- Pindah mode operasi koneksi layanan WARP:

`warp-cli set-mode {{mode_operasi}}`

- Tampilkan bantuan umum:

`warp-cli help`

- Tampilkan bantuan untuk suatu subperintah:

`warp-cli help {{subperintah}}`
