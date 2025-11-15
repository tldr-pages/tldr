# airdecap-ng

> Dekripsi file tangkapan jaringan terenkripsi dengan kunci sandi WEP, WPA, atau WPA2.
> Bagian dari paket perangkat lunak jaringan Aircrack-ng.
> Informasi lebih lanjut: <https://www.aircrack-ng.org/doku.php?id=airdecap-ng>.

- Buang informasi header jaringan wireless/nirkabel dari file tangkapan jaringan (bebas enkripsi WEP/WPA/WPA2), dan gunakan alamat MAC titik akses Wi-Fi untuk menyaringnya:

`airdecap-ng -b {{alamat_mac}} {{jalan/menuju/tangkapan_jaringan.cap}}`

- Buka enkripsi WEP dari file tangkapan jaringan menggunakan kunci WEP dalam format heksadesimal:

`airdecap-ng -w {{kunci_heksadesimal}} {{jalan/menuju/tangkapan_jaringan.cap}}`

- Buka enkripsi WPA/WPA2 dari file tangkapan jaringan menggunakan [e]ssid titik akses Wi-Fi dan kata sandi ([p]assword):

`airdecap-ng -e {{essid}} -p {{kata_sandi}} {{jalan/menuju/tangkapan_jaringan.cap}}`

- Buka enkripsi WPA/WPA2 dari file tangkapan jaringan menggunakan [e]ssid dan kata sandi ([p]assword), tanpa menghilangkan informasi header jaringan:

`airdecap-ng -l -e {{essid}} -p {{kata_sandi}} {{jalan/menuju/tangkapan_jaringan.cap}}`

- Buka enkripsi WPA/WPA2 dari file tangkapan jaringan menggunakan [e]ssid dan kata sandi ([p]assword), dan saring menurut alamat MAC titik akses Wi-Fi:

`airdecap-ng -b {{alamat_mac}} -e {{essid}} -p {{kata_sandi}} {{jalan/menuju/tangkapan_jaringan.cap}}`
