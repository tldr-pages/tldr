# crane rebase

> Rebase an image onto a new base image.
> More information: <https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane_rebase.md>.

- Rebase image:

`crane rebase`

- New base image to insert:

`crane rebase --new_base {{image_name}}`

- Old base image to remove:

`crane rebase --old_base {{image_name}}`

- Tag to apply to rebased image:

`crane rebase {{[-t|--tag]}} {{tag_name}}`

- Display help:

`crane rebase {{[-h|--help]}}`
