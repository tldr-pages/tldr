# git reset

> Deshace commits o desmarca cambios mediante el reseteo del actual HEAD de git al estado especificado.
> Si se pasa una ruta, funciona como "desmarcar", si se pasa el hash de un commit o una rama, funciona como "deshacer" el commit.
> Más información: <https://git-scm.com/docs/git-reset>.

- Desmarcar todo:

`git reset`

- Desmarcar un archivo o archivos específicos:

`git reset {{ruta/al/archivo_o_archivos}}`

- Desmarca partes de un archivo:

`git reset -p {{ruta/al/archivo}}`

- Deshace el último commit, manteniendo sus cambios,y cualquier otro cambios sin commit,en el sistema de archivo:

`git reset HEAD~`

- Deshace los últimos dos commits al añadir sus cambios al índice (por ej., marcado para commit):

`git reset --soft HEAD~2`

- Descartar cualquier cambio sin commit, marcado o no (se puede `git checkout` solo para los cambios sin marcar):

`git reset --hard`

- Resetea el repositorio a un commit específico y descarta a partir de este los cambios con y sin commit, y los marcados:

`git reset --hard {{commit}}`
