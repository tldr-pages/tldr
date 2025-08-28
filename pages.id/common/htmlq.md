# htmlq

> Gunakan selektor CSS untuk mengekstrak konten dari berkas-berkas HTML.
> Informasi lebih lanjut: <https://github.com/mgdm/htmlq>.

- Dapatkan seluruh elemen HTML yang memuat class `card`:

`cat {{jalan/menuju/berkas.html}} | htmlq '.card'`

- Dapatkan konten teks dari paragraf pertama:

`cat {{jalan/menuju/berkas.html}} | htmlq --text 'p:first-of-type'`

- Tampilkan seluruh tautan dalam suatu laman:

`cat {{jalan/menuju/berkas.html}} | htmlq --attribute href 'a'`

- Hapus seluruh gambar dan elemen SVG dari suatu laman:

`cat {{jalan/menuju/berkas.html}} | htmlq --remove-nodes 'img' --remove-nodes 'svg'`

- Simpan laman input secara cetak-cantik menuju suatu berkas output:

`htmlq --pretty --filename {{jalan/menuju/input.html}} --output {{jalan/menuju/output.html}}`
