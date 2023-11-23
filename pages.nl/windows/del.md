# del

> Verwijder een of meer bestanden.
> In PowerShell is dit commando een alias van `Remove-Item`. Deze documentatie is gebaseerd op de Command Prompt (`cmd`) versie van `del`.
> Meer informatie: <https://learn.microsoft.com/windows-server/administration/windows-commands/del>.

- Bekijk de documentatie van het equivalente PowerShell commando:

`tldr remove-item`

- Verwijder een of meer, door spatie gescheiden, bestanden of patronen:

`del {{file_pattern}}`

- Vraag om bevestiging voordat u elk bestand verwijdert:

`del {{file_pattern}} /p`

- Forceer de verwijdering van alleen-lezen bestanden:

`del {{file_pattern}} /f`

- Verwijder de bestand(en) recursief uit alle submappen:

`del {{file_pattern}} /s`

- Vraag niet om bevestiging voor het verwijderen van bestanden gebaseerd op een globale wildcard:

`del {{file_pattern}} /q`

- Geef de beschikbare hulp en lijst met attributen weer:

`del /?`

- Verwijder bestanden op basis van opgegeven kenmerken:

`del {{file_pattern}} /a {{attribute}}`
