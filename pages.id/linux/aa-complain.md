# aa-complain

> Atur kebijakan AppArmor ke mode complain.
> Lihat juga: `aa-disable`, `aa-enforce`, `aa-status`.
> Informasi lebih lanjut: <https://gitlab.com/apparmor/apparmor/-/wikis/manpage_aa-complain.8>.

- Atur kebijakan ke mode complain:

`sudo aa-complain {{path/ke/profil1 path/ke/profil2 ...}}`

- Atur kebijakan ke mode complain (menentukan direktori profil):

`sudo aa-complain {{[-d|--dir]}} {{path/ke/profil}}`
