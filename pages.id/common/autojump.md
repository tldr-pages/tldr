# autojump

> Lompat dengan cepat menuju direktori-direktori yang paling sering anda kunjungi.
> Alias seperti `j` atau `jc` sudah disediakan untuk mengurangi pengetikan.
> Informasi lebih lanjut: <https://github.com/wting/autojump>.

- Lompat menuju direktori yang mengandung pola yang diberikan:

`j {{pola}}`

- Lompat menuju sub-direktori (anak) dari direktori saat ini yang mengandung pola yang diberikan:

`jc {{pola}}`

- Buka direktori yang mengandung pola yang diberikan dalam aplikasi manajemen berkas sistem operasi:

`jo {{pola}}`

- Buang direktori-direktori dalam pangkalan data (database) `autojump` yang telah sebelumnya dihapus:

`j --purge`

- Tampilkan entri yang ada dalam pangkalan data `autojump`:

`j {{[-s|--stat]}}`
