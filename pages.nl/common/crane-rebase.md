# crane rebase

> Rebase een image op een nieuw basisimage.
> Meer informatie: <https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane_rebase.md>.

- Rebase image:

`crane rebase`

- Specificeer een nieuwe basisimage om in te voegen:

`crane rebase --new_base {{image_naam}}`

- Specificeer een oude basisimage om te verwijderen:

`crane rebase --old_base {{image_naam}}`

- Pas een tag toe op de gerebaseerde image:

`crane rebase {{[-t|--tag]}} {{tag_naam}}`

- Toon de help:

`crane rebase {{[-h|--help]}}`
