# html5validator

> Lakukan proses validasi sintaks terhadap suatu berkas HTML5.
> Informasi lebih lanjut: <https://github.com/svenkreiss/html5validator>.

- Lakukan proses validasi terhadap suatu berkas:

`html5validator {{jalan/menuju/berkas}}`

- Lakukan validasi terhadap seluruh berkas HTML pada suatu direktori:

`html5validator --root {{jalan/menuju/direktori}}`

- Tampilkan seluruh pesan peringatan (warning) dan galat (error):

`html5validator --show-warnings {{jalan/menuju/berkas}}`

- Lakukan proses validasi terhadap kumpulan berkas yang memenuhi glob kriteria nama berkas:

`html5validator --root {{jalan/menuju/direktori}} --match "{{*.html *.php}}"`

- Jangan lakukan validasi terhadap nama-nama berkas tertentu:

`html5validator --root {{jalan/menuju/direktori}} --blacklist "{{node_modules vendor}}"`

- Tampilkan laporan hasil analisa dalam format tertentu:

`html5validator --format {{gnu|xml|json|text}} {{jalan/menuju/berkas}}`

- Tampilkan log validasi dalam tingkat verbositas tertentu:

`html5validator --root {{jalan/menuju/direktori}} --log {{debug|info|warning}}`
