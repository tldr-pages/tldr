# more

> Toon gepagineerde uitvoer van `stdin` of een bestand.
> Meer informatie: <https://learn.microsoft.com/windows-server/administration/windows-commands/more>.

- Toon gepagineerde uitvoer van `stdin`:

`{{echo test}} | more`

- Toon gepagineerde uitvoer van één of meer bestanden:

`more {{pad\naar\bestand}}`

- Zet tabs om naar het opgegeven aantal spaties:

`more {{pad\naar\bestand}} /t{{spaties}}`

- Wis het scherm voordat de pagina wordt weergegeven:

`more {{pad\naar\bestand}} /c`

- Toon de uitvoer beginnend bij regel 5:

`more {{pad\naar\bestand}} +{{5}}`

- Schakel uitgebreide interactieve modus in (zie help voor gebruik):

`more {{pad\naar\bestand}} /e`

- Toon de help:

`more /?`
