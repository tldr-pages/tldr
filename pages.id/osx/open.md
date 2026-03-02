# open

> Buka berkas, direktori, dan aplikasi.
> Informasi lebih lanjut: <https://keith.github.io/xcode-man-pages/open.1.html>.

- Buka sebuah berkas di dalam aplikasi default:

`open {{berkas.ext}}`

- Buka aplikasi macOS tertentu:

`open -a "{{Aplikasi}}"`

- Buka sebuah aplikasi macOS berdasarkan ID pengenal (bundle identifier) tertentu (gunakan `osascript` untuk mencari ID pengenal aplikasi secara mudah dan cepat):

`open -b {{com.domain.aplikasi}}`

- Buka direktori saat ini di dalam aplikasi Finder:

`open .`

- Tampilkan lokasi suatu berkas di dalam aplikasi Finder:

`open -R {{jalan/menuju/berkas}}`

- Buka semua berkas dengan ekstensi tertentu di dalam aplikasi default pada direktori saat ini:

`open {{*.ext}}`

- Buka instansi baru ([n]ew) bagi suatu aplikasi, yang diidentifikasikan dengan [b]undle identifier:

`open -n -b {{com.domain.application}}`
