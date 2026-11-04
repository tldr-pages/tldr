# gdb

> GNU Debugger, alat pengawakutu program komputer.
> Informasi lebih lanjut: <https://sourceware.org/gdb/current/onlinedocs/gdb#Invocation>.

- Jalankan pengawakutu pada sebuah berkas program yang dapat dieksekusi:

`gdb {{jalan/menuju/berkas_exe}}`

- Tambahkan suatu proses untuk diawasi oleh `gdb`:

`gdb {{[-p|--pid]}} {{berkas_exe}}`

- Jalankan pengawakutu dengan berkas core (rekaman memnori dan diagnostik kesalahan program) yang ditentukan:

`gdb {{[-c|--core]}} {{jalan/menuju/berkas_core}} {{jalan/menuju/berkas_exe}}`

- Kirim perintah menuju pengawakutu pada saat dijalankan:

`gdb {{[-ex|--eval-command]}} "{{perintah}}" {{jalan/menuju/berkas_exe}}`

- Jalankan `gdb` dan teruskan argumen-argumen perintah ke dalam program yang diawasi:

`gdb --args {{jalan/menuju/berkas_exe}} {{argumen1 argumen2 ...}}`

- Lewati `debuginfod` dan fitur navigasi, dan kemudian segera cetak jejak balik eksekusi program jika terdapat kesalahan:

`gdb {{[-c|--core]}} {{jalan/menuju/berkas_core}} {{jalan/menuju/berkas_exe}} -iex 'set debuginfod enabled on' -iex 'set pagination off' -ex bt`
