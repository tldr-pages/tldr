# aircrack-ng

> Retas dan dapatkan kunci WEP dan WPA/WPA2 dari proses handshake dalam paket jaringan yang ditangkap.
> Bagian dari paket perangkat lunak jaringan Aircrack-ng.
> Informasi lebih lanjut: <https://www.aircrack-ng.org/doku.php?id=aircrack-ng>.

- Retas dan dapatkan kunci dari file tangkapan jaringan dan file daftar kata sandi ([w]ordlist):

`aircrack-ng -w {{jalan/menuju/wordlist.txt}} {{jalan/menuju/tangkapan_jaringan.cap}}`

- Retas dan dapatkan kunci dari file tangkapan jaringan, [w]ordlist, dan [e]ssid milik perangkat titik akses Wi-Fi:

`aircrack-ng -w {{jalan/menuju/wordlist.txt}} -e {{essid}} {{jalan/menuju/tangkapan_jaringan.cap}}`

- Retas dan dapatkan kunci dari file tangkapan jaringan, [w]ordlist, dan alamat MAC milik perangkat titik akses Wi-Fi:

`aircrack-ng -w {{jalan/menuju/wordlist.txt}} --bssid {{mac}} {{jalan/menuju/tangkapan_jaringan.cap}}`
