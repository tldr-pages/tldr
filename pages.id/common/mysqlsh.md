# mysqlsh

> Klien MySQL tingkat lanjut (advanced) yang mendukung SQL, JavaScript, dan Python.
> Alat ini menawarkan fitur untuk mengelola klaster InnoDB dan koleksi penyimpanan dokumen (document store).
> Informasi lebih lanjut: <https://manned.org/mysqlsh>.

- Mulai MySQL Shell dalam mode interaktif:

`mysqlsh`

- Hubungkan ke sebuah peladen (server) MySQL:

`mysqlsh --user {{nama_pengguna}} --host {{nama_host}} --port {{port}}`

- Jalankan sebuah pernyataan SQL pada peladen lalu keluar:

`mysqlsh --user {{nama_pengguna}} --execute '{{pernyataan_sql}}'`

- Mulai MySQL Shell dalam mode JavaScript:

`mysqlsh --js`

- Mulai MySQL Shell dalam mode Python:

`mysqlsh --py`

- Impor dokumen JSON ke dalam koleksi MySQL:

`mysqlsh --import {{jalan/ke/berkas.json}} --schema {{nama_skema}} --collection {{nama_koleksi}}`

- Aktifkan keluaran yang detail (verbose):

`mysqlsh --verbose`
