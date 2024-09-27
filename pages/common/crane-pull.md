# crane pull

> Pull remote images by reference and store their contents locally.
> More information: <https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane_pull.md>.

- Pull remote image:

`crane pull {{image_name}} {{tarball}}`

- Preserve image reference used to pull as an annotation when used with --format=oci:

`crane pull {{image_name}} {{tarball}} {{--annoate-ref}}`

- Path to cache image layers:

`crane pull {{image_name}} {{tarball}} {{-c|--cache_path}} {{string}}`

- Format in which to save images (default 'tarball'):

`crane pull {{image_name}} {{tarball}} {{-format}} {{string}}`

- Display help:

`crane pull {{-h|--help}}`
