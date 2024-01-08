# git check-ignore

> Analisa kumpulan file yang diabaikan/dikecualikan oleh Git (didefinisikan dalam ".gitignore").
> Informasi lebih lanjut: <https://git-scm.com/docs/git-check-ignore>.

- Cek apakah suatu file atau direktori telah diabaikan:

`git check-ignore {{jalan/menuju/file_atau_direktori}}`

- Cek apakah lebih dari satu file atau direktori telah diabaikan:

`git check-ignore {{jalan/menuju/file_atau_direktori1 jalan/menuju/file_atau_direktori2 ...}}`

- Cek pengecualian file dan direktori menggunakan daftar yang didefinisikan dalam `stdin`:

`git check-ignore --stdin < {{jalan/menuju/file_daftar}}`

- Jangan cek index Git (biasanya dipakai untuk mengetahui mengapa terdapat jalur yang tetap dilacak Git dan tak diabaikan):

`git check-ignore --no-index {{jalan/menuju/file_atau_direktori1 jalan/menuju/file_atau_direktori2 ...}}`

- Tampilkan informasi pola pengecualian `.gitignore` yang dipakai untuk mengecualikan setiap jalur:

`git check-ignore --verbose {{jalan/menuju/file_atau_direktori1 jalan/menuju/file_atau_direktori2 ...}}`
