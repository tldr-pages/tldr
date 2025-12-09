# crane append

> Push an image based on an (optional) base image.
> Appends layers containing the contents of the provided tarballs.
> More information: <https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane_append.md>.

- Push image based on a base image:

`crane append {{[-b|--base]}} {{image_name}}`

- Push image with appended layer from tarball:

`crane append {{[-f|--new_layer]}} {{layer_name1 layer_name2 ...}}`

- Push image with appended layer with new tag:

`crane append {{[-t|--new_tag]}} {{tag_name}}`

- Push resulting image to new tarball:

`crane append {{[-o|--output]}} {{path/to/tarball}}`

- Use empty base image of type OCI media instead of Docker:

`crane append --oci-empty-base`

- Annotate resulting image as being based on the base image:

`crane append --set-base-image-annotations`

- Display help:

`crane append {{[-h|--help]}}`
