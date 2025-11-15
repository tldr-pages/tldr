# crane flatten

> Flatten an image's layers into a single layer.
> Pushes digest to original image repository if no tags are specified.
> More information: <https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane_digest.md>.

- Flatten an image:

`crane flatten`

- Apply new tag to flattened image:

`crane flatten {{[-t|--tag]}} {{tag_name}}`

- Display help:

`crane flatten {{[-h|--help]}}`
