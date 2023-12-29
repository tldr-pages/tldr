# git checkout

> Lihat isi cabang atau alamat ke dalam direktori kerja.
> Informasi lebih lanjut: <https://git-scm.com/docs/git-checkout>.

- Buat dan lihat isi cabang baru:

`git checkout -b {{nama_cabang}}`

- Buat dan lihat isi cabang baru berdasarkan referensi tertentu (misal cabang, remote, cabang remote, dan tag):

`git checkout -b {{nama_cabang}} {{referense}}`

- Alih dan lihat isi cabang lokal yang ada:

`git checkout {{nama_cabang}}`

- Alih dan lihat isi cabang yang sebelumnya di checkout:

`git checkout -`

- Alih dan lihat isi cabang remote yang ada:

`git checkout --track {{nama_remote}}/{{nama_cabang}}`

- Singkirkan semua perubahan yang tidak masuk status stage pada direktori saat ini (lihat `git reset` untuk perintah yang lebih mirip undo):

`git checkout .`

- Singkirkan perubahan yang tidak masuk status stage pada berkas:

`git checkout {{nama_berkas}}`

- Ubah berkas pada direktori saat ini dengan versi pada cabang lain:

`git checkout {{nama_cabang}} -- {{nama_berkas}}`
