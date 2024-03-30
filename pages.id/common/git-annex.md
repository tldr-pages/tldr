# git annex

> Kelola file dengan Git, tanpa memeriksa isi kontennya.
> Saat file dianeksasi, kontennya dipindahkan ke penyimpanan key-value, dan symlink dibuat yang mengarah ke konten tersebut.
> Informasi lebih lanjut: <https://git-annex.branchable.com>.

- Inisialisasi sebuah repositori dengan Git annex:

`git annex init`

- Tambahkan file ke dalam repositori:

`git annex add {{jalan/menuju/file_atau_direktori}}`

- Tampilkan status file atau direktori saat ini:

`git annex status {{jalan/menuju/file_atau_direktori}}`

- Sinkronisasikan repositori lokal dengan sumber remote:

`git annex {{remote}}`

- Dapatkan isi file atau direktori:

`git annex get {{jalan/menuju/file_atau_direktori}}`

- Tampilkan informasi bantuan:

`git annex help`
