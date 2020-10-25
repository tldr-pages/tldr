# aapt

> Alat Pemaketan Android Asset.
> Menyusun dan memaketkan resource aplikasi Android.

- Daftar berkas-berkas yang termuat dalam arsip APK:

`aapt list {{path/to/aplikasi.apk}}`

- Menampilkan metadata aplikasi (versi, izin, dsb.):

`aapt dump badging {{path/to/aplikasi.apk}}`

- Membuat arsip APK baru dengan berkas dari direktory yang ditentukan:

`aapt package -F {{path/to/aplikasi.apk}} {{path/to/direktori}}`
