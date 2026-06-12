# pm list packages

> Tampilkan daftar paket aplikasi yang terpasang, dikenal, atau disaring dalam suatu perangkat Android.
> Informasi lebih lanjut: <https://developer.android.com/tools/adb#pm>.

- Tampilkan daftar seluruh paket yang terpasang:

`pm list packages`

- Tampilkan seluruh paket beserta alamat berkas APK yang mengarah menuju paket aplikasi:

`pm list packages -f`

- Hanya tampilkan daftar paket yang dinonaktifkan:

`pm list packages -d`

- Hanya tampilkan daftar paket yang diaktifkan:

`pm list packages -e`

- Hanya tampilkan daftar paket bawaan [s]istem Android:

`pm list packages -s`

- Hanya tampilkan daftar paket pihak ke-[3] (non-bawaan):

`pm list packages -3`

- Tampilkan pula ID aplikasi yang membantu memasang setiap paket:

`pm list packages -i`
