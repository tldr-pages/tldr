# androguard

> Lakukan rekayasa terbalik terhadap suatu aplikasi Android. Program ini ditulis dalam bahasa pemrograman Python.
> Informasi lebih lanjut: <https://github.com/androguard/androguard>.

- Tampilkan manifes aplikasi Android:

`androguard axml {{jalan/menuju/aplikasi.apk}}`

- Tampilkan metadata aplikasi (versi dan ID aplikasi):

`androguard apkid {{jalan/menuju/aplikasi.apk}}`

- Bongkar kode-kode program Java dari suatu aplikasi:

`androguard decompile {{jalan/menuju/aplikasi.apk}} --output {{jalan/menuju/direktori}}`
