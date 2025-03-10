# crane digest

> Verkrijg de digest van een image.
> Meer informatie: <https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane_digest.md>.

- Verkrijg de digest van een image:

`crane digest {{image_naam}}`

- Print de volledige image-referentie op basis van de digest:

`crane digest {{image_naam}} --full-ref`

- Specificeer het pad naar de tarball met de image:

`crane digest {{image_naam}} --tarball {{pad/naar/tarball}}`

- Toon de help:

`crane digest {{[-h|--help]}}`
