# crane digest

> Get the digest of an image.
> More information: <https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane_digest.md>.

- Get the digest of an image:

`crane digest {{image_name}}`

- Print the full image reference by digest:

`crane digest {{image_name}} --full-ref`

- Specify path to tarball containing the image:

`crane digest {{image_name}} --tarball {{path/to/tarball}}`

- Display help:

`crane digest {{[-h|--help]}}`
