# buku

> Manajer markah buku (bookmark) lintas peramban (web browser).
> Informasi lebih lanjut: <https://github.com/jarun/Buku#usage>.

- Tampilkan seluruh markah yang mengandung "kata kunci" dan tag "privasi":

`buku {{kata kunci}} {{[-t|--stag]}} {{privasi}}`

- Tambahkan markah baru dengan tag "mesin pencari" dan "privasi":

`buku {{[-a|--add]}} {{https://example.com}} {{mesin pencari}}, {{privasi}}`

- Hapus suatu markah:

`buku {{[-d|--delete]}} {{id_markah}}`

- Buka program penyunting untuk menyunting suatu markah:

`buku {{[-w|--write]}} {{id_markah}}`

- Hapus tag "mesin pencari" dari suatu markah:

`buku {{[-u|--update]}} {{id_markah}} --tag - {{mesin pencari}}`
