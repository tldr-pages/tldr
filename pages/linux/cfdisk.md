# cfdisk

> A program for managing partition tables and partitions on a hard disk using a curses UI.
> More information: <https://linux.die.net/man/8/cfdisk>.

- Open partitioning interface for the disk /dev/sda:

`cfdisk {{/dev/sda}}`

- Create a new partitioning table for the disk /dev/sda and edit it:

`cfdisk --zero {{/dev/sda}}`
