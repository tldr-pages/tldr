# git add

> Voegt gewijzigde bestanden toe aan de index.
> Meer informatie: <https://git-scm.com/docs/git-add>.

- Voeg een bestand toe aan de index:

`git add {{pad/naar/bestand}}`

- Voeg alle bestanden toe (bijgehouden en niet bijgehouden):

`git add {{[-A|--all]}}`

- Voeg alle bestanden toe in de huidige map:

`git add .`

- Voeg alleen al bijgehouden bestanden toe:

`git add {{[-u|--update]}}`

- Voeg ook genegeerde bestanden toe:

`git add {{[-f|--force]}}`

- Interactief delen van bestanden toevoegen:

`git add {{[-p|--patch]}}`

- Interactief delen van een opgegeven bestand toevoegen:

`git add {{[-p|--patch]}} {{pad/naar/bestand}}`

- Interactief een bestand toevoegen:

`git add {{[-i|--interactive]}}`
