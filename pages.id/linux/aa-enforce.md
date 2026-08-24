# aa-enforce

> Atur profil AppArmor ke mode enforce.
> Lihat juga: `aa-complain`, `aa-disable`, `aa-status`.
> Informasi lebih lanjut: <https://gitlab.com/apparmor/apparmor/-/wikis/manpage_aa-enforce.8>.

- Aktifkan profil:

`sudo aa-enforce {{[-d|--dir]}} {{path/ke/profil}}`

- Aktifkan beberapa profil:

`sudo aa-enforce {{path/ke/profil1 path/ke/profil2 ...}}`
