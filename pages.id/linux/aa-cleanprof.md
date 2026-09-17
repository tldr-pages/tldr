# aa-cleanprof

> Bersihkan profil keamanan AppArmor dengan menghapus aturan yang tidak digunakan.
> Informasi lebih lanjut: <https://gitlab.com/apparmor/apparmor/-/wikis/manpage_aa-cleanprof.8>.

- Bersihkan profil untuk menghapus aturan yang tidak digunakan:

`sudo aa-cleanprof {{profile_name}}`

- Bersihkan beberapa profil sekaligus:

`sudo aa-cleanprof {{profile1 profile2 ...}}`

- Tentukan direktori yang berisi profil:

`sudo aa-cleanprof {{[-d|--dir]}} /{{path/ke/profil}} {{profile_name}}`

- Jalankan secara senyap tanpa prompt:

`sudo aa-cleanprof {{[-s|--silent]}} {{profile_name}}`

- Cegah muat ulang profil setelah pembersihan:

`sudo aa-cleanprof --no-reload {{profile_name}}`

- Tampilkan bantuan:

`aa-cleanprof {{[-h|--help]}}`
