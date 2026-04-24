# adb shell pm

> Manajer paket aplikasi Android.
> Informasi lebih lanjut: <https://developer.android.com/tools/adb>.

- Tampilkan daftar paket yang terpasang:

`adb shell pm list packages`

- Pasang suatu paket aplikasi dari alamat tertentu:

`adb shell pm install /{{jalan/menuju/aplikasi}}.apk`

- Hapus suatu paket aplikasi dari perangkat Android:

`adb shell pm uninstall {{paket}}`

- Hapus seluruh data aplikasi untuk suatu paket:

`adb shell pm clear {{paket}}`

- Aktifkan suatu paket atau komponen:

`adb shell pm enable {{paket_atau_kelas}}`

- Nonaktifkan suatu paket atau komponen:

`adb shell pm disable-user {{paket_atau_kelas}}`

- Berikan suatu ijin untuk suatu aplikasi:

`adb shell pm grant {{paket}} {{android.permission.CAMERA|android.permission.ACCESS_FINE_LOCATION|android.permission.READ_CONTACTS|...}}`

- Cabut suatu ijin untuk suatu aplikasi:

`adb shell pm revoke {{paket}} {{android.permission.CAMERA|android.permission.ACCESS_FINE_LOCATION|android.permission.READ_CONTACTS|...}}`
