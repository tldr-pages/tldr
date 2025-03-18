# crane validate

> Validate that an image is well-formed.
> More information: <https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane_validate.md>.

- Validate an image:

`crane validate`

- Skip downloading/digesting layers:

`crane validate --fast`

- Name of remote image to validate:

`crane validate --remote {{image_name}}`

- Path to tarball to validate:

`crane validate --tarball {{path/to/tarball}}`

- Display help:

`crane validate {{[-h|--help]}}`
