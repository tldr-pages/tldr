# git ls-tree

> Muestra los contenidos de un objeto árbol.
> Más información: <https://git-scm.com/docs/git-ls-tree>.

- Muestra el contenido del árbol en una rama:

`git ls-tree {{nombre_de_la_rama}}`

- Muestra el contenido del árbol en una confirmación (recursivo en subárboles):

`git ls-tree -r {{hash_de_la_confirmación}}`

- Muestra solo los nombres de archivos del árbol en una confirmación:

`git ls-tree --name-only {{hash_de_la_confirmación}}`
