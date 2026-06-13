# git add

> Voeg gewijzigde bestanden toe voor een commit.
> Meer informatie: <https://git-scm.com/docs/git-add>.

- Voeg een bestand toe voor een commit:

`git add {{pad/naar/bestand}}`

- Voeg alle bestanden toe (bijgehouden en niet bijgehouden):

`git add {{[-A|--all]}}`

- Voeg alle bestanden toe in de huidige map:

`git add .`

- Voeg alleen al bijgehouden bestanden toe:

`git add {{[-u|--update]}}`

- Voeg een genegeerd bestand toe:

`git add {{[-f|--force]}} {{pad/naar/bestand}}`

- Interactief delen van bestanden toevoegen:

`git add {{[-p|--patch]}}`

- Interactief delen van een opgegeven bestand toevoegen:

`git add {{[-p|--patch]}} {{pad/naar/bestand}}`

- Interactief een bestand toevoegen:

`git add {{[-i|--interactive]}}`
