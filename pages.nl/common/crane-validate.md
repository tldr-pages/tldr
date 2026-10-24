# crane validate

> Valideer of een image goed is gevormd.
> Meer informatie: <https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane_validate.md>.

- Valideer een image:

`crane validate`

- Sla het downloaden/digesten van lagen over:

`crane validate --fast`

- Valideer een remote image:

`crane validate --remote {{image_naam}}`

- Valideer een tarball:

`crane validate --tarball {{pad/naar/tarball}}`

- Toon de help:

`crane validate {{[-h|--help]}}`
