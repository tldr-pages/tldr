# sfdisk

> Display or manipulate a disk partition table.
> More information: <https://manned.org/sfdisk>.

- Back up the partition layout to a file:

`sudo sfdisk {{[-d|--dump]}} {{/dev/sdX}} > {{path/to/file.dump}}`

- Restore a partition layout:

`sudo sfdisk < {{path/to/file.dump}} {{/dev/sdX}}`

- Set the type of a partition:

`sfdisk --part-type {{/dev/sdX}} {{partition_number}} {{swap}}`

- Delete a partition:

`sfdisk --delete {{/dev/sdX}} {{partition_number}}`

- Display help:

`sfdisk {{[-h|--help]}}`
