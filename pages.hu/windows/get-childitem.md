# Get-ChildItem

> Egy könyvtár elemeinek listázása. Ez a parancs csak a PowerShell segítségével használható. További információ: <https://learn.microsoft.com/powershell/module/microsoft.powershell.management/get-childitem>.

- Az aktuális könyvtár összes nem rejtett elemének listázása:

`Get-ChildItem`

- Csak az aktuális könyvtárban lévő könyvtárak listázása:

`Get-ChildItem -Directory`

- Csak az aktuális könyvtárban lévő fájlok listázása:

`Get-ChildItem -File`

- Az aktuális könyvtárban lévő elemek listázása, beleértve a rejtett elemeket is:

`Get-ChildItem -Hidden`

- Az aktuális könyvtáron kívüli könyvtárban lévő elemek listázása:

`Get-ChildItem -Path {{path/to/directory}}`
