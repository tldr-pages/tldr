# adb

> Android Debug Bridge: berkomunikasi dengan emulator Android atau perangkat Android terhubung.
> Kami mempunyai dokumentasi terpisah untuk menggunakan subperintah seperti `shell`.
> Informasi lebih lanjut: <https://developer.android.com/tools/adb>.

- Periksa apakah proses server adb telah dimulai dan memulainya:

`adb start-server`

- Hentikan proses server adb:

`adb kill-server`

- Mulai shell jarak jauh pada emulator/perangkat tujuan:

`adb shell`

- Pasang suatu aplikasi Android menuju emulator/perangkat tujuan:

`adb install -r {{jalan/menuju/berkas.apk}}`

- Salin berkas/direktori dari perangkat tujuan:

`adb pull {{jalan/menuju/berkas_atau_direktori_perangkat}} {{jalan/menuju/direktori_lokal_tujuan}}`

- Salin berkas/direktori menuju perangkat tujuan:

`adb push {{jalan/menuju/berkas_atau_direktori_lokal}} {{jalan/menuju/direktori_perangkat_tujuan}}`

- Tampilkan daftar perangkat yang terhubung:

`adb devices`
