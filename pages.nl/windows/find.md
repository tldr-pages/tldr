# find

> Vind een gespecificeerde string in bestanden.
> Meer informatie: <https://learn.microsoft.com/windows-server/administration/windows-commands/find>.

- Vind de regels die een specifieke string bevatten:

`find "{{string}}" {{pad\naar\bestand_of_map}}`

- Laat regels zien die de string niet bevatten:

`find "{{string}}" {{pad\naar\bestand_of_map}} /v`

- Toon het aantal regels dat de string bevat:

`find "{{string}}" {{pad\naar\bestand_of_map}} /c`

- Toon de regelnummers samen met de regels:

`find "{{string}}" {{pad\naar\bestand_of_map}} /n`
