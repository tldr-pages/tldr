# pwsh

> Command-line shell en scripting taal specifiek ontworpen voor systeemadministratie.
> Dit commando refereert naar PowerShell versie 6 en hoger (ook wel bekend als  PowerShell Core en cross-platform PowerShell).
> Om de originele Windows versie (5.1 en lager, ook wel bekend als de legacy Windows PowerShell) te gebruiken, gebruik `powershell` in plaats van `pwsh`.
> Meer informatie: <https://learn.microsoft.com/powershell/module/microsoft.powershell.core/about/about_pwsh>.

- Start een interactieve shell sessie:

`pwsh`

- Start een interactieve shell sessie zonder het laden van startup configuraties:

`pwsh -NoProfile`

- Voer specifieke commando's uit:

`pwsh -Command "{{echo 'powershell is uitgevoerd'}}"`

- Voer een specifiek script uit:

`pwsh -File {{pad/naar/script.ps1}}`

- Start een sessie met een specifieke versie van PowerShell:

`pwsh -Version {{versie}}`

- Voorkom dat een shell afsluit na het uitvoeren van de opstart-commando's:

`pwsh -NoExit`

- Beschrijf het formaat van de data die gestuurd word naar to PowerShell:

`pwsh -InputFormat {{Text|XML}}`

- Bepaal hoe een uitvoer van Powershell word geformateerd:

`pwsh -OutputFormat {{Text|XML}}`
