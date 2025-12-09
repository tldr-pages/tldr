# ip

> Atur konfigurasi IP.
> Gunakan mode konfigurasi untuk mengakses perintah ini..
> Informasi lebih lanjut: <https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/ipaddr/command/ipaddr-cr-book.html>.

- Atur versi SSH:

`ip ssh version {{2}}`

- Atur alamat perangkat saat ini (Perintah ini dijalankan di dalam perintah `interface`):

`ip address {{10.0.0.1}} {{255.255.255.0}}`

- Atur alamat perangkat menggunakan DHCP (Perintah ini dijalankan di dalam perintah `interface`):

`ip address dhcp`

- Setel suatu alamat domain:

`ip domain-name {{example.com}}`
