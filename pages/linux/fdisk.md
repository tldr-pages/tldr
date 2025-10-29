# fdisk

> Manage partition tables and partitions on a storage drive.
> See also: `partprobe`.
> More information: <https://manned.org/fdisk>.

- List partitions:

`sudo fdisk {{[-l|--list]}}`

- Start the partition manipulator (interactive mode):

`sudo fdisk {{/dev/sdX}}`

- Open a help [m]enu (in interactive mode):

`<m>`

- View the [p]artition table (in interactive mode):

`<p>`

- Create a [n]ew partition (in interactive mode):

`<n>`

- Select a partition to [d]elete (in interactive mode):

`<d>`

- [w]rite the changes made (in interactive mode):

`<w>`

- Discard the changes made and [q]uit (in interactive mode):

`<q>`
