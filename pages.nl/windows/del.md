# del

> Verwijder een of meer bestanden.
> In PowerShell is dit commando een alias van `Remove-Item`. Deze documentatie is gebaseerd op de Command Prompt (`cmd`) versie van `del`.
> Meer informatie: <https://learn.microsoft.com/windows-server/administration/windows-commands/del>.

- Bekijk de documentatie van het equivalente PowerShell commando:

`tldr remove-item`

- Verwijder een of meer bestanden of patronen:

`del {{bestand_patroon1 bestand_patroon2 ...}}`

- Vraag om bevestiging voordat elk bestand wordt verwijderd:

`del {{bestand_patroon}} /p`

- Forceer de verwijdering van alleen-lezen bestanden:

`del {{bestand_patroon}} /f`

- Verwijder de bestand(en) recursief uit alle submappen:

`del {{bestand_patroon}} /s`

- Vraag niet om bevestiging voor het verwijderen van bestanden gebaseerd op een globale wildcard:

`del {{bestand_patroon}} /q`

- Verwijder bestanden op basis van opgegeven attributen:

`del {{bestand_patroon}} /a {{attribuut}}`

- Toon de help en beschikbare attributen:

`del /?`
