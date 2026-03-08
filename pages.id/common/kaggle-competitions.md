# kaggle competitions

> Mengelola kompetisi Kaggle.
> Informasi lebih lanjut: <https://github.com/Kaggle/kaggle-api/blob/main/docs/README.md#competitions>.

- Tampilkan daftar semua kompetisi:

`kaggle {{[c|competitions]}} list`

- Unduh data kompetisi:

`kaggle {{[c|competitions]}} download {{nama_kompetisi}}`

- Unduh berkas tertentu:

`kaggle {{[c|competitions]}} download {{nama_kompetisi}} {{[-f|--file]}} {{berkas}}`

- Kirim berkas ke sebuah kompetisi:

`kaggle {{[c|competitions]}} submit {{nama_kompetisi}} {{[-f|--file]}} {{jalan/ke/berkas}} {{[-m|--message]}} "{{pesan}}"`

- Tampilkan atau unduh papan peringkat (leaderboard):

`kaggle {{[c|competitions]}} leaderboard {{nama_kompetisi}} {{--show|--download}}`

- Lihat kiriman (submission):

`kaggle {{[c|competitions]}} submissions {{nama_kompetisi}}`
