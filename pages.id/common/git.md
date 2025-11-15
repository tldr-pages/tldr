# git

> Sistem kontrol versi terdistribusi.
> Beberapa subperintah seperti `commit`, `add`, `branch`, `checkout`, `push`, dsb. mempunyai dokumentasi terpisah.
> Informasi lebih lanjut: <https://git-scm.com/docs/git>.

- Jalankan suatu subperintah Git:

`git {{subperintah}}`

- Jalankan suatu subperintah terhadap suatu direktori repositori:

`git -C {{jalan/menuju/repo}} {{subperintah}}`

- Jalankan suatu subperintah dengan set konfigurasi/pengaturan tertentu:

`git -c '{{kunci.config}}={{nilai}}' {{subperintah}}`

- Tampilkan bantuan umum:

`git --help`

- Tampilkan bantuan pada subperintah Git (seperti `clone`,` add`, `push`, `log`, dll.):

`git help {{subcommand}}`

- Periksa versi Git:

`git --version`
