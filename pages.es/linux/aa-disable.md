# aa-disable

> Deshabilita las políticas de seguridad de AppArmor.
> Vea también: `aa-complain`, `aa-enforce`, `aa-status`.
> Más información: <https://gitlab.com/apparmor/apparmor/-/wikis/manpage_aa-disable.8>.

- Deshabilita perfil:

`sudo aa-disable {{ruta/a/perfil1 ruta/a/perfil2 ...}}`

- Deshabilita perfiles (predeterminado a `/etc/apparmor.d`):

`sudo aa-disable --dir {{ruta/a/perfiles}}`
