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

`adb install -r {{path/to/file.apk}}`

- Menyalin berkas/direktori dari perangkat tujuan:

`adb pull {{path/to/device_file_or_directory}} {{path/to/local_destination_directory}}`

- Menyalin berkas/direktori ke perangkat tujuan:

`adb push {{path/to/local_file_or_directory}} {{path/to/device_destination_directory}}`

- Mendapatkan daftar perangkat yang terhubung:

`adb devices`
