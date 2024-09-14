# mkfs.xfs

> Create an xfs filesystem inside a partition.
> More information: <https://manned.org/mkfs.ext4>.

- Create an xfs filesystem inside partition 1 on device b (`sdb1`):

`sudo mkfs.xfs {{/dev/sdb1}}`

- Create an xfs filesystem with a volume-label:

`sudo mkfs.xfs -L {{volume_label}} {{/dev/sdb1}}`
