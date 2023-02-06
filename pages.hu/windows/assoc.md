# assoc

> A fájlkiterjesztések és fájltípusok közötti asszociációk megjelenítése vagy módosítása. További információ: <https://learn.microsoft.com/windows-server/administration/windows-commands/assoc>.

- A fájlkiterjesztések és fájltípusok közötti összes társítás listázása:

`assoc`

- Egy adott kiterjesztéshez kapcsolódó fájltípusok megjelenítése:

`assoc {{.txt}}`

- A társított fájltípus beállítása egy adott kiterjesztéshez:

`assoc .{{txt}}={{txtfile}}`

- A `assoc` kimenetének egy-egy képernyőn történő megtekintése:

`assoc | {{more}}`
