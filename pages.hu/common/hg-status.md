# hg status

> A munkakönyvtárban megváltozott fájlok megjelenítése. További információ: <https://www.mercurial-scm.org/doc/hg.1.html#status>.

- A megváltozott fájlok állapotának megjelenítése:

`hg status`

- Csak a módosított fájlok megjelenítése:

`hg status --modified`

- Csak a hozzáadott fájlok megjelenítése:

`hg status --added`

- Csak az eltávolított fájlok megjelenítése:

`hg status --removed`

- Csak a törölt (de követett) fájlok megjelenítése:

`hg status --deleted`

- A munkakönyvtárban bekövetkezett változások megjelenítése egy megadott módosításkészlethez képest:

`hg status --rev {{revision}}`

- Csak a megadott globális mintának megfelelő fájlok megjelenítése:

`hg status --include {{pattern}}`

- Megjelenítés a megadott glob-mintának megfelelő fájlok kivételével:

`hg status --exclude {{pattern}}`
