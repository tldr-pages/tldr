# mysqld

> Memulai peladen (server) basis data MySQL.
> Informasi lebih lanjut: <https://dev.mysql.com/doc/refman/en/mysqld.html>.

- Memulai peladen basis data MySQL:

`mysqld`

- Memulai peladen, dengan mencetak pesan kesalahan ke konsol:

`mysqld --console`

- Memulai peladen, dengan menyimpan keluaran log ke berkas log tertentu:

`mysqld --log={{jalan/ke/berkas.log}}`

- Tampilkan argumen baku (default) beserta nilainya lalu keluar:

`mysqld --print-defaults`

- Memulai peladen, dengan membaca argumen dan nilai dari sebuah berkas:

`mysqld --defaults-file={{jalan/ke/berkas}}`

- Memulai peladen dan mendengarkan pada port tertentu:

`mysqld --port={{port}}`

- Tampilkan bantuan:

`mysqld --verbose --help`
