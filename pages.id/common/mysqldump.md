# mysqldump

> Mencadangkan (backup) basis data MySQL.
> Lihat juga: `mysql`.
> Informasi lebih lanjut: <https://dev.mysql.com/doc/refman/en/mysqldump.html>.

- Membuat sebuah cadangan (backup); pengguna akan diminta memasukkan kata sandi:

`mysqldump --user {{nama_pengguna}} --password {{nama_basis_data}} --result-file={{jalan/ke/berkas.sql}}`

- Mencadangkan tabel tertentu dengan mengalihkan keluarannya ke sebuah berkas; pengguna akan diminta memasukkan kata sandi:

`mysqldump --user {{nama_pengguna}} --password {{nama_basis_data}} {{nama_tabel}} > {{jalan/ke/berkas.sql}}`

- Mencadangkan semua basis data dengan mengalihkan keluarannya ke sebuah berkas; pengguna akan diminta memasukkan kata sandi:

`mysqldump --user {{nama_pengguna}} --password --all-databases > {{jalan/ke/berkas.sql}}`

- Mencadangkan semua basis data dari host jarak jauh (remote) dengan mengalihkan keluarannya ke sebuah berkas; pengguna akan diminta memasukkan kata sandi:

`mysqldump --host={{ip_atau_nama_host}} --user {{nama_pengguna}} --password --all-databases > {{jalan/ke/berkas.sql}}`
