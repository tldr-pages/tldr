# fastd

> Program layanan daemon untuk jaringan priat virtual (VPN).
> Bekerja baik dalam lapisan jaringan Layer 2 atau Layer 3, mendukung berbagai metode enkripsi, dan dipakai oleh Freifunk.
> Lihat juga: `ivpn`, `mozillavpn`, `mullvad`, `warp-cli`.
> Informasi lebih lanjut: <https://fastd.readthedocs.io/en/stable/>.

- Jalankan `fastd` dengan konfigurasi yang diatur dalam suatu berkas:

`fastd {{[-c|--config]}} {{jalan/menuju/fastd.conf}}`

- Jalankan suatu layanan VPN Layer 3 dengan MTU sebesar 1400, dengan konfigurasi lainnya yang diatur dalam suatu berkas:

`fastd {{[-m|--mode]}} {{tap}} {{[-M|--mtu]}} {{1400}} {{[-c|--config]}} {{jalan/menuju/fastd.conf}}`

- Lakukan validasi terhadap suatu berkas konfigurasi:

`fastd --verify-config {{[-c|--config]}} {{jalan/menuju/fastd.conf}}`

- Buat sebuah pasangan kunci untuk mengakses layanan VPN:

`fastd --generate-key`

- Tampilkan kunci publik terhadap kunci privat yang diatur dalam berkas konfigurasi:

`fastd --show-key {{[-c|--config]}} {{jalan/menuju/fastd.conf}}`

- Tampilkan versi program:

`fastd {{[-v|--version]}}`
