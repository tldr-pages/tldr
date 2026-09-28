# move

> Verplaats of hernoem bestanden en mappen.
> In PowerShell is dit commando een alias van `Move-Item`. Deze documentatie is gebaseerd op de Command Prompt (`cmd`) versie van `move`.
> Meer informatie: <https://learn.microsoft.com/windows-server/administration/windows-commands/move>.

- Bekijk de documentatie van het equivalente PowerShell commando:

`tldr move-item`

- Hernoem een bestand of map als het doel een niet-bestaande map is:

`move {{pad\naar\bron}} {{pad\naar\doel}}`

- Verplaats een bestand of map naar een bestaande map:

`move {{pad\naar\bron}} {{pad\naar\bestaande_map}}`

- Verplaats een map of bestand naar een andere schijf:

`move {{C:\pad\naar\bron}} {{D:\pad\naar\doel}}`

- Vraag niet om bevestiging voordat bestaande bestanden worden overschreven:

`move /Y {{pad\naar\bron}} {{pad\naar\bestaande_map}}`

- Vraag om bevestiging voordat bestaande bestanden worden overschreven, ongeacht de bestandspermissies:

`move /-Y {{pad\naar\bron}} {{pad\naar\bestaande_map}}`
