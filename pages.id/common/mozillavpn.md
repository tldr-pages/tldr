# mozillavpn

> Layanan jaringan privat virtual (VPN) dari pembuat Firefox.
> Lihat juga: `fastd`, `ivpn`, `mullvad`, `warp-cli`.
> Informasi lebih lanjut: <https://github.com/mozilla-mobile/mozilla-vpn-client/wiki/Command-line-interface>.

- Masuk ke dalam akun melalui mode input interaktif:

`mozillavpn login`

- Hubungkan ke dalam jaringan Mozilla VPN:

`mozillavpn activate`

- Tampilkan status hubungan:

`mozillavpn status`

- Tampilkan daftar peladen (server) VPN yang tersedia:

`mozillavpn servers`

- Pilih peladen jaringan untuk dihubungkan:

`mozillavpn select {{nama_peladen}}`

- Putuskan hubungan dengan layanan VPN:

`mozillavpn deactivate`

- Keluar dari akun:

`mozillavpn logout`

- Tampilkan bantuan untuk suatu subperintah:

`mozillavpn {{subperintah}} --help`
