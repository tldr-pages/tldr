# adb shell pm list packages

> Tampilkan daftar paket aplikasi yang terpasang, dikenal, atau disaring dalam suatu perangkat Android.
> Informasi lebih lanjut: <https://developer.android.com/tools/adb>.

- Tampilkan daftar seluruh paket yang terpasang:

`adb shell pm list packages`

- Tampilkan seluruh paket beserta alamat berkas APK yang mengarah menuju paket aplikasi:

`adb shell pm list packages -f`

- Hanya tampilkan daftar paket yang dinonaktifkan:

`adb shell pm list packages -d`

- Hanya tampilkan daftar paket yang diaktifkan:

`adb shell pm list packages -e`

- Hanya tampilkan daftar paket bawaan [s]istem Android:

`adb shell pm list packages -s`

- Hanya tampilkan daftar paket pihak ke-[3] (non-bawaan):

`adb shell pm list packages -3`

- Tampilkan pula ID aplikasi yang membantu memasang setiap paket:

`adb shell pm list packages -i`
