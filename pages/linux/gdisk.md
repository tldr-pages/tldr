# gdisk

> GPT (GUID Partition Table) disk partitioning tool.
> See also: `cfdisk`, `fdisk`, `parted`.
> More information: <https://manned.org/gdisk>.

- Start partition manipulator for a specific disk:

`sudo gdisk {{/dev/sdX}}`

- Display partition table without entering interactive mode:

`sudo gdisk -l {{/dev/sdX}}`
