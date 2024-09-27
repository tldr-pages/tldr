# crane rebase

> Rebase an image onto a new base image.
> More information: <https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane_rebase.md>.

- Rebase image:

`crane rebase`

- Display help:

`crane rebase {{-h|--help}}`

- New base image to insert:

`crane rebase {{--new_base}} {{string}}`

- Old base image to remove:

`crane rebase {{--old_base}} {{string}}`

- Tag to apply to rebased image:

`crane rebase {{-t|--tag}} {{string}}`
