# git

> Sistem kontrol versi terdistribusi.
> Kami mempunyai dokumentasi terpisah untuk menggunakan subperintah seperti `git commit`.
> Informasi lebih lanjut: <https://git-scm.com/>.

- Memeriksa versi Git:

`git --version`

- Menunjukkan bantuan umum:

`git --help`

- Menampilkan bantuan pada sub perintah Git (seperti `commit`,` log`, dll.):

`git help {{subcommand}}`

- Menjalankan subperintah Git:

`git {{subcommand}}`

- Menjalankan subperintah Git di jalur root repositori kustom:

`git -C {{alamat/ke/repositori}} {{subcommand}}`

- Menjalankan subperintah Git dengan set konfigurasi yang diberikan:

`git -c '{{config.key}}={{value}}' {{subcommand}}`
