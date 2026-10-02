# aa-enforce

> Imposta un profilo AppArmor in modalità enforce.
> Vedi anche: `aa-complain`, `aa-disable`, `aa-status`.
> Maggiori informazioni: <https://gitlab.com/apparmor/apparmor/-/wikis/manpage_aa-enforce.8>.

- Abilita un profilo:

`sudo aa-enforce {{[-d|--dir]}} {{path/to/profile}}`

- Abilita più profili:

`sudo aa-enforce {{path/to/profile1 path/to/profile2 ...}}`
