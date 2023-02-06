# hg add

> Hozzáadja a megadott fájlokat a Mercurial következő commitjához. További információ: <https://www.mercurial-scm.org/doc/hg.1.html#add>.

- Fájlok vagy könyvtárak hozzáadása az előkészítő területhez:

`hg add {{path/to/file}}`

- A megadott mintának megfelelő összes még nem tárolt fájl hozzáadása:

`hg add --include {{pattern}}`

- Hozzáad az összes még nem előkészített fájlhoz, kivéve azokat, amelyek megfelelnek a megadott mintának:

`hg add --exclude {{pattern}}`

- Rekurzívan adjon hozzá al-tárolókat:

`hg add --subrepos`

- Tesztfuttatás végrehajtása műveletek végrehajtása nélkül:

`hg add --dry-run`
