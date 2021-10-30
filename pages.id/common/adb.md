# adb

> Android Debug Bridge: berkomunikasi dengan emulator Android atau perangkat Android terhubung.
> Kami mempunyai dokumentasi terpisah untuk menggunakan subperintah seperti `adb shell`.
> Informasi lebih lanjut: <https://developer.android.com/studio/command-line/adb>.

- Cek apakah proses server adb telah dimulai dan memulainya:

`adb start-server`

- Menghentikan proses server adb:

`adb kill-server`

- Memulai shell jarak jauh pada emulator/perangkat tujuan:

`adb shell`

- Menginstal aplikasi Android ke emulator/perangkat tujuan:

`adb install -r {{alamat/ke/berkas.apk}}`

- Menyalin berkas/direktori dari perangkat tujuan:

`adb pull {{alamat/ke/berkas_atau_direktori_perangkat}} {{alamat/ke/direktori_lokal_tujuan}}`

- Menyalin berkas/direktori ke perangkat tujuan:

`adb push {{alamat/ke/berkas_atau_direktori_lokal}} {{alamat/ke/direktori_perangkat_tujuan}}`

- Mendapatkan daftar perangkat yang terhubung:

`adb devices`
