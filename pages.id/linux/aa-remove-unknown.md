# aa-remove-unknown

> Hapus profil AppArmor yang sudah tidak ada di direktori konfigurasi.
> Informasi lebih lanjut: <https://gitlab.com/apparmor/apparmor/-/wikis/manpage_aa-remove-unknown.8>.

- Lakukan dry run untuk melihat profil mana yang akan dihapus:

`sudo aa-remove-unknown -n`

- Hapus profil tersebut:

`sudo aa-remove-unknown`

- Tampilkan bantuan:

`aa-remove-unknown {{[-h|--help]}}`
