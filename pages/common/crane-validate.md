# crane validate

> Validate that an image is well-formed.
> More information: <https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane_validate.md>.

- Validate an image:

`crane validate`

- Skip downloading/digesting layers:

`crane validate --fast`

- Validate a remote image:

`crane validate --remote {{image_name}}`

- Validate a tarball:

`crane validate --tarball {{path/to/tarball}}`

- Display help:

`crane validate {{[-h|--help]}}`
