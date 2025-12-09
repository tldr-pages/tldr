# git rev-parse

> Muestra metadatos relativos a revisiones específicas.
> Más información: <https://git-scm.com/docs/git-rev-parse>.

- Obtén el hash de la confirmación de una rama:

`git rev-parse {{nombre_de_la_rama}}`

- Obtén el nombre de la rama actual:

`git rev-parse --abbrev-ref {{HEAD}}`

- Obtén la ruta absoluta al directorio raíz:

`git rev-parse --show-toplevel`
