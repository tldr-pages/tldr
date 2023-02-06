# shutdown

> Eszköz a gép leállítására, újraindítására vagy kijelentkezésre. További információ: <https://learn.microsoft.com/windows-server/administration/windows-commands/shutdown>.

- Az aktuális gép leállítása:

`shutdown /s`

- Az aktuális gép leállítása az összes alkalmazás kényszerlezárásával:

`shutdown /s /f`

- Az aktuális gép azonnali újraindítása:

`shutdown /r /t 0`

- Az aktuális gép hibernálása:

`shutdown /h`

- Az aktuális gép kijelentkezése:

`shutdown /l`

- A leállítás előtti várakozási idő megadása másodpercben:

`shutdown /s /t {{seconds}}`

- Olyan leállítási sorozat megszakítása, amelynek időkorlátja még nem járt le:

`shutdown /a`

- Távoli gép leállítása:

`shutdown /m {{\\hostname}}`
