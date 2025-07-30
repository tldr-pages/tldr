# wc

> Hitung baris, kata, dan bita.
> Informasi lebih lanjut: <https://www.gnu.org/software/coreutils/manual/html_node/wc-invocation.html>.

- Hitung semua baris dalam suatu berkas:

`wc {{[-l|--lines]}} {{jalur/ke/berkas}}`

- Hitung semua kata dalam suatu berkas:

`wc {{[-w|--words]}} {{jalur/ke/berkas}}`

- Hitung semua bita dalam suatu berkas:

`wc {{[-c|--bytes]}} {{jalur/ke/berkas}}`

- Hitung semua karakter dalam suatu berkas (dengan memperhitungkan karakter multi-bita):

`wc {{[-m|--chars]}} {{jalur/ke/berkas}}`

- Hitung semua baris, kata, dan byte dari `stdin`:

`{{temukan .}} | wc`

- Hitung panjang baris yang terpanjang dalam jumlah karakter:

`wc {{[-L|--max-line-length]}} {{jalur/ke/berkas}}`
