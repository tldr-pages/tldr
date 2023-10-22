# ipconfig

> Menampilkan dan mengatur konfigurasi jaringan dalam sistem operasi Windows.
> Informasi lebih lanjut: <https://learn.microsoft.com/windows-server/administration/windows-commands/ipconfig>.

- Menunjukkan daftar adaptor jaringan:

`ipconfig`

- Menunjukkan daftar adaptor jaringan secara lengkap:

`ipconfig /all`

- Memperbarui alamat IP sebuah adaptor jaringan:

`ipconfig /renew {{adaptor}}`

- Mengosongkan alamat-alamat IP yang disetel dalam sebuah adaptor jaringan:

`ipconfig /release {{adaptor}}`

- Mengosongkan cache DNS:

`ipconfig /flushdns`
