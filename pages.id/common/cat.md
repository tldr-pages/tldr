# cat

> Cetak dan menggabungkan berkas.
> Informasi lebih lanjut: <https://www.gnu.org/software/coreutils/cat>.

- Cetak konten berkas menuju `stdout`:

`cat {{jalan/menuju/berkas}}`

- Gabungkan konten beberapa berkas ke berkas tujuan:

`cat {{jalan/menuju/berkas1 jalan/menuju/berkas2 ...}} > {{jalan/menuju/berkas_tujuan}}`

- Tambahkan konten beberapa berkas ke berkas tujuan:

`cat {{jalan/menuju/berkas1 jalan/menuju/berkas2 ...}} >> {{jalan/menuju/berkas_tujuan}}`

- Salin isi suatu file menuju file tujuan tanpa proses buffering:

`cat -u {{/dev/tty12}} > {{/dev/tty13}}`

- Tulis isi `stdin` menuju suatu file:

`cat - > {{jalan/menuju/berkas}}`
