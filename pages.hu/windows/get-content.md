# Get-Content

> A megadott helyen lévő elem tartalmának lekérdezése. Ez a parancs csak a PowerShell segítségével használható. További információ: <https://learn.microsoft.com/powershell/module/microsoft.powershell.management/get-content>.

- Egy fájl tartalmának megjelenítése:

`Get-Content -Path {{path/to/file}}`

- Egy fájl első néhány sorának megjelenítése:

`Get-Content -Path {{path/to/file}} -TotalCount {{count}}`

- A fájl tartalmának megjelenítése és folyamatos olvasás a `Ctrl + C` megnyomásáig:

`Get-Content -Path {{path/to/file}} -Wait`
