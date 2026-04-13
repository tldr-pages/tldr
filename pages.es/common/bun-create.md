# bun create

> Crea un nuevo proyecto a partir de una plantilla.
> Nota: Se puede utilizar `c` como alias de `create`.
> Más información: <https://bun.com/docs/runtime/templating/create>.

- Crea un nuevo proyecto a partir de una plantilla oficial de forma interactiva:

`bun create {{plantilla}}`

- Crea un nuevo proyecto a partir de una plantilla oficial en un nuevo directorio:

`bun create {{plantilla}} {{ruta/al/destino}}`

- Crea un nuevo proyecto a partir de una plantilla de un repositorio de GitHub:

`bun create {{https://github.com/username/repo}} {{ruta/al/destino}}`

- Crea un nuevo proyecto a partir de una plantilla local:

`bun create {{ruta/a/plantilla}} {{ruta/al/destino}}`

- Crea un nuevo proyecto, sobrescribiendo el directorio de destino si ya existe:

`bun create {{plantilla}} {{ruta/al/destino}} --force`

- Crea un nuevo proyecto sin inicializar automáticamente un repositorio de Git:

`bun create {{plantilla}} {{ruta/al/destino}} --no-git`

- Crea un nuevo proyecto sin instalar automáticamente las dependencias:

`bun create {{plantilla}} {{ruta/al/destino}} --no-install`
