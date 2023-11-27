# find

> Vind een gespecificieerde string in een bestand.
> Meer informatie: <https://learn.microsoft.com/windows-server/administration/windows-commands/find>.

- Vind de regels die een specifieke string bevatten:

`find "{{string}}" {{pad/naar/bestand_of_map}}`

- Laat regels zie die de string niet bevatten:

`find "{{string}}" {{pad/naar/bestand_of_map}} /v`

- Toon het aantal regels dat de string bevat:

`find "{{string}}" {{pad/naar/bestand_of_map}} /c`

- Laat het aantal regels zien samen met de regels:

`find "{{string}}" {{pad/naar/bestand_of_map}} /n`
