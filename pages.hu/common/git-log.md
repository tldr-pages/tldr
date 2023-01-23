# git log

> A commitok előzményeinek megjelenítése. További információ: <https://git-scm.com/docs/git-log>.

- Megjeleníti a commitok sorrendjét az aktuális könyvtárban lévő Git-repository fordított időrendben, az aktuális munkakönyvtárban lévő commitoktól kezdve:

`git log`

- Egy adott fájl vagy könyvtár előzményeinek megjelenítése, beleértve a különbségeket is:

`git log -p {{path/to/file_or_directory}}`

- Áttekintést mutat arról, hogy melyik fájl(ok) változott(ak) az egyes commitokban:

`git log --stat`

- Az aktuális ágban lévő commitok grafikonjának megjelenítése, csak az egyes commit üzenetek első sorát használva:

`git log --oneline --graph`

- A teljes repo összes commitjának, címkéjének és ágának grafikonja:

`git log --oneline --decorate --all --graph`

- Csak azok a commitok megjelenítése, amelyek üzenetei tartalmaznak egy adott karakterláncot (a nagy- és kisbetűket nem figyelembe véve):

`git log -i --grep {{search_string}}`

- Egy adott szerző utolsó N commitjának megjelenítése:

`git log -n {{number}} --author={{author}}`

- Két dátum közötti commitok megjelenítése (ééééé-hh-hh-hh):

`git log --before="{{2017-01-29}}" --after="{{2017-01-17}}"`
