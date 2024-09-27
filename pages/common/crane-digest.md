# crane digest

> Get the digest of an image.
> More information: <https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane_digest.md>.

- Get the digest of an image:

`crane digest {{image_name}}`

- Print the full image reference by digest:

`crane digest {{image_name}} {{--full-ref}}`

- Display help:

`crane digest {{image_name}} {{-h|--help}}`

- Specify path to tarball containing the image:

`crane digest {{image_name}} {{--tarball}} {{string}}`
