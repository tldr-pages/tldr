# mongosh

> Program syel baris perintah baru untuk manajemen pangkalan data (database) MongoDB, menggantikan `mongo`.
> Catatan: Seluruh opsi koneksi dapat digantikan dengan suatu string: `mongodb://pengguna@host:port/nama_db?authSource=nama_authdb`.
> Informasi lebih lanjut: <https://www.mongodb.com/docs/mongodb-shell>.

- Hubungkan terhadap suatu database lokal menggunakan port bawaan (`mongodb://localhost:27017`):

`mongosh`

- Hubungkan kepada suatu database:

`mongosh --host {{host}} --port {{port}} {{nama_db}}`

- Masuk dengan akses menggunakan suatu username (nama pengguna) pada suatu database (Anda akan diminta untuk memasukkan kata sandi):

`mongosh --host {{host}} --port {{port}} --username {{pengguna}} --authenticationDatabase {{nama_authdb}} {{nama_db}}`

- Jalankan suatu perintah JavaScript pada suatu database:

`mongosh --eval '{{JSON.stringify(db.foo.findOne())}}' {{nama_db}}`
