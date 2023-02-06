# git cat-file

> Tartalom- vagy típus- és méretadatok megadása a Git tároló objektumokhoz. További információ: <https://git-scm.com/docs/git-cat-file>.

- A HEAD commit \[s\]ize bájtokban kifejezve:

`git cat-file -s HEAD`

- Egy adott Git objektum \[t\]ype (blob, fa, commit, tag) típusának lekérdezése:

`git cat-file -t {{8c442dc3}}`

- Pretty-\[p\]rint egy adott Git objektum tartalmának a típusa alapján:

`git cat-file -p {{HEAD~2}}`
