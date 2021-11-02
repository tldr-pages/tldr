# scoop bucket

> Mengelola bucket: Repository Git yang berisi berkas yang menjelaskan bagaimana scoop menginstall aplikasi.
> Jika Scoop tidak tahu dimana sebuah bucket terletak, lokasi repository harus ditentukan.
> Informasi lebih lanjut: <https://github.com/lukesampson/scoop/wiki/Buckets>.

- Menampilkan daftar semua bucket yang sedang digunakan:

`scoop bucket list`

- Menampilkan daftar semua bucket yang dikenal:

`scoop bucket known`

- Menambahkan bucket yang dikenal berdasarkan namanya:

`scoop bucket add {{nama}}`

- Menambahkan bucket yang tidak dikenal bersarkan nama dan URL repository Git:

`scoop bucket add {{nama}} {{https://contoh.com/repository.git}}`

- Menghapus bucket berdasarkan namanya:

`scoop bucket rm {{nama}}`
