# lsblk

> List information about block devices.
> More information: <https://manned.org/lsblk>.

- List all storage devices in a tree-like format:

`lsblk`

- Show empty devices:

`lsblk --all`

- Display sizes in bytes instead of human-readable format:

`lsblk --bytes`

- Show filesystem information:

`lsblk --fs`

- Use ASCII characters for tree formatting:

`lsblk --ascii`

- Show block-device topology information:

`lsblk --topology`

- Exclude specific devices using a comma-separated list of device major numbers:

`lsblk --exclude {{1,7,...}}`

- Sort results by size (new useful example):

`lsblk --sort {{SIZE}}`
