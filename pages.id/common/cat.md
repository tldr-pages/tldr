# cat

> Mencetak dan menggabungkan berkas.

- Mencetak konten berkas ke keluaran standar:

`cat {{berkas}}`

- Menggabungkan konten beberapa berkas ke berkas tujuan:

`cat {{berkas1}} {{berkasw}} > {{berkas_tujuan}}`

- Menambahkan konten beberapa berkas ke berkas tujuan:

`cat {{berkas1}} {{berkas2}} >> {{berkas_tujuan}}`

- Memberi nomor pada semua baris keluaran:

`cat -n {{berkas}}`

- Menampilkan karakter yang tidak dapat dicetak dan spasi (dengan awalan `M-`jika non-ASCII):

`cat -v -t -e {{berkas}}`
