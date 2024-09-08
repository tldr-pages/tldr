# mkfs.ext4

> Create an ext4 filesystem inside a partition.
> More information: <https://manned.org/mkfs.ext4>.

- Create an ext4 filesystem inside partition 1 on device b (`sdb1`):

`sudo mkfs.ext4 {{/dev/sdb1}}`

- Create an ext4 filesystem with a volume-label:

`sudo mkfs.ext4 -L {{volume_label}} {{/dev/sdb1}}`
