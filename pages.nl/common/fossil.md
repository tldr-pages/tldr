# fossil

> Gedistribueerd versiebheer systeem met een ingebouwde wiki, bugtracker en webinterface.
> Sommige subcommando's zoals `db` hebben hun eigen documentatie.
> Meer informatie: <https://fossil-scm.org/home/help>.

- Maak een nieuwe lege Fossil-repository aan:

`fossil init {{repository_naam.fossil}}`

- Maak een lokale kopie van een externe repository:

`fossil clone {{externe_url}}`

- Toon een overzicht van de huidige status van een repository:

`fossil status`

- Voeg een nieuw bestand toe:

`fossil add {{pad/naar/bestand}}`

- Verwijder een bestand:

`fossil {{[rm|delete]}} {{pad/naar/bestand}}`

- Commit alle toegevoegde wijzigingen:

`fossil {{[ci|commit]}} {{[-m|--comment]}} "{{bericht}}"`

- Stuur wijzigingen van de lokale repository naar een externe repository:

`fossil push {{externe_url}}`

- Haal de wijzigingen van een externe repository op naar een lokale repository:

`fossil pull {{externe_url}}`
