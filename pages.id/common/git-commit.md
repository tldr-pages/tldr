# git commit

> Komit file ke dalam sebuah repositori.
> Informasi lebih lanjut: <https://git-scm.com/docs/git-commit>.

- Komit file bertahap ke repositori dengan sebuah pesan:

`git commit --message "{{pesan}}"`

- Komit file bertahap dengan pesan yang disimpan dalam suatu file:

`git commit --file {{jalan/menuju/file_pesan_komit}}`

- Ubah secara otomatis semua file yang dimodifikasi menjadi ke status stage dan menambahkan sebuah pesan:

`git commit --all --message "{{pesan}}"`

- Komit file bertahap kemudian tandatangani komit tersebut menggunakan kunci GPG (atau kunci yang didefinisikan dalam file konfigurasi jika tidak didefinisikan):

`git commit --gpg-sign {{id_kunci_gpg}} --message "{{pesan}}"`

- Ganti komit terakhir dengan perubahan yang ada di status stage saat ini:

`git commit --amend`

- Komit file tertentu (yang sudah di status stage):

`git commit {{alamat/ke/file1}} {{alamat/ke/file2}}`

- Buat komit kosong, tanpa file bertahap:

`git commit --message "{{pesan}}" --allow-empty`
