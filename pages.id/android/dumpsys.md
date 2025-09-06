# dumpsys

> Berikan informasi tentang layanan (daemon) sistem milik Android.
> Perintah ini hanya dapat dijalankan melalui `adb shell`.
> Informasi lebih lanjut: <https://developer.android.com/tools/dumpsys>.

- Tampilkan informasi diagnostik terhadap seluruh layanan sistem Android:

`dumpsys`

- Tampilkan informasi diagnostik untuk layanan sistem tertentu:

`dumpsys {{layanan}}`

- Tampilkan daftar layanan sistem yang diketahui oleh `dumpsys`:

`dumpsys -l`

- Tampilkan daftar argumen yang diterima oleh sebuah layanan sistem:

`dumpsys {{layanan}} -h`

- Kecualikan layanan sistem tertentu dari informasi diagnostik yang ditampilkan:

`dumpsys --skip {{layanan}}`

- Tetapkan periode waktu habis dalam hitungan detik (10 detik secara default):

`dumpsys -t {{detik}}`
