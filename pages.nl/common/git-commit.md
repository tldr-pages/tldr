# git commit

> Commit bestanden naar de repository.
> Meer informatie: <https://git-scm.com/docs/git-commit>.

- Open een tekstbewerker om een bericht te schrijven en commit de toegevoegde bestanden naar de repository:

`git commit`

- Commit toegevoegde bestanden naar de repository met het opgegeven bericht:

`git commit {{[-m|--message]}} "{{bericht}}"`

- Commit toegevoegde bestanden met een bericht dat uit een bestand wordt gelezen:

`git commit {{[-F|--file]}} {{pad/naar/commit_bericht_bestand}}`

- Voeg automatisch alle bewerkte en verwijderde bestanden toe en commit:

`git commit {{[-a|--all]}} {{[-m|--message]}} "{{bericht}}"`

- Commit toegevoegde bestanden en onderteken ze met de opgegeven GPG-sleutel (of de sleutel die is gedefinieerd in het configuratiebestand als er geen `sleutel_id` is opgegeven):

`git commit {{[-S|--gpg-sign]}} {{sleutel_id}} {{[-m|--message]}} "{{bericht}}"`

- Voeg de huidige wijzigingen toe aan de laatste commit en herschrijf deze, waarbij de commit hash wordt aangepast en een tekstverwerker wordt geopend om het bericht te veranderen:

`git commit --amend`

- Commit alleen specifieke (al toegevoegde) bestanden:

`git commit {{pad/naar/bestand1 pad/naar/bestand2 ...}}`

- Maak een commit met het opgegeven bericht en omschrijving:

`git commit {{[-m|--message]}} "{{bericht}}" {{[-m|--message]}} "{{omschrijving}}"`
