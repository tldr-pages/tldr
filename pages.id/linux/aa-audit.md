# aa-audit

> Atur profil keamanan AppArmor ke mode audit.
> Informasi lebih lanjut: <https://gitlab.com/apparmor/apparmor/-/wikis/manpage_aa-audit.8>.

- Atur profil ke mode audit:

`sudo aa-audit {{profile_name}}`

- Atur beberapa profil ke mode audit:

`sudo aa-audit {{profile1 profile2 ...}}`

- Atur profil ke mode audit dari direktori tertentu:

`sudo aa-audit {{[-d|--dir]}} /{{path/ke/profil}} {{profile_name}}`

- Paksa mode audit meskipun sudah diterapkan:

`sudo aa-audit --force {{profile_name}}`

- Atur profil ke mode audit tanpa memuat ulang (reload):

`sudo aa-audit --no-reload {{profile_name}}`

- Hapus mode audit untuk sebuah profil:

`sudo aa-audit {{[-r|--remove]}} {{profile_name}}`

- Tampilkan bantuan:

`aa-audit {{[-h|--help]}}`
