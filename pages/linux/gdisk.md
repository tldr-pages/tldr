# gdisk

> GPT (GUID Partition Table) disk partitioning tool.
> See also: `cfdisk`, `fdisk`, `parted`.
> More information: <https://manned.org/gdisk>.

- Start partition manipulator for a specific disk:

`sudo gdisk {{/dev/sdX}}`

- Display partition table without entering interactive mode:

`sudo gdisk -l {{/dev/sdX}}`

- Backup partition table to a file before making changes:

`sudo gdisk -b {{path/to/backup_file}} {{/dev/sdX}}`

- Restore partition table from backup file:

`sudo gdisk -l {{path/to/backup_file}} {{/dev/sdX}}`

- Convert MBR partition table to GPT without data loss:

`sudo gdisk -m {{/dev/sdX}}`

- Display help:

`sudo gdisk -? {{/dev/sdX}}`
