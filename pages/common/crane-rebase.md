# crane rebase

> Rebase an image onto a new base image.
> More information: <https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane_rebase.md>.

- Rebase image:

`crane rebase`

- Specify a new base image to insert:

`crane rebase --new_base {{image_name}}`

- Specify an old base image to remove:

`crane rebase --old_base {{image_name}}`

- Apply a tag to the rebased image:

`crane rebase {{[-t|--tag]}} {{tag_name}}`

- Display help:

`crane rebase {{[-h|--help]}}`
