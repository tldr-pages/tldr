# Get-Alias

> Toon en verkrijg commandoaliassen in de huidige PowerShell sessie.
> Dit commando kan alleen worden uitgevoerd onder PowerShell.
> Meer informatie: <https://learn.microsoft.com/powershell/module/microsoft.powershell.utility/get-alias>.

- Toon alle aliassen in de huidige sessie:

`Get-Alias`

- Haal de gealiaste commandonaam op:

`Get-Alias {{commando_alias}}`

- Toon alle aliassen toegewezen aan een specifiek commando:

`Get-Alias -Definition {{commando}}`

- Toon aliassen die beginnen met `abc`, maar sluit die uit die eindigen op `def`:

`Get-Alias {{abc}}* -Exclude *{{def}}`
