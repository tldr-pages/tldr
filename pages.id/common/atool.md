# atool

> Suatu skrip untuk mengatur isi berkas arsip dengan berbagai format.
> `atool` menggunakan beragam program pengarsip eksternal namun menyediakan antarmuka baris perintah yang sama untuk melihat isi, mengekstrak, membangun, dan mengatur arsip.
> Informasi lebih lanjut: <https://manned.org/atool>.

- Tampilkan isi berkas di dalam suatu arsip:

`atool {{[-l|--list]}} {{jalan/menuju/arsip.zip}}`

- Ekstrak isi arsip (akan membuat subdirektori jika diperlukan):

`atool {{[-x|--extract]}} {{arsip.tar.gz}}`

- Ekstrak isi arsip menuju suatu direktori:

`atool {{[-X|--extract-to]}} {{jalan/menuju/direktori_luaran}} {{arsip.rar}}`

- Tampilkan isi suatu berkas yang tersimpan dari arsip menuju `stdout` (seperti `cat`):

`atool {{[-c|--cat]}} {{arsip.tar}} {{jalan/menuju/berkas_dalam_arsip.txt}}`

- Buat suatu berkas arsip untuk kumpulan berkas dan/atau direktori yang ditentukan:

`atool {{[-a|--add]}} {{arsip_baru.zip}} {{jalan/menuju/berkas1 jalan/menuju/berkas2 ...}}`

- Tampilkan daftar isi berkas arsip dan kirim luaran program menuju program penampil teks dengan manajemen halaman:

`atool {{[-l|--list]}} {{[-p|--pager]}} {{arsip_besar.tar.bz2}}`

- Ekstrak beberapa arsip dengan sekali jalan (setiap arsip dapat diekstrak menuju masing-masing subdirektori bila dibutuhkan):

`atool {{[-x|--extract]}} {{[-e|--each]}} {{arsip1.zip}} {{arsip2.tar.gz}} {{*.rar}}`

- Kemas ulang suatu arsip dari suatu format menuju format lain (misalnya, `.tar.gz` menuju `.tar.7z`):

`atool {{[-r|--repack]}} {{arsip_lama.tar.gz}} {{arsip_baru.tar.7z}}`
