# git rev-parse

> Az egyes revíziókhoz kapcsolódó metaadatok megjelenítése. További információ: <https://git-scm.com/docs/git-rev-parse>.

- Egy ág commit hash-jának lekérdezése:

`git rev-parse {{branch_name}}`

- Az aktuális ág nevének lekérdezése:

`git rev-parse --abbrev-ref {{HEAD}}`

- A gyökérkönyvtár abszolút elérési útjának lekérdezése:

`git rev-parse --show-toplevel`
