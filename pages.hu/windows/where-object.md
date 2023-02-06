# Where-Object

> Objektumok kiválasztása egy gyűjteményből azok tulajdonságértékei alapján. Ez a parancs csak a PowerShell segítségével használható. További információ: <https://learn.microsoft.com/powershell/module/microsoft.powershell.core/where-object>.

- Aliasok szűrése a neve alapján:

`Get-Alias | Where-Object -{{Property}} {{Name}} -{{eq}} {{name}}`

- A jelenleg leállított szolgáltatások listájának lekérése. A `$_` automatikus változó minden olyan objektumot képvisel, amelyet a `Where-Object` cmdletnek ad át:

`Get-Service | Where-Object {$_.Status -eq "Stopped"}`

- Több feltétel használata:

`Get-Module -ListAvailable | Where-Object { $_.Name -NotLike "Microsoft*" -And $_.Name -NotLike "PS*" }`
