# Where-Object

> Selecteert objecten uit een verzameling op basis van hun eigenschapswaarden.
> Dit commando kan alleen gebruikt worden via PowerShell.
> Meer informatie: <https://learn.microsoft.com/powershell/module/microsoft.powershell.core/where-object>.

- Filter aliassen op naam:

`Get-Alias | Where-Object -{{Property}} {{Name}} -{{eq}} {{naam}}`

- Toon een lijst van alle services die momenteel zijn gestopt. De `$_` automatische variable representeert ieder object dat word gestuurd naar de `Where-Object` cmdlet:

`Get-Service | Where-Object {$_.Status -eq "Stopped"}`

- Gebruik meerdere condities:

`Get-Module -ListAvailable | Where-Object { $_.Name -NotLike "Microsoft*" -And $_.Name -NotLike "PS*" }`
