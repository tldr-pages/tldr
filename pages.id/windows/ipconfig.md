# ipconfig

> Tampilkan dan atur konfigurasi jaringan dalam sistem operasi Windows.
> Informasi lebih lanjut: <https://learn.microsoft.com/windows-server/administration/windows-commands/ipconfig>.

- Tampilkan daftar seluruh adaptor jaringan yang terpasang:

`ipconfig`

- Tampilkan daftar adaptor jaringan secara rinci:

`ipconfig /all`

- Perbarui alamat IP suatu adaptor jaringan:

`ipconfig /renew {{adaptor}}`

- Kosongkan alamat-alamat IP yang disetel dalam suatu adaptor jaringan:

`ipconfig /release {{adaptor}}`

- Tampilkan dafter informasi DNS yang disimpan dalam cache:

`ipconfig /displaydns`

- Kosongkan cache DNS:

`ipconfig /flushdns`
