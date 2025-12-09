# Move-Item

> Verplaats of hernoem bestanden, mappen, registersleutels en andere PowerShell data items.
> Dit commando kan alleen worden uitgevoerd onder PowerShell.
> Meer informatie: <https://learn.microsoft.com/powershell/module/microsoft.powershell.management/move-item>.

- Hernoem een bestand of map wanneer het doelwit geen bestaande map is:

`Move-Item {{pad\naar\bron}} {{pad\naar\doel}}`

- Verplaats een bestand of map naar een bestaande map:

`Move-Item {{pad\naar\bron}} {{pad\naar\bestaande_map}}`

- Hernoem of verplaats bestand(en) met een specifieke naam (behandel geen speciale karakters in strings):

`Move-Item -LiteralPath "{{pad\naar\bron}}" {{pad\naar\bestand_of_map}}`

- Verplaats meerdere bestanden naar een bestaande map, waardoor de bestandsnamen ongewijzigd blijven:

`Move-Item {{pad\naar\bron1 , pad\naar\bron2 ...}} {{pad\naar\bestaande_map}}`

- Verplaats of hernoem registersleutel(s):

`Move-Item {{pad\naar\bron_sleutel1 , pad\naar\bron_sleutel2 ...}} {{pad\naar\nieuwe_of_bestaande_sleutel}}`

- Vraag niet om bevestiging voordat bestaande bestanden of registersleutels worden overschreven:

`mv -Force {{pad\naar\bron}} {{pad\naar\doel}}`

- Vraag om bevestiging voordat bestaande bestanden worden overschreven, ongeacht bestandsrechten:

`mv -Confirm {{pad\naar\bron}} {{pad\naar\doel}}`

- Verplaats bestanden in de dry-run-modus en toon bestanden en mappen die kunnen worden verplaatst zonder ze uit te voeren:

`mv -WhatIf {{pad\naar\bron}} {{pad\naar\doel}}`
