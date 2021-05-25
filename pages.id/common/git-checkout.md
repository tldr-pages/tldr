# git checkout

> Checkout cabang atau alamat ke direktori kerja.
> Informasi lebih lanjut: <https://git-scm.com/docs/git-checkout>.

- Membuat dan beralih ke cabang baru:

`git checkout -b {{nama_cabang}}`

- Membuat dan beralih ke cabang baru berdasarkan referensi tertentu (misal cabang, remote, cabang remote, dan tag):

`git checkout -b {{nama_cabang}} {{referense}}`

- Beralih ke cabang lokal yang ada:

`git checkout {{nama_cabang}}`

- Beralih ke cabang yang sebelumnya di checkout:

`git checkout -`

- Beralih ke cabang remote yang ada:

`git checkout --track {{nama_remote}}/{{nama_cabang}}`

- Menyingkirkan semua perubahan yang tidak masuk status stage pada direktori saat ini (lihat `git reset` untuk perintah yang lebih mirip undo):

`git checkout .`

- Menyingkirkan perubahan yang tidak masuk status stage pada berkas:

`git checkout {{nama_berkas}}`

- Mengganti berkas pada direktori saat ini dengan versi pada cabang lain:

`git checkout {{nama_cabang}} -- {{nama_berkas}}`
