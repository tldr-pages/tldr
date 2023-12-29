# airodump-ng

> Tangkap para paket dan tampilkan informasi mengenai jaringan nirkabel/wireless.
> Bagian dari paket perangkat lunak jaringan Aircrack-ng.
> Informasi lebih lanjut: <https://www.aircrack-ng.org/doku.php?id=airodump-ng>.

- Tangkap para paket dan tampilkan informasi jaringan nirkabel tertentu:

`sudo airodump-ng {{interface}}`

- Tangkap para paket dan tampilkan informasi jaringan nirkabel berdasarkan alamat MAC dan kanal jaringan, kemudian simpan hasil ke dalam suatu file:

`sudo airodump-ng --channel {{channel}} --write {{jalan/menuju/file}} --bssid {{alamat_mac}} {{interface}}`
