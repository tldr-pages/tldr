# crane export

> Export filesystem of a container image as a tarball.
> More information: <https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane_digest.md>.

- Write tarball to `stdout`:

`crane export {{image_name}} -`

- Write tarball to file:

`crane export {{image_name}} {{path/to/tarball}}`

- Read image from `stdin`:

`crane export - {{path/to/filename}}`
