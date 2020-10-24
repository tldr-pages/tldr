# aapt

> Alat Pemaketan Android Asset.
> Menyusun dan memaketkan resource aplikasi Android.

- Daftar berkas-berkas yang termuat dalam arsip APK:

`aapt list {{path/to/app.apk}}`

- Menampilkan metadata aplikasi (versi, izin, dsb.):

`aapt dump badging {{path/to/app.apk}}`

- Membuat arsip APK baru dengan berkas dari direktory yang ditentukan:

`aapt package -F {{path/to/app.apk}} {{path/to/directory}}`
