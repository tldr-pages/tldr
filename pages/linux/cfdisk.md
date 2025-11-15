# cfdisk

> Manage partition tables and partitions on a hard disk using a curses UI.
> More information: <https://manned.org/cfdisk>.

- Start the partition manipulator with a specific device:

`sudo cfdisk {{/dev/sdX}}`

- Create a new partition table for a specific device and manage it:

`sudo cfdisk {{[-z|--zero]}} {{/dev/sdX}}`
