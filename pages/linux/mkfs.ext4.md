# mkfs.ext4

> Create an ext4 filesystem inside a partition.
> More information: <https://manned.org/mkfs.ext4>.

- Create an ext4 filesystem inside partition Y on device X:

`sudo mkfs.ext4 {{/dev/sdXY}}`

- Create an ext4 filesystem with a volume-label:

`sudo mkfs.ext4 -L {{volume_label}} {{/dev/sdXY}}`

- Create an ext4 filesystem owned by a specific user and group:

`sudo mkfs.ext4 -E root_owner={{uid}}:{{gid}} {{/dev/sdXY}}`
