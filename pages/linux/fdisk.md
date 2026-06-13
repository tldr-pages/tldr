# fdisk

> Manage partition tables and partitions on a storage drive.
> See also: `partprobe`, `parted`, `cfdisk`.
> More information: <https://manned.org/fdisk>.

- List partitions:

`sudo fdisk {{[-l|--list]}}`

- Start the interactive partition manipulator:

`sudo fdisk {{/dev/sdX}}`

- Open a help [m]enu:

`<m>`

- View the [p]artition table:

`<p>`

- Create a [n]ew partition:

`<n>`

- Select a partition to [d]elete:

`<d>`

- [w]rite the changes made:

`<w>`

- Discard the changes made and [q]uit:

`<q>`
