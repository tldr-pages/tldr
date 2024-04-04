# mongod

> Peladen basis data MongoDB.
> Informasi lebih lanjut: <https://docs.mongodb.com/manual/reference/program/mongod>.

- Tentukan direktori penyimpanan basis data (default: `/data/db` dalam Linux dan macOS, `C:\data\db` dalam Windows):

`mongod --dbpath {{jalan/menuju/direktori}}`

- Tentukan berkas konfigurasi basis data:

`mongod --config {{jalan/menuju/berkas}}`

- Tentukan port yang akan digunakan (default: 27017):

`mongod --port {{port}}`

- Tentukan tingkat pencatatan perilaku (profiling) peladen basis data. 0 mati, 1 hanya operasi lambat, 2 semuanya (default: 0):

`mongod --profile {{0|1|2}}`
