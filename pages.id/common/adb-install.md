# adb install

> Android Debug Bridge Install: Menginstal paket ke emulator Android atau perangkat Android terhubung.
> Informasi lebih lanjut: <https://developer.android.com/studio/command-line/adb>.

- Menginstal aplikasi Android ke emulator/perangkat:

`adb install {{path/to/file.apk}}`

- Menginstal ulang aplikasi yang sudah ada, menjaga datanya:

`adb install -r {{path/to/file.apk}}`

- Memberikan semua izin yang terdaftar di manifest aplikasi:

`adb install -g {{path/to/file.apk}}`

- Memperbarui langsung paket terinstal dengan hanya memperbarui bagian dari APK yang berubah:

`Adb install --fastdeploy {{path/to/file.apk}}`
