# Get-Clipboard

> PowerShell commando om inhoud van het klembord op te halen.
> Opmerking: `gcb` kan gebruikt worden als een alias voor `Get-Clipboard`.
> Meer informatie: <https://learn.microsoft.com/powershell/module/microsoft.powershell.management/get-clipboard>.

- Haal tekst van het klembord op:

`Get-Clipboard`

- Haal de inhoud van het klembord op in een specifiek tekstformaat:

`Get-Clipboard -TextFormatType {{Text|Html|Rtf}}`

- Haal de ruwe inhoud van het klembord op:

`Get-Clipboard -Raw`

- Haal een afbeelding op:

`Get-Clipboard -Format Image`

- Haal bestandspaden op die in de verkenner zijn gekopieerd:

`Get-Clipboard -Format FileDropList`
