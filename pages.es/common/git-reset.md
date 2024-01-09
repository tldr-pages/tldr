# git reset

> Deshaz confirmaciones o desmarca cambios mediante el restablecimiento del actual HEAD de Git al estado especificado.
> Si se pasa una ruta, funciona como "desmarcar", si se pasa el hash de una confirmación o una rama, funciona como "deshacer" la confirmación.
> Más información: <https://git-scm.com/docs/git-reset>.

- Desmarca todo:

`git reset`

- Desmarca un archivo o archivos específicos:

`git reset {{ruta/al/archivo_o_archivos}}`

- Interactivamente desmarca partes de un archivo:

`git reset --patch {{ruta/al/archivo}}`

- Deshaz la última confirmación, manteniendo sus cambios, y cualquier otro cambio sin confirmación, en el sistema de archivos:

`git reset HEAD~`

- Deshaz las últimas dos confirmaciones al añadir sus cambios al índice (p. ej. marcado para confirmación):

`git reset --soft HEAD~2`

- Descarta cualquier cambio sin confirmación, marcado o no (se puede `git checkout` solo para los cambios sin marcar):

`git reset --hard`

- Restablece el repositorio a una confirmación específica y descarta a partir de esta los cambios con y sin confirmación, y los marcados:

`git reset --hard {{confirmación}}`
