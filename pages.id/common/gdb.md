# gdb

> GNU Debugger.
> Informasi lebih lanjut: <https://www.gnu.org/software/gdb>.

- Menjalankan debug pada sebuah berkas yang dapat dieksekusi:

`gdb {{berkas_exe}}`

- Menambahkan sebuah proses pada gdb:

`gdb -p {{berkas_exe}}`

- Menjalankan debug dengan berkas core:

`gdb -c {{core}} {{berkas_exe}}`

- Mengeksekusi perintah GDB pada saat dijanlakan:

`gdb -ex "{{perintah}}" {{berkas_exe}}`

- Menjalankan gdb dan melemparkan argumen pada berkas yang dieksekusi:

`gdb --args {{berkas_exe}} {{argumen1}} {{argumen2}}`
