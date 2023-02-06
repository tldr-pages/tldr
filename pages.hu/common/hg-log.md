# hg log

> Az adattár felülvizsgálati előzményeinek megjelenítése. További információ: <https://www.mercurial-scm.org/doc/hg.1.html#log>.

- Az adattár teljes revíziós előzményeinek megjelenítése:

`hg log`

- A revíziós előzmények megjelenítése ASCII grafikonnal:

`hg log --graph`

- A revíziós előzmények megjelenítése egy megadott mintának megfelelő fájlnevekkel:

`hg log --include {{pattern}}`

- A revíziós előzmények megjelenítése a megadott mintának megfelelő fájlnevek kivételével:

`hg log --exclude {{pattern}}`

- Egy adott revízió naplóinformációinak megjelenítése:

`hg log --rev {{revision}}`

- Egy adott ág revíziós előzményeinek megjelenítése:

`hg log --branch {{branch}}`

- Egy adott dátumhoz tartozó revíziós előzmények megjelenítése:

`hg log --date {{date}}`

- Egy adott felhasználó által lekötött revíziók megjelenítése:

`hg log --user {{user}}`
