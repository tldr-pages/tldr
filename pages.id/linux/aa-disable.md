# aa-disable

> Nonaktifkan kebijakan keamanan AppArmor.
> Lihat juga: `aa-complain`, `aa-enforce`, `aa-status`.
> Informasi lebih lanjut: <https://gitlab.com/apparmor/apparmor/-/wikis/manpage_aa-disable.8>.

- Nonaktifkan profil:

`sudo aa-disable {{path/ke/profil1 path/ke/profil2 ...}}`

- Nonaktifkan profil dalam direktori (default ke `/etc/apparmor.d`):

`sudo aa-disable --dir {{path/ke/profil}}`
