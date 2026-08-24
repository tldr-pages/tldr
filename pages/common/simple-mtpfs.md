# simple-mtpfs

> Mount MTP devices (like Android phones) as a filesystem using FUSE.
> More information: <https://manned.org/simple-mtpfs>.

- List available MTP devices:

`simple-mtpfs {{[-l|--list-devices]}}`

- Mount a device to a directory:

`simple-mtpfs {{mount_point}}`

- Mount a specific device to a directory (useful when multiple devices are connected):

`simple-mtpfs --device {{number}} {{mount_point}}`

- Unmount the filesystem:

`umount {{mount_point}}`
