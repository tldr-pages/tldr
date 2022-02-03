# gdb

> GNU Debugger.
> Informasi lebih lanjut: <https://www.gnu.org/software/gdb>.

- Menjalankan debug pada sebuah berkas yang dapat dieksekusi:

`gdb {{berkas-exe}}`

- menambahkan sebuah proses pada gdb:

`gdb -p {{berkas-exe}}`

- Menjalankan debug dengan berkas core:

`gdb -c {{core}} {{berkas-exe}}`

- Mengeksekusi perintah GDB pada saat dijanlakan:

`gdb -ex "{{perintah}}" {{berkas-exe}}`

- Menjalankan gdb dan melemparkan argumen pada berkas yang dieksekusi:

`gdb --args {{berkas-exe}} {{argumen1}} {{argumen2}}`
