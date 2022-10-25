# git rev-parse

> Muestra metadatos relativos a revisiones específicas.
> Más información: <https://git-scm.com/docs/git-rev-parse>.

- Obtiene el hash del commit de una rama:

`git rev-parse {{nombre_de_la_rama}}`

- Obtiene el nombre de la rama actual:

`git rev-parse --abbrev-ref {{HEAD}}`

- Obtiene la ruta absoluta al directorio raíz:

`git rev-parse --show-toplevel`
