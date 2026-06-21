# pm

> Manajer paket aplikasi Android.
> Informasi lebih lanjut: <https://developer.android.com/tools/adb#pm>.

- Tampilkan daftar paket yang terpasang:

`pm list packages`

- Pasang suatu paket aplikasi dari alamat tertentu:

`pm install /{{jalan/menuju/aplikasi}}.apk`

- Hapus suatu paket aplikasi dari perangkat Android:

`pm uninstall {{paket}}`

- Hapus seluruh data aplikasi untuk suatu paket:

`pm clear {{paket}}`

- Aktifkan suatu paket atau komponen:

`pm enable {{paket_atau_kelas}}`

- Nonaktifkan suatu paket atau komponen:

`pm disable-user {{paket_atau_kelas}}`

- Berikan suatu ijin untuk suatu aplikasi:

`pm grant {{paket}} {{android.permission.CAMERA|android.permission.ACCESS_FINE_LOCATION|android.permission.READ_CONTACTS|...}}`

- Cabut suatu ijin untuk suatu aplikasi:

`pm revoke {{paket}} {{android.permission.CAMERA|android.permission.ACCESS_FINE_LOCATION|android.permission.READ_CONTACTS|...}}`
