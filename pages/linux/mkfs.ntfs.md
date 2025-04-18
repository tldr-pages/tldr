# mkfs.ntfs

> Create a NTFS filesystem inside a partition.
> More information: <https://manned.org/mkfs.ntfs>.

- Create a NTFS filesystem inside partition Y on device X:

`mkfs.ntfs {{/dev/sdXY}}`

- Create filesystem with a volume-label:

`mkfs.ntfs -L {{volume_label}} {{/dev/sdXY}}`

- Create filesystem with specific UUID:

`mkfs.ntfs -U {{UUID}} {{/dev/sdXY}}`
