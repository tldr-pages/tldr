# aa-cleanprof

> Limpia perfiles de seguridad de AppArmor eliminando reglas sin utilizar.
> Más información: <https://gitlab.com/apparmor/apparmor/-/wikis/manpage_aa-cleanprof.8>.

- Limpia un usuario:

`sudo aa-cleanprof {{nombre_perfil}}`

- Limpia múltiples perfiles al mismo tiempo:

`sudo aa-cleanprof {{perfil1 perfil2 ...}}`

- Limpia un perfil desde un directorío específico:

`sudo aa-cleanprof {{[-d|--dir]}} {{/ruta/a/perfiles}} {{nombre_perfil}}`

- Ejecuta silenciosamente sin indicaciones:

`sudo aa-cleanprof {{[-s|--silent]}} {{nombre_perfil}}`

- Prevén la recarga del perfil tras limpiarlo:

`sudo aa-cleanprof --no-reload {{nombre_perfil}}`

- Muestra la ayuda:

`aa-cleanprof {{[-h|--help]}}`
