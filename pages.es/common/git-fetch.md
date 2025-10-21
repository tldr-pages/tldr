# git fetch

> Descarga objetos y referencias de un repositorio remoto.
> Más información: <https://git-scm.com/docs/git-fetch>.

- Recibe los últimos cambios del repositorio remoto upstream por defecto (si se ha establecido):

`git fetch`

- Recibe las ramas nuevas de un repositorio remoto upstream específico:

`git fetch {{remote_name}}`

- Recibe los últimos cambios de todos los repositorios remotos upstream:

`git fetch --all`

- Recibe también las etiquetas de un repositorio upstream:

`git fetch {{[-t|--tags]}}`

- Elimina las referencias locales a ramas remotas que han sido eliminadas de upstream:

`git fetch {{[-p|--prune]}}`

- Ahonda la rama superficial actual en 2 commits:

`git fetch --deepen 2`
