# git restore

> Restaura los archivos del árbol de trabajo. Requiere la version 2.23+ de Git.
> Vea también `git checkout` y `git reset`.
> Más información: <https://git-scm.com/docs/git-restore>.

- Restaura un archivo sin marcar a la versión de la confirmación actual (HEAD):

`git restore {{ruta/al/archivo}}`

- Restaura un archivo sin marcar a la versión de una confirmación específica:

`git restore --source {{confirmación}} {{ruta/al/archivo}}`

- Descarta los cambios sin confirmación para los archivos rastreados:

`git restore :/`

- Desmarca un archivo:

`git restore --staged {{ruta/al/archivo}}`

- Desmarca todos los archivos:

`git restore --staged :/`

- Descarta todos los cambios de los archivos, marcados o no:

`git restore --worktree --staged :/`

- Selecciona interactivamente secciones de archivos para restaurar:

`git restore --patch`
