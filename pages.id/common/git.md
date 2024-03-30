# git

> Sistem kontrol versi terdistribusi.
> Kami mempunyai dokumentasi terpisah untuk menggunakan subperintah seperti `commit`, `add`, `branch`, `checkout`, `push`, dsb.
> Informasi lebih lanjut: <https://git-scm.com/>.

- Periksa versi Git:

`git --version`

- Tampilkan bantuan umum:

`git --help`

- Tampilkan bantuan pada sub perintah Git (seperti `commit`,` log`, dll.):

`git help {{subcommand}}`

- Jalankan subperintah Git:

`git {{subcommand}}`

- Jalankan subperintah Git di jalur root repositori kustom:

`git -C {{alamat/ke/repositori}} {{subcommand}}`

- Jalankan subperintah Git dengan set konfigurasi yang diberikan:

`git -c '{{config.key}}={{value}}' {{subcommand}}`
