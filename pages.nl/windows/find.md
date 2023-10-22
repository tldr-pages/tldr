# find

> Vind een gespecificieerde string in een bestand.
> Meer informatie: <https://learn.microsoft.com/windows-server/administration/windows-commands/find>.

- Vind de lijnen dat een specifieke string bevatten:

`find {{string}} {{pad/naar/bestand_of_map}}`

- Laat lijnen zie die de string niet bevatten:

`find {{string}} {{pad/naar/bestand_of_map}} /v`

- Toon het aantal lijnen dat de string bevat:

`find {{string}} {{pad/naar/bestand_of_map}} /c`

- Laat het aantal lijnen zien samen met de lijnen:

`find {{string}} {{pad/naar/bestand_of_map}} /n`
