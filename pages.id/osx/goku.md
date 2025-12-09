# goku

> Atur konfigurasi Karabiner.
> Informasi lebih lanjut: <https://github.com/yqrashawn/GokuRakuJoudo>.

- Buat file `karabiner.json` dengan konfigurasi default:

`goku`

- Buat file `karabiner.json` menggunakan konfigurasi khusus dari `config.edn`:

`goku --config {{jalan/menuju/config.edn}}`

- Tampilkan daftar perubahan konfigurasi baru menuju `stdout`, tanpa mengubah file `karabiner.json` yang sesungguhnya:

`goku --dry-run`

- Tampilkan hasil file konfigurasi yang baru menuju `stdout`, tanpa mengubah file `karabiner.json` yang sesungguhnya:

`goku --dry-run-all`

- Tampilkan informasi bantuan:

`goku --help`

- Tampilkan informasi versi:

`goku --version`
