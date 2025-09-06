# scoop bucket

> Kelola bucket: Repository Git yang berisi berkas yang menjelaskan bagaimana scoop menginstall aplikasi.
> Jika Scoop tidak tahu di mana sebuah bucket terletak, maka lokasi repositori harus ditentukan.
> Informasi lebih lanjut: <https://github.com/lukesampson/scoop/wiki/Buckets>.

- Tampilkan daftar semua bucket yang sedang digunakan:

`scoop bucket list`

- Tampilkan daftar semua bucket yang dikenal:

`scoop bucket known`

- Tambahkan bucket yang dikenal berdasarkan namanya:

`scoop bucket add {{nama}}`

- Tambahkan bucket yang tidak dikenal bersarkan nama dan URL repository Git:

`scoop bucket add {{nama}} {{https://example.com/repository.git}}`

- Hapus suatu bucket berdasarkan namanya:

`scoop bucket rm {{nama}}`
