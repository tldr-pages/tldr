# git remote

> Mengelola kumpulan repositori yang dilacak/diikuti ("remotes").
> Informasi lebih lanjut: <https://git-scm.com/docs/git-remote>.

- Menampilkan daftar remote, namanya dan URL:

`git remote -v`

- Menampilkan informasi tentang remote:

`git remote show {{nama_remote}}`

- Menambahkan remote:

`git remote add {{nama_remote}} {{url_remote}}`

- Mengubah URL dari remote (gunakan `--add` untuk tetap menyimpan URL lama):

`git remote set-url {{nama_remote}} {{url_baru}}`

- Menghapus remote:

`git remote remove {{nama_remote}}`

- Mengubah nama remote:

`git remote rename {{nama_lama}} {{nama_baru}}`
