# crane append

> Push een image gebaseerd op een (optionele) basisimage.
> Voegt lagen toe met de inhoud van de opgegeven tarballs.
> Meer informatie: <https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane_append.md>.

- Push een image gebaseerd op een basisimage:

`crane append {{[-b|--base]}} {{image_naam}}`

- Push een image met een toegevoegde laag vanuit een tarball:

`crane append {{[-f|--new_layer]}} {{layer_naam1 layer_naam2 ...}}`

- Push een image met een toegevoegde laag met een nieuwe tag:

`crane append {{[-t|--new_tag]}} {{tag_naam}}`

- Push de resulterende image naar een nieuwe tarball:

`crane append {{[-o|--output]}} {{pad/naar/tarball}}`

- Gebruik een lege basisimage van het type OCI-media in plaats van Docker:

`crane append --oci-empty-base`

- Annoteer de resulterende image als gebaseerd op de basisimage:

`crane append --set-base-image-annotations`

- Toon de help:

`crane append {{[-h|--help]}}`
