# aa-complain

> Atur kebijakan AppArmor ke mode _complain_.
> Lihat juga: `aa-disable`, `aa-enforce`, `aa-status`.
> Informasi lebih lanjut: <https://gitlab.com/apparmor/apparmor/-/wikis/manpage_aa-complain.8>.

- Atur kebijakan ke mode _complain_:

`sudo aa-complain {{path/ke/profil1 path/ke/profil2 ...}}`

- Atur kebijakan ke mode _complain_ (menentukan direktori profil):

`sudo aa-complain {{[-d|--dir]}} {{path/ke/profil}}`
