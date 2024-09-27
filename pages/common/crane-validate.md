# crane validate

> Validate that an image is well-formed.
> More information: <https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane_validate.md>.

- Validate an image:

`crane validate`

- Skip downloading/digesting layers:

`crane validate {{--fast}}`

- Display help:

`crane validate {{-h|--help}}`

- Name of remote image to validate:

`crane validate {{--remote}} {{string}}`

- Path to tarball to validate:

`crane validate {{--tarball}} {{string}}`
