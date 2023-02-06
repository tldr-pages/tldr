# ed

> Az eredeti Unix szövegszerkesztő. Lásd még: `awk`, `sed`. További információ: [https://www.gnu.org/software/ed/manual/ed_manual.html.](https://www.gnu.org/software/ed/manual/ed_manual.html)

- Indítson interaktív szerkesztési munkamenetet egy üres dokumentummal:

`ed`

- Interaktív szerkesztési munkamenet indítása egy üres dokumentummal és egy adott prompttal:

`ed --prompt='> '`

- Interaktív szerkesztési munkamenet indítása felhasználóbarát hibákkal:

`ed --verbose`

- Interaktív szerkesztési munkamenet indítása üres dokumentummal és diagnosztika, bájtszám és '!' prompt nélkül:

`ed --quiet`

- Interaktív szerkesztő munkamenet indítása kilépési állapotváltoztatás nélkül, ha a parancs sikertelen:

`ed --loose-exit-status`

- Egy adott fájl szerkesztése (ez a betöltött fájl bájtszámát mutatja):

`ed {{path/to/file}}`

- Egy karakterlánc cseréje egy adott helyettesítővel az összes sorban:

`,s/{{regular_expression}}/{{replacement}}/g`
