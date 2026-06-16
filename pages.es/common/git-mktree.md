# git mktree

> Construye un objeto árbol usando texto formateado `ls-tree`.
> Más información: <https://git-scm.com/docs/git-mktree>.

- Construye un objeto árbol y verifica que el hash de cada entrada del árbol identifica un objeto existente:

`git mktree`

- Permite que falten objetos:

`git mktree --missing`

- Lee la salida terminada en NUL (carácter cero) del objeto árbol (`ls-tree -z`):

`git mktree -z`

- Permite la creación de múltiples objetos árbol:

`git mktree --batch`

- Ordena y construye un árbol a partir de `stdin` (se requiere un formato de salida de `git ls-tree` no recursivo):

`git < {{ruta/a/árbol.txt}} mktree`
