# adb connect

> Hubungkan menuju suatu perangkat Android secara nirkabel.
> Informasi lebih lanjut: <https://developer.android.com/tools/adb>.

- Hubungkan menuju suatu perangkat Android (alamat dan kode berpasangan/pairing dapat dilihat pada pengaturan pengembang):

`adb pair {{alamat_ip}}:{{port}}`

- Hubungkan menuju suatu perangkat (nomor port akan berbeda dengan mode pairing):

`adb connect {{alamat_ip}}:{{port}}`

- Putuskan sambungan suatu perangkat:

`adb disconnect {{alamat_ip}}:{{port}}`
