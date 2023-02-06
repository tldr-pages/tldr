# git fame

> Git-tárhoz való hozzájárulások szépen nyomtatása. További információ: <https://github.com/casperdcl/git-fame>.

- Az aktuális Git-tárhoz való hozzájárulások kiszámítása:

`git fame`

- A megadott reguláris kifejezésnek megfelelő fájlok/könyvtárak kizárása:

`git fame --excl "{{regular_expression}}"`

- A megadott dátum után készült hozzájárulások kiszámítása:

`git fame --since "{{3 weeks ago|2021-05-13}}"`

- Hozzájárulások megjelenítése a megadott formátumban:

`git fame --format {{pipe|yaml|json|csv|tsv}}`

- Hozzájárulások megjelenítése fájlkiterjesztésenként:

`git fame --bytype`

- A szóközös változtatások figyelmen kívül hagyása:

`git fame --ignore-whitespace`

- Fájlok közötti soráthelyezések és másolások felismerése:

`git fame -C`

- Fájlon belüli sormozgások és másolatok észlelése:

`git fame -M`
