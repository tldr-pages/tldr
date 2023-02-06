# hg commit

> Az összes szakaszolt vagy megadott fájl átadása a tárolóba. További információ: <https://www.mercurial-scm.org/doc/hg.1.html#commit>.

- A szakaszolt fájlok rögzítése az adattárba:

`hg commit`

- Egy adott fájl vagy könyvtár átadása:

`hg commit {{path/to/file_or_directory}}`

- Commit egy adott üzenettel:

`hg commit --message {{message}}`

- Az összes, egy megadott mintának megfelelő fájl lekötése:

`hg commit --include {{pattern}}`

- Az összes fájl lekötése, kivéve azokat, amelyek megfelelnek egy megadott mintának:

`hg commit --exclude {{pattern}}`

- Interaktív módban történő kötelezettségvállalás:

`hg commit --interactive`
