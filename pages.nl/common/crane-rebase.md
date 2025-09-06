# crane rebase

> Rebase een image op een nieuw basisimage.
> Meer informatie: <https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane_rebase.md>.

- Rebase image:

`crane rebase`

- Nieuwe basisimage om in te voegen:

`crane rebase --new_base {{image_naam}}`

- Oude basisimage om te verwijderen:

`crane rebase --old_base {{image_naam}}`

- Tag om toe te passen op de gerebaseerde image:

`crane rebase {{[-t|--tag]}} {{tag_naam}}`

- Toon de help:

`crane rebase {{[-h|--help]}}`
