# mongod

> Server database MongoDB.
> Informasi lebih lanjut: <https://docs.mongodb.com/manual/reference/program/mongod>.

- Menentukan berkas konfigurasi:

`mongod --config {{nama_berkas}}`

- Menentukan port yang digunakan:

`mongod --port {{port}}`

- Menentukan tingkat pencatatan perilaku (profiling) database. 0 mati, 1 hanya operasi lambat, 2 semuanya:

`mongod --profile {{0|1|2}}`
