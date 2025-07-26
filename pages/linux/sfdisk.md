# sfdisk

> Display or manipulate a disk partition table.
> More information: <https://manned.org/sfdisk>.

- Back up the partition layout to a file:

`sudo sfdisk {{[-d|--dump]}} {{path/to/device}} > {{path/to/file.dump}}`

- Restore a partition layout:

`sudo sfdisk {{path/to/device}} < {{path/to/file.dump}}`

- Set the type of a partition:

`sfdisk --part-type {{path/to/device}} {{partition_number}} {{swap}}`

- Delete a partition:

`sfdisk --delete {{path/to/device}} {{partition_number}}`

- Display help:

`sfdisk {{[-h|--help]}}`
