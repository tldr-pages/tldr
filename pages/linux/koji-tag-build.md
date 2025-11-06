# koji tag-build

> Apply a tag to one or more builds.
> More information: <https://docs.pagure.org/koji>.

- Apply a tag to one or more builds:

`koji tag-build {{tag}} {{NVR1 NVR2 ...}}`

- Do't wait on task:

`koji tag-build --nowait {{tag}} {{NVR1 NVR2 ...}}`

- Force operation:

`koji tag-build --force {{tag}} {{NVR1 NVR2 ...}}`

- Display help:

`koji tag-build --help`
