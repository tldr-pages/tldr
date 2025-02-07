# growpart

> Extend a partition in a disk or disk image to fill available space.
> More information: <https://github.com/canonical/cloud-utils>.

- Extend partition 3 in /dev/sdb to fill empty space until end of disk or beginning of next partition:

`growpart /dev/sdb 3`

- Show what modifications would be made when growing partition 2 in a disk image:

`growpart --dry-run /path/to/mydisk.img 2`
