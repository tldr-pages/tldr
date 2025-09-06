# git status

> Tampilkan perubahan pada berkas dalam repositori Git.
> Menampilkan daftar perubahan, menambahkan dan menghapus berkas dibandingkan dengan komit yang saat ini diperiksa (checkout).
> Informasi lebih lanjut: <https://git-scm.com/docs/git-status>.

- Tampilkan daftar berkas yang diubah yang belum ditambahkan untuk komit:

`git status`

- Tampilkan informasi dalam format singkat:

`git status {{[-s|--short]}}`

- Tampilkan informasi secara terperinci baik dalam panggung rencana perubahan (staging) dan direktori kerja saat ini:

`git status {{[-vv|--verbose --verbose]}}`

- Tampilkan informasi mengenai cabang ([b]ranch) dan status pelacakan dari remote:

`git status {{[-b|--branch]}}`

- Tampilkan daftar berkas beserta informasi cabang dalam format:

`git status {{[-sb|--short --branch]}}`

- Tampilkan jumlah entri yang disimpan ke dalam kumpulan stash:

`git status --show-stash`

- Jangan tampilkan berkas yang tidak terlacak:

`git status {{[-uno|--untracked-files=no]}}`
