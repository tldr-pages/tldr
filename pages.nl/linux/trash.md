# trash

> Beheer de prullenbak.
> Meer informatie: <https://github.com/andreafrancia/trash-cli>.

- Verplaats een bestand naar de prullenbak:

`trash {{pad/naar/bestand}}`

- Toon alle bestanden in de prullenbak:

`trash-list`

- Herstel een bestand uit de prullenbak (interactief):

`trash-restore`

- Leeg de prullenbak:

`trash-empty`

- Verwijder permanent alle bestanden in de prullenbak die ouder zijn dan 10 dagen:

`trash-empty 10`

- Verwijder alle bestanden in de prullenbak die overeenkomen met een specifiek blob-patroon:

`trash-rm "{{*.o}}"`

- Verwijder alle bestanden met een specifieke oorspronkelijke locatie:

`trash-rm /{{pad/naar/bestand_of_map}}`
