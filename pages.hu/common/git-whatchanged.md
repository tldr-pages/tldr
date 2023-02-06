# git whatchanged

> Megmutatja, hogy mi változott a legutóbbi commitok vagy fájlok esetében. Lásd még: `git log`. További információ: <https://git-scm.com/docs/git-whatchanged>.

- A legutóbbi commitok naplóinak és változásainak megjelenítése:

`git whatchanged`

- A megadott időkereten belüli legutóbbi commitok naplóinak és változásainak megjelenítése:

`git whatchanged --since="{{2 hours ago}}"`

- Meghatározott fájlok vagy könyvtárak legutóbbi commitjainak naplóinak és változásainak megjelenítése:

`git whatchanged {{path/to/file_or_directory}}`
