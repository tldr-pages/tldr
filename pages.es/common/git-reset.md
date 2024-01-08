# git reset

> Deshace commits o desmarca cambios mediante el restablecimiento del actual HEAD de Git al estado especificado.
> Si se pasa una ruta, funciona como "desmarcar", si se pasa el hash de un commit o una rama, funciona como "deshacer" el commit.
> Más información: <https://git-scm.com/docs/git-reset>.

- Desmarca todo:

`git reset`

- Desmarca un archivo o archivos específicos:

`git reset {{ruta/al/archivo_o_archivos}}`

- Interactivamente desmarca partes de un archivo:

`git reset --patch {{ruta/al/archivo}}`

- Deshaz el último commit, manteniendo sus cambios, y cualquier otro cambio sin commit, en el sistema de archivo:

`git reset HEAD~`

- Deshaz los últimos dos commits al añadir sus cambios al índice (por ej., marcado para commit):

`git reset --soft HEAD~2`

- Descarta cualquier cambio sin commit, marcado o no (se puede `git checkout` solo para los cambios sin marcar):

`git reset --hard`

- Restablece el repositorio a un commit específico y descarta a partir de este los cambios con y sin commit, y los marcados:

`git reset --hard {{commit}}`
