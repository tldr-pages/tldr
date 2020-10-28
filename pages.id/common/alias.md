# alias

> Membuat alias -- kata-kata yang digantikan oleh utasan perintah (command).
> Alias menjadi kadaluarsa sampai sesi shell saat ini berakhir, kecuali jika didefinisikan di file konfigurasi shell, misalnya `~/.bashrc`.

- Menampilkan daftar semua alias:

`alias`

- Membuat alias generik:

`alias {{kata}}="{{perintah}}"`

- Melihat perintah yang dirujuk oleh alias yang diberikan:

`alias {{kata}}`

- Menghapus alias dari sebuah perintah:

`unalias {{kata}}`

- Mengubah `rm` menjadi perintah interaktif:

`alias {{rm}}="{{rm -i}}"`

- Membuat `la` menjadi pintasan untuk `ls -a`:

`alias {{la}}="{{ls -a}}"`
