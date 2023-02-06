# more

> A `stdin` vagy egy fájl oldalankénti kimeneteinek megjelenítése. További információ: <https://learn.microsoft.com/windows-server/administration/windows-commands/more>.

- Oldalankénti kimenet megjelenítése a `stdin` oldalról:

`{{echo test}} | more`

- Egy vagy több fájlból származó oldalszámozott kimenet megjelenítése:

`more {{path/to/file}}`

- A tabulátorok átalakítása a megadott számú szóközökké:

`more {{path/to/file}} /t{{spaces}}`

- A képernyő törlése az oldal megjelenítése előtt:

`more {{path/to/file}} /c`

- A kimenet megjelenítése az 5. sorral kezdődően:

`more {{path/to/file}} +{{5}}`

- Bővített interaktív mód engedélyezése (a használathoz lásd a súgóban):

`more {{path/to/file}} /e`

- Teljes használati információ megjelenítése:

`more /?`
