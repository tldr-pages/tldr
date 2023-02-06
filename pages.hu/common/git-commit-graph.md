# git commit-graph

> Git commit-graph fájlok írása és ellenőrzése. További információ: <https://git-scm.com/docs/git-commit-graph>.

- Írjon commit-graph fájlt a csomagolt commitokhoz az adattár helyi `.git` könyvtárában:

`git commit-graph write`

- Írjon egy commit-graph fájlt, amely tartalmazza az összes elérhető commitot:

`git show-ref --hash | git commit-graph write --stdin-commits`

- Írjon egy commit-graph fájlt, amely tartalmazza az aktuális commit-graph fájlban lévő összes commitot, valamint a `HEAD` címen elérhető commitokat:

`git rev-parse {{HEAD}} | git commit-graph write --stdin-commits --append`
