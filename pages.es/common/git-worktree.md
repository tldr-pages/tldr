# git worktree

> Gestiona múltiples árboles de trabajo adjuntos al mismo repositorio.
> Más información: <https://git-scm.com/docs/git-worktree>.

- Crea un nuevo directorio con la rama específicada y se cambia a él:

`git worktree add {{ruta/al/directorio}} {{rama}}`

- Crea un nuevo directorio con un nueva rama y se cambia a él:

`git worktree add {{ruta/al/directorio}} -b {{rama_nueva}}`

- Muestra todos los directorios de trabajo adjuntos a este repositorio:

`git worktree list`

- Elimina un árbol de trabajo (después de eliminar el directorio del árbol de trabajo):

`git worktree prune`
