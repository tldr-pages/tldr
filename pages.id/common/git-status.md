# git status

> Tampilkan perubahan pada berkas dalam repositori Git.
> Menampilkan daftar perubahan, menambahkan dan menghapus berkas dibandingkan dengan komit yang saat ini diperiksa (checkout).
> Informasi lebih lanjut: <https://git-scm.com/docs/git-status>.

- Tampilkan daftar berkas yang diubah yang belum ditambahkan untuk komit:

`git status`

- Tampilkan informasi dalam format [s]ingkat:

`git status --short`

- Tampilkan informasi secara terperinci ([v]erbose) baik dalam panggung rencana perubahan (staging) dan direktori kerja saat ini:

`git status --verbose --verbose`

- Tampilkan informasi mengenai cabang ([b]ranch) dan status pelacakan dari remote:

`git status --branch`

- Tampilkan daftar berkas beserta informasi cabang ([b]ranch) dalam format [s]ingkat:

`git status --short --branch`

- Tampilkan jumlah entri yang disimpan ke dalam kumpulan stash:

`git status --show-stash`

- Jangan tampilkan berkas yang tidak terlacak:

`git status --untracked-files=no`
