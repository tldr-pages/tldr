# alias

> Buat alias perintah -- kata-kata yang digantikan oleh utasan perintah (command).
> Alias menjadi kadaluarsa sampai sesi shell saat ini berakhir, kecuali jika didefinisikan di file konfigurasi shell, misalnya `~/.bashrc`.
> Informasi lebih lanjut: <https://www.gnu.org/software/bash/manual/bash.html#index-alias>.

- Tampilkan daftar seluruh alias yang terdaftar:

`alias`

- Buat suatu alias generik:

`alias {{kata}}="{{perintah}}"`

- Lihat perintah yang dirujuk oleh alias yang diberikan:

`alias {{kata}}`

- Hapus suatu perintah alias:

`unalias {{kata}}`

- Ubah perintah `rm` menjadi perintah interaktif:

`alias {{rm}}="{{rm --interactive}}"`

- Buat perintah `la` menjadi pintasan untuk `ls --all`:

`alias {{la}}="{{ls --all}}"`
