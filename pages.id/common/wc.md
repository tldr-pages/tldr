# wc

> Hitung baris, kata, dan bita.
> Informasi lebih lanjut: <https://www.gnu.org/software/coreutils/manual/html_node/wc-invocation.html>.

- Hitung semua baris dalam suatu berkas:

`wc {{[-l|--lines]}} {{path/to/file}}`

- Hitung semua kata dalam suatu berkas:

`wc {{[-w|--words]}} {{path/to/file}}`

- Hitung semua bita dalam suatu berkas:

`wc {{[-c|--bytes]}} {{path/to/file}}`

- Hitung semua karakter dalam suatu berkas (dengan memperhitungkan karakter multi-bita):

`wc {{[-m|--chars]}} {{path/to/file}}`

- Hitung semua baris, kata, dan byte dari `stdin`:

`{{find .}} | wc`

- Hitung panjang baris yang terpanjang dalam jumlah karakter:

`wc {{[-L|--max-line-length]}} {{path/to/file}}`
