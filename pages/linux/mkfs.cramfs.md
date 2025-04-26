# mkfs.cramfs

> Create a ROM filesystem inside a partition.
> More information: <https://manned.org/mkfs.cramfs>.

- Create a ROM filesystem inside partition Y on device X:

`mkfs.cramfs {{/dev/sdXY}}`

- Create a ROM filesystem with a volume-name:

`mkfs.cramfs -n {{volume_name}} {{/dev/sdXY}}`
