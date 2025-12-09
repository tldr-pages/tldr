# crane validate

> Valideer of een image goed is gevormd.
> Meer informatie: <https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane_validate.md>.

- Valideer een image:

`crane validate`

- Sla het downloaden/digiteren van lagen over:

`crane validate --fast`

- Naam van de remote image om te valideren:

`crane validate --remote {{image_naam}}`

- Pad naar tarball om te valideren:

`crane validate --tarball {{pad/naar/tarball}}`

- Toon de help:

`crane validate {{[-h|--help]}}`
