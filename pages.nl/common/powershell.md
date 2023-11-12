# powershell

> Command-line shell en scripting taal specifiek ontworpen voor systeemadministratie.
> Zie ook: `pwsh`.
> Meer informatie: <https://learn.microsoft.com/powershell/module/microsoft.powershell.core/about/about_pwsh>.

- Start een interactieve shell sessie:

`powershell`

- Start een interactieve shell sessie zonder het laden van startup configuraties:

`powershell -NoProfile`

- Voer specifieke commando's uit:

`powershell -Command "{{echo 'powershell is uitgevoerd'}}"`

- Voer een specifiek script uit:

`powershell -File {{pad/naar/script.ps1}}`

- Start een sessie met een specifieke versie van PowerShell:

`powershell -Version {{versie}}`

- Voorkom dat een shell uitgaat na het uitvoeren van startup commando's:

`powershell -NoExit`

- Beschrijf het formaat van gegevens die naar PowerShell zijn verzonden:

`powershell -InputFormat {{Text|XML}}`

- Bepaal hoe een output van PowerShell wordt opgemaakt:

`powershell -OutputFormat {{Text|XML}}`
