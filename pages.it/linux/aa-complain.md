# aa-complain

> Imposta una policy di AppArmor in modalità complain.
> Vedi anche: `aa-disable`, `aa-enforce`, `aa-status`.
> Maggiori informazioni: <https://gitlab.com/apparmor/apparmor/-/wikis/manpage_aa-complain.8>.

- Imposta una policy in modalità complain:

`sudo aa-complain {{path/to/profile1 path/to/profile2 ...}}`

- Imposta più policy in modalità complain:

`sudo aa-complain {{[-d|--dir]}} {{path/to/profiles}}`
