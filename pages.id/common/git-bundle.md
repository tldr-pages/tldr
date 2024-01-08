# git bundle

> Bungkus seluruh objek dan referensi internal Git ke dalam suatu berkas arsip.
> Informasi lebih lanjut: <https://git-scm.com/docs/git-bundle>.

- Buat sebuah berkas (bundle) dengan seluruh objek dan referensi Git pada cabang tertentu:

`git bundle create {{jalan/menuju/berkas.bundle}} {{nama_cabang}}`

- Bungkus objek dan referensi untuk seluruh cabang:

`git bundle create {{jalan/menuju/berkas.bundle}} --all`

- Bungkus objek dan referensi untuk lima komit terakhir pada cabang saat ini:

`git bundle create {{jalan/menuju/berkas.bundle}} -{{5}} {{HEAD}}`

- Bungkus objek dan referensi untuk perubahan sejak 7 hari terakhir:

`git bundle create {{jalan/menuju/berkas.bundle}} --since={{7.days}} {{HEAD}}`

- Cek apakah suatu berkas bundle bersifat valid dan dapat diaplikasikan ke dalam repositori saat ini:

`git bundle verify {{jalan/menuju/berkas.bundle}}`

- Cetak daftar berkas referensi yang terkandung dalam berkas bundle menuju stdout:

`git bundle unbundle {{jalan/menuju/berkas.bundle}}`

- Buka dan pakai isi bungkusan untuk suatu cabang pada repositori saat ini:

`git pull {{jalan/menuju/berkas.bundle}} {{nama_cabang}}`
