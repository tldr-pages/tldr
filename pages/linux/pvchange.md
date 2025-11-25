# pvchange

> Change attributes of physical volume(s).
> More information: <https://manned.org/pvchange>.

- Allow allocation on a physical volume:

`sudo pvchange {{[-x|--allocatable]}} y {{/dev/sdXN}}`

- Disallow allocation on a physical volume:

`sudo pvchange {{[-x|--allocatable]}} n {{/dev/sdXN}}`

- Ignore metadata areas on a physical volume:

`sudo pvchange --metadataignore y {{/dev/sdXN}}`

- Stop ignoring metadata areas on a physical volume:

`sudo pvchange --metadataignore n {{/dev/sdXN}}`

- Add a tag to a physical volume:

`sudo pvchange --addtag {{tag}} {{/dev/sdXN}}`

- Generate a new UUID for a physical volume (use with care):

`sudo pvchange --uuid {{/dev/sdXN}}`

- Change all visible physical volumes (combine with other options such as allocatable):

`sudo pvchange {{[-a|--all]}} {{[-x|--allocatable]}} y`
