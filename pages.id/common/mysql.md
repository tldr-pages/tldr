# mysql

> Alat baris perintah MySQL.
> Informasi lebih lanjut: <https://manned.org/mysql>.

- Menghubungkan ke sebuah basis data:

`mysql {{nama_basis_data}}`

- Menghubungkan ke basis data; pengguna akan diminta memasukkan kata sandi:

`mysql {{[-u|--user]}} {{nama_pengguna}} {{[-p|--password]}} {{nama_basis_data}}`

- Menghubungkan ke basis data pada host lain:

`mysql {{[-h|--host]}} {{host_basis_data}} {{nama_basis_data}}`

- Menghubungkan ke basis data melalui soket Unix:

`mysql {{[-S|--socket]}} {{jalan/ke/soket.sock}}`

- Menjalankan pernyataan SQL dalam sebuah berkas skrip (batch):

`mysql {{[-e|--execute]}} "source {{nama_berkas.sql}}" {{nama_basis_data}}`

- Memulihkan (restore) basis data dari cadangan yang dibuat dengan mysqldump (pengguna akan diminta memasukkan kata sandi):

`mysql < {{jalan/ke/cadangan.sql}} {{[-u|--user]}} {{nama_pengguna}} {{[-p|--password]}} {{nama_basis_data}}`

- Memulihkan semua basis data dari berkas cadangan (pengguna akan diminta memasukkan kata sandi):

`mysql < {{jalan/ke/cadangan.sql}} {{[-u|--user]}} {{nama_pengguna}} {{[-p|--password]}}`
