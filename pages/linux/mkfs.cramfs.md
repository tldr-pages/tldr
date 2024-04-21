# mkfs.cramfs

> Create a ROM filesystem inside a partition.
> More information: <https://manned.org/mkfs.cramfs>.

- Create a ROM filesystem inside partition 1 on device b (`sdb1`):

`mkfs.cramfs {{/dev/sdb1}}`

- Create a ROM filesystem with a volume-name:

`mkfs.cramfs -n {{volume_name}} {{/dev/sdb1}}`
