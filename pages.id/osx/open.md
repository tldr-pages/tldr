# open

> Membuka file, direktori, dan aplikasi.
> Informasi lebih lanjut: <https://ss64.com/osx/open.html>.

- Membuka sebuah file di dalam aplikasi default:

`open {{file.ext}}`

- Membuka aplikasi macOS tertentu:

`open -a "{{Aplikasi}}"`

- Membuka sebuah aplikasi macOS berdasarkan ID pengenal (bundle identifier) tertentu (gunakan `osascript` untuk mencari ID pengenal aplikasi secara mudah dan cepat):

`open -b {{com.domain.aplikasi}}`

- Buka direktori saat ini di dalam aplikasi Finder:

`open .`

- Lihat sebuah file di dalam aplikasi Finder:

`open -R {{jalan/menuju/file}}`

- Buka semua file dengan ekstensi tertentu di dalam aplikasi default pada direktori saat ini:

`open {{*.ext}}`
