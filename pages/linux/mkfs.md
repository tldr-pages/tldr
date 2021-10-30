# mkfs

> Build a Linux filesystem on a hard disk partition.
> This command is deprecated in favor of filesystem specific mkfs.<type> utils.
> More information: <https://manned.org/mkfs>.

- Build a Linux ext2 filesystem on a partition:

`mkfs {{path/to/partition}}`

- Build a filesystem of a specified type:

`mkfs -t {{ext4}} {{path/to/partition}}`

- Build a filesystem of a specified type and check for bad blocks:

`mkfs -c -t {{ntfs}} {{path/to/partition}}`
