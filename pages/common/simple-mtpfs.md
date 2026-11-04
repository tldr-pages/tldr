# simple-mtpfs

> Mount MTP devices (like Android phones) as a filesystem using FUSE.
> More information: <https://manned.org/simple-mtpfs>.

- List available MTP devices:

`simple-mtpfs {{[-l|--list-devices]}}`

- Mount a device to a directory:

`simple-mtpfs {{path/to/mount_point}}`

- Mount a specific device to a directory (useful when multiple devices are connected):

`simple-mtpfs --device {{number}} {{path/to/mount_point}}`

- Unmount the filesystem:

`umount {{path/to/mount_point}}`
