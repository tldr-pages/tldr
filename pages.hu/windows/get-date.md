# Get-Date

> Az aktuális dátum és idő lekérdezése. Ez a parancs csak a PowerShell segítségével használható. További információ: <https://learn.microsoft.com/powershell/module/microsoft.powershell.utility/get-date>.

- Az aktuális dátum és idő megjelenítése:

`Get-Date`

- Az aktuális dátum és idő megjelenítése .NET formátummeghatározóval:

`Get-Date -Format "{{yyyy-MM-dd HH:mm:ss}}"`

- Az aktuális dátum és idő megjelenítése UTC és ISO 8601 formátumban:

`(Get-Date).ToUniversalTime()`

- Unix időbélyegző átalakítása:

`Get-Date -UnixTimeSeconds {{1577836800}}`
