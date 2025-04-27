# mkfs.exfat

> Create an exfat filesystem inside a partition.
> More information: <https://manned.org/mkfs.exfat>.

- Create an exfat filesystem inside partition Y on device X:

`mkfs.exfat {{/dev/sdXY}}`

- Create filesystem with a volume-name:

`mkfs.exfat {{[-L|--volume-label]}} {{volume_name}} {{/dev/sdXY}}`

- Create filesystem with a volume-id:

`mkfs.exfat {{[-U|--volume-guid]}} {{volume_id}} {{/dev/sdXY}}`
