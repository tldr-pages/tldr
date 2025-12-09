# aapt

> Alat Pemaketan Android Asset.
> Susun dan buat paket resource aplikasi Android.
> Informasi lebih lanjut: <https://manned.org/aapt>.

- Tampilkan daftar berkas yang termuat dalam suatu arsip APK:

`aapt list {{jalan/menuju/aplikasi.apk}}`

- Tampilkan metadata aplikasi (versi, izin, dsb.):

`aapt dump badging {{jalan/menuju/aplikasi.apk}}`

- Buat suatu arsip APK baru dengan berkas dari direktori yang ditentukan:

`aapt package -F {{jalan/menuju/aplikasi.apk}} {{jalan/menuju/direktori}}`
