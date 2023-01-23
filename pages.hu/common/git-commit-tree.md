# git commit-tree

> Alacsony szintű segédprogram commit objektumok létrehozásához. Lásd még: `git commit`. További információ: <https://git-scm.com/docs/git-commit-tree>.

- Commit objektum létrehozása a megadott üzenettel:

`git commit-tree {{tree}} -m "{{message}}"`

- Létrehoz egy commit objektumot, amely az üzenetet egy fájlból olvassa be (használja a `-` a `stdin`):

`git commit-tree {{tree}} -F {{path/to/file}}`

- GPG aláírással ellátott commit objektum létrehozása:

`git commit-tree {{tree}} -m "{{message}}" --gpg-sign`

- Commit objektum létrehozása a megadott szülő commit objektummal:

`git commit-tree {{tree}} -m "{{message}}" -p {{parent_commit_sha}}`
