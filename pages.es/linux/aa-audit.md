# aa-audit

> Establece perfiles de seguridad de AppArmor en modo de auditoría.
> Más información: <https://gitlab.com/apparmor/apparmor/-/wikis/manpage_aa-audit.8>.

- Establece un perfil en modo auditoría:

`sudo aa-audit {{nombre_perfil}}`

- Establece múltiples perfiles en modo auditoría:

`sudo aa-audit {{perfil1 perfil2 ...}}`

- Establece un perfil en modo auditoría desde un directorío específico:

`sudo aa-audit {{[-d|--dir]}} {{/ruta/a/perfiles}} {{nombre_perfil}}`

- Fuerza modo auditoría incluso si ya ha sido aplicado:

`sudo aa-audit --force {{nombre_perfil}}`

- Establece un perfil en modo auditoría sin recargarlo:

`sudo aa-audit --no-reload {{nombre_perfil}}`

- Elimina el modo auditoría de un perfil:

`sudo aa-audit {{[-r|--remove]}} {{nombre_perfil}}`

- Muestra la ayuda:

`aa-audit {{[-h|--help]}}`
