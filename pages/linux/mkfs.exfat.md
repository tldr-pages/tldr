# mkfs.exfat

> Creates an exfat filesystem inside a partition.

- Create an exfat filesystem inside partition 1 on device b (`sdb1`):

`mkfs.exfat {{/dev/sdb1}}`

- Create filesystem with a volume-name:

`mkfs.exfat -n {{volume_name}} {{/dev/sdb1}}`

- Create filesystem with a volume-id:

`mkfs.exfat -i {{volume_id}} {{/dev/sdb1}}`
