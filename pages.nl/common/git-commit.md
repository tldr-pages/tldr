# git commit

> Commit bestanden naar de repository.
> Meer informatie: <https://git-scm.com/docs/git-commit>.

- Commit toegevoegde bestanden naar de repository met een bericht:

`git commit {{[-m|--message]}} "{{bericht}}"`

- Commit toegevoegde bestanden met een bericht dat uit een bestand wordt gelezen:

`git commit {{[-F|--file]}} {{pad/naar/commit_bericht_bestand}}`

- Voeg automatisch alle bewerkte en verwijderde bestanden toe en commit met een bericht:

`git commit {{[-a|--all]}} {{[-m|--message]}} "{{bericht}}"`

- Commit toegevoegde bestanden en onderteken ze met de opgegeven GPG-sleutel (of de sleutel die is gedefinieerd in het configuratiebestand als er geen argument is opgegeven):

`git commit {{[-S|--gpg-sign]}} {{sleutel_id}} {{[-m|--message]}} "{{bericht}}"`

- Voeg de huidige wijzigingen toe aan de laatste commit en herschrijf deze, waarbij de commit hash wordt aangepast:

`git commit --amend`

- Commit alleen specifieke (al toegevoegde) bestanden:

`git commit {{pad/naar/bestand1 pad/naar/bestand2 ...}}`

- Maak een commit, zelfs als er geen toegevoegde bestanden zijn:

`git commit {{[-m|--message]}} "{{bericht}}" --allow-empty`
