# git add

> Tambahkan berkas yang diubah ke dalam indeks.
> Informasi lebih lanjut: <https://git-scm.com/docs/git-add>.

- Tambahkan berkas ke dalam indeks:

`git add {{jalan/menuju/berkas}}`

- Tambahkan seluruh berkas (baik yang terlacak maupun tidak terlacak):

`git add {{[-A|--all]}}`

- Tambahkan seluruh berkas pada folder saat ini:

`git add .`

- Hanya tambahkan berkas yang sudah terlacak:

`git add {{[-u|--update]}}`

- Tambahkan juga berkas yang diabaikan:

`git add {{[-f|--force]}}`

- Tambahkan berkas ke status stage secara interaktif:

`git add {{[-p|--patch]}}`

- Tambahkan berkas tertentu ke status stage secara interaktif:

`git add {{[-p|--patch]}} {{jalan/menuju/berkas}}`

- Stage berkas secara interaktif:

`git add {{[-i|--interactive]}}`
