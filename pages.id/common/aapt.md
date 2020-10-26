# aapt

> Alat Pemaketan Android Asset.
> Menyusun dan memaketkan resource aplikasi Android.

- Daftar berkas-berkas yang termuat dalam arsip APK:

`aapt list {{alamat/ke/aplikasi.apk}}`

- Menampilkan metadata aplikasi (versi, izin, dsb.):

`aapt dump badging {{alamat/ke/aplikasi.apk}}`

- Membuat arsip APK baru dengan berkas dari direktory yang ditentukan:

`aapt package -F {{alamat/ke/aplikasi.apk}} {{alamat/ke/direktori}}`
