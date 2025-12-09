# aireplay-ng

> Masukkan paket jaringan kepada jaringan nirkabel/wireless.
> Bagian dari paket perangkat lunak jaringan Aircrack-ng.
> Informasi lebih lanjut: <https://www.aircrack-ng.org/doku.php?id=aireplay-ng>.

- Kirim sejumlah paket terpisah berdasarkan alamat MAC titik akses, alamat MAC klien, dan antarmuka jaringan (interface):

`sudo aireplay-ng --deauth {{jumlah_paket}} --bssid {{alamat_mac_titik_akses}} --dmac {{alamat_mac_klien}} {{interface}}`
