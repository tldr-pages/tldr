# hg remove

> A megadott fájlok eltávolítása az előkészítő területről. További információ: <https://www.mercurial-scm.org/doc/hg.1.html#remove>.

- Fájlok vagy könyvtárak eltávolítása az előkészítő területről:

`hg remove {{path/to/file}}`

- A megadott mintának megfelelő összes beállított fájl eltávolítása:

`hg remove --include {{pattern}}`

- Az összes beállított fájl eltávolítása, kivéve azokat, amelyek megfelelnek egy megadott mintának:

`hg remove --exclude {{pattern}}`

- Al-tárolók rekurzív eltávolítása:

`hg remove --subrepos`

- Fizikailag eltávolított fájlok eltávolítása az adattárból:

`hg remove --after`
