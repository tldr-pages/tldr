# sgdisk

> Create and modify partition tables on disks that use the GUID Partition Table (GPT) format.
> This tool is part of the `gdisk` family of utilities.
> More information: <https://manpages.org/sgdisk>.

- Display the current GPT partition table of a device:

`sgdisk -p {{/dev/sdX}}`

- Create a new partition with a specified number, start sector, and end sector:

`sgdisk -n {{1}}:{{start_sector}}:{{end_sector}} {{/dev/sdX}}`

- Delete a specific partition:

`sgdisk -d {{1}} {{/dev/sdX}}`

- Back up the entire GPT partition table to a file:

`sgdisk -b {{backup.img}} {{/dev/sdX}}`

- Restore the GPT partition table from a backup file:

`sgdisk -l {{backup.img}} {{/dev/sdX}}`

