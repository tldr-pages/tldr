# mysqlcheck

> Periksa dan perbaiki tabel-tabel MySQL.
> Informasi lebih lanjut: <https://dev.mysql.com/doc/refman/en/mysqlcheck.html>.

- Periksa sebuah tabel:

`mysqlcheck --check {{nama_tabel}}`

- Periksa sebuah tabel dan berikan kredensial untuk mengaksesnya:

`mysqlcheck --check {{nama_tabel}} --user {{nama_pengguna}} --password {{kata_sandi}}`

- Perbaiki sebuah tabel:

`mysqlcheck --repair {{nama_tabel}}`

- Optimalkan sebuah tabel:

`mysqlcheck --optimize {{nama_tabel}}`
