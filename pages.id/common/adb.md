# adb

> Android Debug Bridge: berkomunikasi dengan emulator Android atau perangkat Android terhubung.
> Kami mempunyai dokumentasi terpisah untuk menggunakan subperintah seperti `adb shell`.
> Informasi lebih lanjut: <https://developer.android.com/tools/adb>.

- Cek apakah proses server adb telah dimulai dan memulainya:

`adb start-server`

- Hentikan proses server adb:

`adb kill-server`

- Mulai shell jarak jauh pada emulator/perangkat tujuan:

`adb shell`

- Instal aplikasi Android ke emulator/perangkat tujuan:

`adb install -r {{alamat/ke/berkas.apk}}`

- Salin berkas/direktori dari perangkat tujuan:

`adb pull {{alamat/ke/berkas_atau_direktori_perangkat}} {{alamat/ke/direktori_lokal_tujuan}}`

- Salin berkas/direktori ke perangkat tujuan:

`adb push {{alamat/ke/berkas_atau_direktori_lokal}} {{alamat/ke/direktori_perangkat_tujuan}}`

- Dapatkan daftar perangkat yang terhubung:

`adb devices`
