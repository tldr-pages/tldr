# mkfs.xfs

> Create an XFS filesystem inside a partition.
> More information: <https://manned.org/mkfs.xfs>.

- Create an XFS filesystem inside partition 1 on a device (`X`):

`sudo mkfs.xfs {{/dev/sdXY}}`

- Create an XFS filesystem with a volume label:

`sudo mkfs.xfs -L {{volume_label}} {{/dev/sdXY}}`
