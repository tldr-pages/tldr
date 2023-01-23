# alex

> Egy eszköz, amely elkapja az érzéketlen, tapintatlan írásokat. Segít megtalálni a nemeket előnyben részesítő, polarizáló, faji, vallási, vagy egyéb egyenlőtlen megfogalmazásokat a szövegben. További információ: <https://github.com/get-alex/alex>.

- Szövegelemzés a `stdin` oldalról:

`echo {{His network looks good}} | alex --stdin`

- Elemzi az aktuális könyvtárban lévő összes fájlt:

`alex`

- Egy adott fájl elemzése:

`alex {{textfile.md}}`

- Az összes Markdown-fájl elemzése a `example.md` kivételével:

`alex *.md !{{example.md}}`
