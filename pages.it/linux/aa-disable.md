# aa-disable

> Disabilita le policy di sicurezza AppArmor.
> Vedi anche: `aa-complain`, `aa-enforce`, `aa-status`.
> Maggiori informazioni: <https://gitlab.com/apparmor/apparmor/-/wikis/manpage_aa-disable.8>.

- Disabilita un profilo:

`sudo aa-disable {{path/to/profile1 path/to/profile2 ...}}`

- Disabilita i profili in una directory (predefinita: `/etc/apparmor.d`):

`sudo aa-disable --dir {{path/to/profiles}}`
