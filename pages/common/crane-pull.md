# crane pull

> Pull remote images by reference and store their contents locally.
> More information: <https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane_pull.md>.

- Pull remote image:

`crane pull {{image_name}} {{path/to/tarball}}`

- Preserve image reference used to pull as an annotation when used with `--format=oci`:

`crane pull {{image_name}} {{path/to/tarball}} --annotate-ref`

- Cache image layers in a specific directory:

`crane pull {{image_name}} {{path/to/tarball}} {{[-c|--cache_path]}} {{path/to/cache}}`

- Specify the format in which to save images (default `tarball`):

`crane pull {{image_name}} {{path/to/tarball}} {{-format}} {{format_name}}`

- Display help:

`crane pull {{[-h|--help]}}`
