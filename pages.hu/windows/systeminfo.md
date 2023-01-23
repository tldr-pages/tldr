# systeminfo

> Az operációs rendszer konfigurációjának megjelenítése egy helyi vagy távoli gépen. További információ: <https://learn.microsoft.com/windows-server/administration/windows-commands/systeminfo>.

- A helyi gép rendszerkonfigurációjának megjelenítése:

`systeminfo`

- A rendszer konfigurációjának megjelenítése egy megadott kimeneti formátumban:

`systeminfo /fo {{table|list|csv}}`

- Távoli gép rendszerkonfigurációjának megjelenítése:

`systeminfo /s {{remote_name}} /u {{username}} /p {{password}}`

- Részletes használati információk megjelenítése:

`systeminfo /?`
