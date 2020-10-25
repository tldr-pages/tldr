# adb

> Android Debug Bridge: berkomunikasi dengan emulator Android atau perangkat Android terhubung.
> Informasi lebih lanjut: <https://developer.android.com/studio/command-line/adb>.

- Cek apakah proses server adb telah dimulai dan memulainya:

`adb start-server`

- Menghentikan proses server adb:

`adb kill-server`

- Memulai shell jarak jauh pada emulator/perangkat tujuan:

`adb shell`

- Menginstal aplikasi Android ke emulator/perangkat tujuan:

`adb install -r {{path/to/berkas.apk}}`

- Menyalin berkas/direktori dari perangkat tujuan:

`adb pull {{path/to/berkas_atau_direktori_perangkat}} {{path/to/direktori_lokal_tujuan}}`

- Menyalin berkas/direktori ke perangkat tujuan:

`adb push {{path/to/berkas_atau_direktori_lokal}} {{path/to/direktori_perangkat_tujuan}}`

- Mendapatkan daftar perangkat yang terhubung:

`adb devices`
