# Set-Clipboard

> PowerShell commando om inhoud naar het klembord te kopiëren.
> Opmerking: `scb` kan gebruikt worden als een alias voor `Set-Clipboard`.
> Meer informatie: <https://learn.microsoft.com/powershell/module/microsoft.powershell.management/set-clipboard>.

- Kopieer tekst naar het klembord:

`Set-Clipboard -Value "{{tekst}}"`

- Kopieer meerdere teksten naar het klembord, gescheiden door een nieuwe regel:

`Set-Clipboard -Value @("{{tekst 1}}", "{{tekst 2}}", "{{tekst 3}}")`

- Kopieer bestanden of mappen naar het klembord:

`Set-Clipboard -Path "{{pad\naar\bestanden_of_mappen}}"`

- Kopieer meerdere bestanden:

`Set-Clipboard -Path "{{pad\naar\bestand1}}","{{pad\naar\bestand2}}","{{pad\naar\bestand3}}"`

- Wis het klembord:

`Set-Clipboard ""`
