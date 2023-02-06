# Set-Date

> A számítógép rendszeridejének módosítása az Ön által megadott időre. Ez a parancs csak a PowerShell segítségével használható. További információ: <https://learn.microsoft.com/powershell/module/microsoft.powershell.utility/set-date>.

- Három napot ad hozzá a rendszer dátumához:

`Set-Date -Date (Get-Date).AddDays({{3}})`

- A rendszerórát 10 perccel hátrébb állítja:

`Set-Date -Adjust -0:10:0 -DisplayHint Time`

- Adjon hozzá 90 percet a rendszerórához:

`$90mins = New-TimeSpan -Minutes {{90}}; Set-Date -Adjust $90mins`
