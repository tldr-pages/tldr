# git commit

> Komit file ke dalam sebuah repositori.
> Informasi lebih lanjut: <https://git-scm.com/docs/git-commit>.

- Komit file bertahap ke repositori dengan sebuah pesan:

`git commit -m {{pesan}}`

- Otomatis merubah semua file yang dimodifikasi menjadi ke status stage dan menambahkan sebuah pesan:

`git commit -a -m {{pesan}}`

- Ganti komit terakhir dengan perubahan yang ada di status stage saat ini:

`git commit --amend`

- Komit file tertentu (yang sudah di status stage):

`git commit {{alamat/ke/file/saya1}} {{alamat/ke/file/saya2}}`
