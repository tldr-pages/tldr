# adb install

> Android Debug Bridge Install: Memasang paket ke emulator Android atau perangkat Android terhubung.
> Informasi lebih lanjut: <https://developer.android.com/studio/command-line/adb>.

- Pasang aplikasi Android ke emulator/perangkat:

`adb install {{jalan/menuju/berkas.apk}}`

- Pasang aplikasi Android menuju emulator/perangkat tertentu (berdasarkan nomor serial yang didapatkan dari `adb devices`, mengesampingkan nilai `$ANDROID_SERIAL`):

`adb -s {{nomor_serial}} install {{jalan/menuju/file.apk}}`

- Pasang ulang aplikasi yang sudah ada, menjaga datanya:

`adb install -r {{jalan/menuju/berkas.apk}}`

- Pasang aplikasi Android versi lawas dari aplikasi Android yang sudah terpasang pada perangkat (khusus aplikasi debug):

`adb install -d {{jalan/menuju/berkas.apk}}`

- Berikan semua izin yang terdaftar di manifest aplikasi:

`adb install -g {{jalan/menuju/berkas.apk}}`

- Perbarui langsung paket terinstal dengan hanya memperbarui bagian dari APK yang berubah:

`adb install --fastdeploy {{jalan/menuju/berkas.apk}}`
