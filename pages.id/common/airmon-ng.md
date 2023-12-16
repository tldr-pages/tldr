# airmon-ng

> Nyalakan mode pengawasan pada perangkat jaringan nirkabel/wireless.
> Bagian dari paket perangkat lunak jaringan Aircrack-ng.
> Informasi lebih lanjut: <https://www.aircrack-ng.org/doku.php?id=airmon-ng>.

- Tampilkan daftar perangkat nirkabel beserta statusnya:

`sudo airmon-ng`

- Mulai awasi jaringan untuk perangkat tertentu:

`sudo airmon-ng start {{wlan0}}`

- Hentikan proses-proses mengganggu yang memanfaatkan perangkat nirkabel:

`sudo airmon-ng check kill`

- Matikan mode pengawasan untuk interface jaringan tertentu:

`sudo airmon-ng stop {{wlan0mon}}`
