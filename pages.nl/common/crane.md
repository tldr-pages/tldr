# crane

> Hulpmiddel voor het beheren van containerimages.
> Sommige subcommando's zoals `pull`, `push`, `copy`, etc. hebben hun eigen documentatie.
> Meer informatie: <https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane.md/>.

- Log in op een register:

`crane auth login {{register}} {{[-u|--username]}} {{gebruiker}} {{[-p|--password]}} {{wachtwoord}}`

- Toon de repositories in een register:

`crane catalog {{register}} --full-ref`

- Toon de tags in een repository:

`crane ls {{repository}} {{[-o|--omit-digest-tags]}}`

- Haal externe images op door middel van referentie en sla de inhoud ervan lokaal op:

`crane pull {{image}} {{tarball}}`

- Push lokale inhoud van images naar een externe repository:

`crane push {{pad/naar/map_of_tarball}} {{image}}`

- Tag efficiënt een externe image:

`crane tag {{image}} {{tag}}`

- Kopieer efficiënt een externe image, waarbij de digest-waarde behouden blijft:

`crane {{[cp|copy]}} {{bron}} {{doel}} {{[-a|--all-tags]}}`

- Verwijder een image-referentie van zijn register:

`crane delete {{image}}`
