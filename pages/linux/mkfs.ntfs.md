# mkfs.ntfs

> Create a NTFS filesystem inside a partition.
> More information: <https://manned.org/mkfs.ntfs>.

- Create a NTFS filesystem inside partition Y on device X:

`sudo mkfs.ntfs {{/dev/sdXY}}`

- Create filesystem with a volume-label:

`sudo mkfs.ntfs {{[-L|--label]}} {{volume_label}} {{/dev/sdXY}}`

- Create filesystem with specific UUID:

`sudo mkfs.ntfs {{[-U|--with-uuid]}} {{UUID}} {{/dev/sdXY}}`
