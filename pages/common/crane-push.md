# crane push

> Push local image contents to a remote registry.
> More information: <https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane_push.md>.

- Push local image to remote registry:

`crane push {{path}} {{image_name}}`

- Display help:

`crane push {{-h|--help}}`

- Path to file with list of published image references:

`crane push {{path}} {{image_name}} {{--image-refs}} {{string}}`

- Push a collection of images as a single index (required if path has multiple images):

`crane push {{path}} {{image_name}} {{--index}}`
