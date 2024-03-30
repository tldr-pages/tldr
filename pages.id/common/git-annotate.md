# git annotate

> Tampilkan kode hash serta pelaku komit terakhir pada setiap baris suatu file teks.
> Lihat juga `git blame`, yang lebih disarankan daripada `git annotate`.
> Perintah `git annotate` disediakan bagi pengguna yang telah familiar pada sistem manajemen versi lainnya.
> Informasi lebih lanjut: <https://git-scm.com/docs/git-annotate>.

- Tampilkan file teks beserta informasi nama pelaku dan kode hash komit terakhir pada akhir setiap baris teks:

`git annotate {{jalan/menuju/file}}`

- Tampilkan file dengan informasi komit menggunakan alamat surel/[e]mail daripada nama pelaku:

`git annotate -e {{jalan/menuju/file}}`

- Tampilkan hanya baris-baris teks yang memenuhi kriteria ekspresi reguler:

`git annotate -L :{{ekspresi_reguler}} {{jalan/menuju/file}}`
