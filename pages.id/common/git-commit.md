# git commit

> Komit file ke dalam sebuah repositori.
> Informasi selengkapnya: <https://git-scm.com/docs/git-commit>.

- Komit file bertahap ke repositori dengan sebuah pesan:

`git commit -m {{message}}`

- otomatis merubah semua file yang dimodifikasi menjadi ke status stage dan menambahkan sebuah pesan:

`git commit -a -m {{message}}`

- Ganti komit terakhir dengan perubahan yang ada di status stage saat ini:

`git commit --amend`

- komit file tertentu (yang sudah di status stage):

`git commit {{path/to/my/file1}} {{path/to/my/file2}}`
