# mkfs.xfs

> Create an xfs filesystem inside a partition.
> More information: <https://manned.org/mkfs.xfs>.

- Create an xfs filesystem inside partition 1 on a device (`X`):

`sudo mkfs.xfs {{/dev/sdX1}}`

- Create an xfs filesystem with a volume-label:

`sudo mkfs.xfs -L {{volume_label}} {{/dev/sdX1}}`
