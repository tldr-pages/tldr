# growpart

> Extend a partition in a disk or disk image to fill available space.
> More information: <https://github.com/canonical/cloud-utils>.

- Extend partition `n` from `sdX` to fill empty space until end of disk or beginning of next partition:

`growpart {{/dev/sdX}} {{n}}`

- Simulate growing partition `n` in a disk image, showing what modifications would be made:

`growpart {{[-N|--dry-run]}} /{{path/to/disk.img}} {{n}}`
