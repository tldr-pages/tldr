# git tag

> Creëer, toon, verwijder of verifieer tags.
> Een tag is een statische verwijzing naar een commit.
> Meer informatie: <https://git-scm.com/docs/git-tag>.

- Toon alle tags:

`git tag`

- Maak een tag aan met de opgegeven naam die verwijst naar de huidige commit:

`git tag {{tag_naam}}`

- Maak een tag aan met de opgegeven naam die verwijst naar een gegeven commit:

`git tag {{tag_naam}} {{commit}}`

- Maak een geannoteerde tag aan met het opgegeven bericht:

`git tag {{tag_naam}} {{[-m|--message]}} {{tag_bericht}}`

- Verwijder de tag met de opgegeven naam:

`git tag {{[-d|--delete]}} {{tag_naam}}`

- Haal geüpdatete tags op van de remote:

`git fetch {{[-t|--tags]}}`

- Push een tag naar de remote:

`git push origin tag {{tag_naam}}`

- Toon alle tags die een bepaalde commit bevatten (HEAD indien niet gespecificeerd):

`git tag --contains {{commit}}`
