# git commit

> Komit berkas ke dalam sebuah repositori.
> Informasi lebih lanjut: <https://git-scm.com/docs/git-commit>.

- Komit berkas bertahap ke repositori dengan sebuah pesan:

`git commit --message "{{pesan}}"`

- Komit berkas bertahap dengan pesan yang disimpan dalam suatu berkas:

`git commit --file {{jalan/menuju/berkas_pesan_komit}}`

- Ubah secara otomatis semua berkas yang dimodifikasi menjadi ke status stage dan menambahkan sebuah pesan:

`git commit --all --message "{{pesan}}"`

- Komit berkas bertahap kemudian tandatangani komit tersebut menggunakan kunci GPG (atau kunci yang didefinisikan dalam berkas konfigurasi jika tidak didefinisikan):

`git commit --gpg-sign {{id_kunci_gpg}} --message "{{pesan}}"`

- Ganti komit terakhir dengan perubahan yang ada di status stage saat ini:

`git commit --amend`

- Komit berkas tertentu (yang sudah di status stage):

`git commit {{jalan/menuju/berkas1 jalan/menuju/berkas2 ...}}`

- Buat komit kosong, tanpa berkas bertahap:

`git commit --message "{{pesan}}" --allow-empty`
