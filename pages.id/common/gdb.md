# gdb

> GNU Debugger, alat pengawakutu program komputer.
> Informasi lebih lanjut: <https://www.gnu.org/software/gdb>.

- Jalankan pengawakutu pada sebuah berkas program yang dapat dieksekusi:

`gdb {{berkas_exe}}`

- Tambahkan suatu proses untuk diawasi oleh gdb:

`gdb -p {{berkas_exe}}`

- Jalankan pengawakutu dengan berkas core:

`gdb -c {{core}} {{berkas_exe}}`

- Kirim perintah menuju pengawakutu pada saat dijalankan:

`gdb -ex "{{perintah}}" {{berkas_exe}}`

- Lemparkan argumen terhadap berkas program yang dieksekusi saat hendak diawasi oleh GDB:

`gdb --args {{berkas_exe}} {{argumen1}} {{argumen2}}`
