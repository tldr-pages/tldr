# mongo

> Program syel baris perintah lawas untuk manajemen pangkalan data (database) MongoDB. Lihat `mongosh` untuk program terbaru.
> Catatan: Seluruh opsi koneksi dapat digantikan dengan suatu string: `mongodb://pengguna@host:port/nama_db?authSource=nama_authdb`.
> Informasi lebih lanjut: <https://docs.mongodb.com/manual/reference/program/mongo>.

- Hubungkan terhadap suatu database lokal menggunakan port bawaan (`mongodb://localhost:27017`):

`mongo`

- Hubungkan kepada suatu database:

`mongo --host {{host}} --port {{port}} {{nama_db}}`

- Masuk dengan akses menggunakan suatu username (nama pengguna) pada suatu database (Anda akan diminta untuk memasukkan kata sandi):

`mongo --host {{host}} --port {{port}} --username {{pengguna}} --authenticationDatabase {{nama_authdb}} {{nama_db}}`

- Jalankan suatu perintah JavaScript pada suatu database:

`mongo --eval '{{JSON.stringify(db.foo.findOne())}}' {{nama_db}}`
