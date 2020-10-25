# adb install

> Android Debug Bridge Install: Menginstal paket ke emulator Android atau perangkat Android terhubung.
> Informasi lebih lanjut: <https://developer.android.com/studio/command-line/adb>.

- Menginstal aplikasi Android ke emulator/perangkat:

`adb install {{alamat/ke/berkas.apk}}`

- Menginstal ulang aplikasi yang sudah ada, menjaga datanya:

`adb install -r {{alamat/ke/berkas.apk}}`

- Memberikan semua izin yang terdaftar di manifest aplikasi:

`adb install -g {{alamat/ke/berkas.apk}}`

- Memperbarui langsung paket terinstal dengan hanya memperbarui bagian dari APK yang berubah:

`Adb install --fastdeploy {{alamat/ke/berkas.apk}}`
