# growpart

> Extend a partition in a disk or disk image to fill available space.
> More information: <https://github.com/canonical/cloud-utils>.

- Extend partition `n` from `sdX` to fill empty space until end of disk or beginning of next partition:

`growpart {{/dev/sdX}} {{n}}`

- Show what modifications would be made when growing partition `n` in a disk image:

`growpart {{[-N|--dry-run]}} {{/path/to/disk.img}} {{n}}`
