# mysqlbinlog

> Utilitas untuk memproses berkas log biner (binary log) MySQL.
> Informasi lebih lanjut: <https://dev.mysql.com/doc/refman/en/mysqlbinlog.html>.

- Menampilkan peristiwa (event) dari berkas log biner tertentu:

`mysqlbinlog {{jalan/ke/binlog}}`

- Menampilkan entri dari log biner untuk basis data tertentu:

`mysqlbinlog --database {{nama_basis_data}} {{jalan/ke/binlog}}`

- Menampilkan peristiwa dari log biner di antara tanggal-tanggal tertentu:

`mysqlbinlog --start-datetime='{{2022-01-01 01:00:00}}' --stop-datetime='{{2022-02-01 01:00:00}}' {{jalan/ke/binlog}}`

- Menampilkan peristiwa dari log biner di antara posisi-posisi tertentu:

`mysqlbinlog --start-position={{100}} --stop-position={{200}} {{jalan/ke/binlog}}`

- Menampilkan log biner dari peladen (server) MySQL pada host yang diberikan:

`mysqlbinlog --host={{nama_host}} {{jalan/ke/binlog}}`
