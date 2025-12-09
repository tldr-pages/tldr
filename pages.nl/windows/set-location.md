# Set-Location

> Geef de huidige werkmap weer of ga naar een andere map.
> Deze opdracht kan alleen worden gebruikt via PowerShell.
> Meer informatie: <https://learn.microsoft.com/powershell/module/microsoft.powershell.management/set-location>.

- Ga naar de opgegeven map:

`Set-Location {{pad\naar\map}}`

- Ga naar een map in een andere drive:

`Set-Location {{C}}:{{pad\naar\map}}`

- Ga en toon de locatie van de opgegeven map:

`Set-Location {{pad\naar\map}} -PassThru`

- Ga naar de bovenliggende map van de huidige map:

`Set-Location ..`

- Ga naar de thuismap van de huidige gebruiker:

`Set-Location ~`

- Ga terug/vooruit naar de eerder gekozen map:

`Set-Location {{-|+}}`

- Ga naar de hoofdmap van de huidige drive:

`Set-Location \`
