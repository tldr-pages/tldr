# powershell

> Command-line shell en scripttaal, ontworpen voor systeembeheer.
> Deze opdracht verwijst naar PowerShell versie 5.1 en lager (ook bekend als legacy Windows PowerShell). Voor de nieuwere, platformonafhankelijke versie van PowerShell (ook bekend als PowerShell Core), gebruik `pwsh` in plaats van `powershell`.
> Meer informatie: <https://learn.microsoft.com/windows-server/administration/windows-commands/powershell>.

- Start een interactieve shellsessie:

`powershell`

- Start een interactieve shellsessie zonder opstartconfiguraties te laden:

`powershell -NoProfile`

- Voer specifieke commando's uit:

`powershell -Command "{{echo 'powershell wordt uitgevoerd'}}"`

- Voer een specifiek script uit:

`powershell -File {{pad/naar/script.ps1}}`

- Start een sessie met een specifieke versie van PowerShell:

`powershell -Version {{versie}}`

- Voorkom dat een shell afsluit na het uitvoeren van opstartcommando's:

`powershell -NoExit`

- Beschrijf het formaat van gegevens die naar PowerShell worden verzonden:

`powershell -InputFormat {{Text|XML}}`

- Bepaal hoe een output van PowerShell wordt opgemaakt:

`powershell -OutputFormat {{Text|XML}}`
