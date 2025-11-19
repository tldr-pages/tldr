# mke2fs

> Create a Linux filesystem inside a partition.
> More information: <https://manned.org/mke2fs>.

- Create an ext2 filesystem on a partition:

`sudo mke2fs -t ext2 {{/dev/sdXY}}`

- Create an ext3 filesystem on a partition:

`sudo mke2fs -t ext3 {{/dev/sdXY}}`

- Create an ext4 filesystem on a partition:

`sudo mke2fs -t {{ext4}} {{/dev/sdXY}}`
