# simple-mtpfs

> Mount MTP devices (like Android phones) as a filesystem using FUSE.
> More information: <https://github.com/phatina/simple-mtpfs>.

- List available MTP devices:

`simple-mtpfs -l`

- Mount device to a directory:

`simple-mtpfs {{mount_point}}`

- Unmount the filesystem:

`fusermount -u {{mount_point}}`
