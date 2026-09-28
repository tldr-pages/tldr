# Invoke-Item

> Open bestanden in hun bijbehorende standaardprogramma's.
> Opmerking: dit commando kan alleen gebruikt worden via PowerShell.
> Meer informatie: <https://learn.microsoft.com/powershell/module/microsoft.powershell.management/invoke-item>.

- Open een bestand in het standaardprogramma:

`Invoke-Item -Path {{pad\naar\bestand}}`

- Open alle bestanden in een map:

`Invoke-Item -Path {{pad\naar\map}}\*`

- Open alle PNG's in een map:

`Invoke-Item -Path {{pad\naar\map}}\*.png`

- Open alle bestanden in een map die een specifiek trefwoord bevatten:

`Invoke-Item -Path {{pad\naar\map}}\* -Include {{*trefwoord*}}`

- Open alle bestanden in een map, behalve die een specifiek trefwoord bevatten:

`Invoke-Item -Path {{pad\naar\map}}\* -Exclude {{*trefwoord*}}`

- Simuleer een uitvoering om te bepalen welke bestanden in een map geopend zullen worden via `Invoke-Item`:

`Invoke-Item -Path {{pad\naar\map}}\* -WhatIf`
