# mkfs.vfat

> Creates an MS-DOS filesystem inside a partition.
> More information: <https://manned.org/mkfs.vfat>.

- Create a vfat filesystem inside partition 1 on device b (`sdb1`):

`mkfs.vfat {{/dev/sdb1}}`

- Create filesystem with a volume-name:

`mkfs.vfat -n {{volume_name}} {{/dev/sdb1}}`

- Create filesystem with a volume-id:

`mkfs.vfat -i {{volume_id}} {{/dev/sdb1}}`

- Use 5 instead of 2 file allocation tables:

`mkfs.vfat -f 5 {{/dev/sdb1}}`
