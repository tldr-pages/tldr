# mkfs

> Build a Linux filesystem on a hard disk partition.
> This mkfs frontend is deprecated in favour of filesystem specific mkfs.<type> utils.

- Build a Linux ext2 filesystem on a partition:

`mkfs {{path/to/partition}}`

- Build a filesystem of a specified type:

`mkfs -t {{filesystem_type}} {{path/to/partition}}`

- Build a filesystem of a specified type and check for bad blocks:

`mkfs -c -t {{filesystem_type}} {{path/to/partition}}`
