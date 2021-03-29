# cfdisk

> A program for managing partition tables and partitions on a hard disk using a curses UI.
> More information: <https://man.archlinux.org/man/cfdisk.8>.

- Start the partition manipulator with a specific device:

`cfdisk {{/dev/sdX}}`

- Create a new partition table for a specific device and manage it:

`cfdisk --zero {{/dev/sdX}}`
