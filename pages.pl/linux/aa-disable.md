# aa-disable

> Wyłącz polityki bezpieczeństwa AppArmor.
> Zobacz także: `aa-complain`, `aa-enforce`, `aa-status`.
> Więcej informacji: <https://gitlab.com/apparmor/apparmor/-/wikis/manpage_aa-disable.8>.

- Wyłącz profile:

`sudo aa-disable {{ścieżka/do/profilu1 ścieżka/do/profilu2 ...}}`

- Wyłącz profile w katalogu (domyślnie `/etc/apparmor.d`):

`sudo aa-disable --dir {{ścieżka/do/profili}}`
