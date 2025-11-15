# git cat-file

> Dapatkan informasi konten atau jenis dan ukuran untuk objek repositori Git.
> Informasi lebih lanjut: <https://git-scm.com/docs/git-cat-file>.

- Dapatkan ukuran ([s]ize) untuk komit terkini (HEAD), dalam hitungan bita/byte:

`git cat-file -s HEAD`

- Dapatkan [t]ipe yang direferensikan dalam suatu objek Git (seperti blob, tree, komit, atau tag):

`git cat-file -t {{8c442dc3}}`

- Cetak isi objek Git yang diberikan berdasarkan jenisnya, dalam format yang mudah dibaca manusia:

`git cat-file -p {{HEAD~2}}`
