# Get-Help

> Toon hulpinformatie en documentatie voor PowerShell-commando's (aliassen, cmdlets en functies).
> Dit commando kan alleen worden uitgevoerd via PowerShell.
> Meer informatie: <https://learn.microsoft.com/powershell/module/microsoft.powershell.core/get-help>.

- Toon algemene hulpinformatie voor een specifiek PowerShell-commando:

`Get-Help {{commando}}`

- Toon meer gedetailleerde documentatie voor een specifiek PowerShell-commando:

`Get-Help {{commando}} -Detailed`

- Toon de volledige technische documentatie voor een specifiek PowerShell-commando:

`Get-Help {{commando}} -Full`

- Print alleen de documentatie voor een specifieke parameter van het PowerShell-commando (gebruik `*` om alle parameters te tonen), indien beschikbaar:

`Get-Help {{commando}} -Parameter {{parameter}}`

- Print alleen de voorbeelden van de cmdlet, indien beschikbaar:

`Get-Help {{commando}} -Examples`

- Toon alle beschikbare cmdlet-hulppagina's:

`Get-Help *`

- Werk de huidige hulp- en documentatiekennisbank bij met `Update-Help`:

`Update-Help`

- Bekijk een online versie van de PowerShell-commandodocumentatie in de standaard webbrowser:

`Get-Help {{commando}} -Online`
