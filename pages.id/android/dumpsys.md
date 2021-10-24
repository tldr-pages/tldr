# dumpsys

> Memberikan informasi tentang layanan (daemon) sistem milik Android.
> Perintah ini hanya dapat dijalankan melalui `adb shell`.
> Informasi lebih lanjut: <https://developer.android.com/studio/command-line/dumpsys>.

- Menampilkan informasi diagnostik terhadap seluruh layanan sistem Android:

`dumpsys`

- Menampilkan informasi diagnostik untuk layanan sistem tertentu:

`dumpsys {{layanan}}`

- Menampilkan daftar layanan sistem yang diketahui oleh `dumpsys`:

`dumpsys -l`

- Menampilkan daftar argumen yang diterima oleh sebuah layanan sistem:

`dumpsys {{layanan}} -h`

- Mengecualikan layanan sistem tertentu dari informasi diagnostik yang ditampilkan:

`dumpsys --skip {{layanan}}`

- Menetapkan periode waktu habis dalam hitungan detik (10 detik secara default):

`dumpsys -t {{detik}}`
