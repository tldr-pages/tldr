# xcodes

> Unduh, pasang, dan atur pemasangan aplikasi Xcode dalam versi yang berbeda.
> Informasi lebih lanjut: <https://github.com/xcodesorg/xcodes>.

- Tampilkan daftar versi Xcode yang terpasang:

`xcodes installed`

- Tampilkan daftar versi Xcode yang tersedia:

`xcodes list`

- Pilih versi Xcode yang hendak digunakan sebagai default, dengan menyertakan versi atau lokasi aplikasi

`xcodes select {{versi_xcode|jalan/menuju/Xcode.app}}`

- Unduh dan pasang Xcode versi tertentu:

`xcodes install {{versi_xcode}}`

- Pasang aplikasi Xcode terkini dan pilih sebagai versi default:

`xcodes install --latest --select`

- Unduh Xcode versi tertentu ke sebuah direktori tanpa memasangnya ke dalam perangkat:

`xcodes-download {{versi_xcode}} --directory {{jalan/menuju/direktori}}`
