# Get-Alias

> Toon en verkrijg commando aliases in de huidige PowerShell sessie.
> Dit commando kan alleen worden uitgevoerd onder PowerShell.
> Meer informatie: <https://learn.microsoft.com/powershell/module/microsoft.powershell.utility/get-alias>.

- Toon alle aliases in de huidige sessie:

`Get-Alias`

- Ontvang de aliased commando naam:

`Get-Alias {{commando_alias}}`

- Toon alle aliases toegewezen aan een specifiek commando:

`Get-Alias -Definition {{commando}}`

- Toon aliases die beginnen met `abc`, maar sluit die uit die eindigen op`def`:

`Get-Alias {{abc}}* -Exclude *{{def}}`
