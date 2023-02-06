# getmac

> A rendszer MAC-címének megjelenítése. További információ: <https://learn.microsoft.com/windows-server/administration/windows-commands/getmac>.

- Az aktuális rendszer MAC-címeinek megjelenítése:

`getmac`

- A részletek megjelenítése meghatározott formátumban:

`getmac /fo {{table|list|csv}}`

- A fejléc kizárása a kimeneti listából:

`getmac /nh`

- Távoli gép MAC-címeinek megjelenítése:

`getmac /s {{hostname}} /u {{username}} /p {{password}}`

- A MAC-címek megjelenítése szó szerinti információkkal:

`getmac /v`

- Részletes használati információk megjelenítése:

`getmac /?`
