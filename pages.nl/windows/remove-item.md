# Remove-Item

> Verwijder bestanden, mappen, evenals registersleutels en subkeys.
> Deze opdracht kan alleen door PowerShell worden uitgevoerd.
> Meer informatie: <https://learn.microsoft.com/powershell/module/microsoft.powershell.management/remove-item>.

- Verwijder specifieke bestanden of registersleutels (zonder subkeys):

`Remove-Item {{pad\naar\bestand_of_key1 pad\naar\bestand_of_key2 ...}}`

- Verwijder verborgen of alleen-lezen bestanden:

`Remove-Item -Force {{pad\naar\bestand1 pad\naar\bestand2 ...}}`

- Verwijder specifieke bestanden of registersleutels interactief gevraagd vóór elke verwijdering:

`Remove-Item -Confirm {{pad\naar\bestand_of_key1 pad\naar\bestand_of_key2 ...}}`

- Verwijder specifieke bestanden en mappen recursief (Windows 10 versie 1909 of hoger):

`Remove-Item -Recurse {{pad\naar\bestand_of_map1 pad\naar\bestand_of_map2 ...}}`

- Verwijder specifieke Windows-registersleutels en al zijn subkeys:

`Remove-Item -Recurse {{pad\naar\key1 pad\naar\key2 ...}}`

- Voer een dry-run van het verwijderproces uit:

`Remove-Item -WhatIf {{pad\naar\bestand1 pad\naar\bestand2 ...}}`
