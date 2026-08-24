# aa-unconfined

> Tampilkan daftar proses dengan port TCP/UDP terbuka yang tidak memiliki profil AppArmor yang dimuat.
> Informasi lebih lanjut: <https://gitlab.com/apparmor/apparmor/-/wikis/manpage_aa-unconfined.8>.

- Tampilkan daftar proses yang tidak dibatasi (_unconfined_) menggunakan perintah `ss` (default):

`sudo aa-unconfined`

- Gunakan `netstat` alih-alih `ss` untuk mendeteksi soket jaringan yang terbuka:

`sudo aa-unconfined --with-netstat`

- Tampilkan semua proses dari `/proc` dengan port TCP/UDP dan tanpa profil AppArmor (lebih terperinci):

`sudo aa-unconfined --paranoid`

- Tampilkan bantuan:

`aa-unconfined {{[-h|--help]}}`
