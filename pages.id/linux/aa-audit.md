# aa-audit

> Mengatur profil keamanan AppArmor ke mode audit.
> Informasi selengkapnya: <https://gitlab.com/apparmor/apparmor/-/wikis/manpage_aa-audit.8>.

- Atur satu profil ke mode audit:

`sudo aa-audit {{nama_profil}}`

- Atur beberapa profil ke mode audit:

`sudo aa-audit {{profil1 profil2 ...}}`

- Atur profil ke mode audit dari direktori tertentu:

`sudo aa-audit {{[-d|--dir]}} {{/path/to/profiles}} {{nama_profil}}`

- Paksa mode audit meski sudah diterapkan:

`sudo aa-audit --force {{nama_profil}}`

- Atur profil ke mode audit tanpa memuat ulang (reload):

`sudo aa-audit --no-reload {{nama_profil}}`

- Hapus mode audit untuk sebuah profil:

`sudo aa-audit {{[-r|--remove]}} {{nama_profil}}`

- Tampilkan bantuan:

`aa-audit {{[-h|--help]}}`
