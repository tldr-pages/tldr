# mkfs

> Build a Linux filesystem on a hard disk partition.
> Note: This command is deprecated, use filesystem specific commands like `mkfs.ext4` instead.
> More information: <https://manned.org/mkfs>.

- Build a Linux ext2 filesystem on a partition:

`sudo mkfs {{/dev/sdXY}}`

- Build a filesystem of a specified type:

`sudo mkfs {{[-t|--type]}} {{ext4}} {{/dev/sdXY}}`

- Build a filesystem of a specified type and check for bad blocks:

`sudo mkfs -c {{[-t|--type]}} {{ntfs}} {{/dev/sdXY}}`
