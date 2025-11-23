# choose

> Alternatif ramah-manusia dan cepat terhadap perintah cut dan (terkadang) awk.
> Informasi lebih lanjut: <https://github.com/theryangeary/choose#usage>.

- Cetak item ke-5 dari suatu baris (dimulai dari 0):

`choose {{4}}`

- Cetak item pertama, ke-3, dan ke-5 dari suatu baris, di mana kumpulan item dipisahkan menggunakan karakter ':' daripada spasi:

`choose --field-separator '{{:}}' {{0}} {{2}} {{4}}`

- Cetak isi seluruh item dari urutan ke-2 menuju ke-5 dalam baris, termasuk item ke-5:

`choose {{1}}:{{4}}`

- Cetak isi seluruh item dari urutan ke-2 menuju ke-5 dalam baris, kecuali item ke-5:

`choose --exclusive {{1}}:{{4}}`

- Cetak isi seluruh item dari awal baris menuju item ke-3:

`choose :{{2}}`

- Cetak isi seluruh item dari awal baris menuju item ke-3 (eksklusif):

`choose --exclusive :{{2}}`

- Cetak isi seluruh item dari urutan ke-3 hingga akhir baris:

`choose {{2}}:`

- Cetak item terakhir dari suatu baris:

`choose {{-1}}`
