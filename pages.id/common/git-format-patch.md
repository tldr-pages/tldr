# git format-patch

> Buat berkas-berkas .patch dari kumpulan komit Git. Dapat dipakai untuk mengirimkan perubahan/komit melalui surel/email.
> Lihat juga `git am`, yang memungkinkan pengguna untuk melakukan perubahan melalui berkas komit .patch yang dibuat.
> Informasi lebih lanjut: <https://git-scm.com/docs/git-format-patch>.

- Buat suatu berkas `.patch` untuk mencatat seluruh komit yang belum dikirimkan (push) ke remote, menggunakan nama berkas otomatis:

`git format-patch {{origin}}`

- Tampilkan isi berkas `.patch` menuju `stdout` yang mengandung perubahan antara dua revisi/komit:

`git format-patch {{revisi_1}}..{{revisi_2}}`

- Tulis suatu berkas `.patch` yang mengandung segala perubahan dalam 3 komit terakhir:

`git format-patch -{{3}}`
