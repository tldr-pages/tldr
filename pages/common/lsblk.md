# lsblk

> List information about block devices.
> More information: <https://man7.org/linux/man-pages/man8/lsblk.8.html>.

- List all block devices in a tree format:

`lsblk`

- List all block devices including empty ones:

`lsblk -a`

- Show filesystem information:

`lsblk -f`

- Use ASCII characters for tree formatting:

`lsblk -i`

- Show block device owner, group and mode:

`lsblk -m`

- Show device full path:

`lsblk -p`

- Show size in bytes rather than human-readable format:

`lsblk -b`

- Display information about a specific device:

`lsblk {{/dev/sda}}`
