# git checkout

> Periksa isi (checkout) cabang atau alamat ke direktori kerja.
> Informasi lebih lanjut: <https://git-scm.com/docs/git-checkout>.

- Buat cabang baru, kemudian lihat isinya:

`git checkout -b {{nama_cabang}}`

- Buat ke cabang baru berdasarkan referensi tertentu (misal cabang, remote, cabang remote, dan tag), kemudian lihat isinya:

`git checkout -b {{nama_cabang}} {{referensi}}`

- Lihat isi suatu cabang lokal:

`git checkout {{nama_cabang}}`

- Lihat kembali cabang yang terakhir kali dilihat sebelum cabang saat ini:

`git checkout -`

- Lihat isi cabang yang bersumber dari sumber jauh (remote):

`git checkout --track {{nama_remote}}/{{nama_cabang}}`

- Singkirkan semua perubahan yang tidak masuk status stage pada direktori saat ini (lihat `git reset` untuk perintah yang lebih mirip undo):

`git checkout .`

- Singkirkan perubahan yang tidak masuk status stage pada berkas:

`git checkout {{nama_berkas}}`

- Ganti berkas pada direktori saat ini dengan versi pada cabang lain:

`git checkout {{nama_cabang}} -- {{nama_berkas}}`
