# git ls-tree

> Muestra los contenidos de un objeto árbol.
> Más información: <https://git-scm.com/docs/git-ls-tree>.

- Lista el contenido del árbol en una rama:

`git ls-tree {{nombre_de_la_rama}}`

- Lista el contenido del árbol en una confirmación (recursivo en subárboles):

`git ls-tree -r {{hash_de_la_confirmación}}`

- Lista solo los nombres de archivos del árbol en una confirmación:

`git ls-tree --name-only {{hash_de_la_confirmación}}`

- Lista el nombre de los archivos en la rama actual en forma de árbol (Nota: la opción `--fromfile` no está disponible en el comando `tree` de Windows):

`git ls-tree -r --name-only HEAD | tree --fromfile`
