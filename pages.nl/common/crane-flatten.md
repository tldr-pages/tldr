# crane flatten

> Flatten de lagen van een image tot een enkele laag.
> Push de digest naar de oorspronkelijke image-repository als er geen tags zijn opgegeven.
> Meer informatie: <https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane_digest.md>.

- Flatten een image:

`crane flatten`

- Pas een nieuwe tag toe op de geflatteerde image:

`crane flatten {{[-t|--tag]}} {{tag_naam}}`

- Toon de help:

`crane flatten {{[-h|--help]}}`
