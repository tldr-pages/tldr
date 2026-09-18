# go-mtpfs

> Mount MTP devices (like Android phones) as a filesystem using FUSE, exposing all storage areas of the device.
> More information: <https://github.com/hanwen/go-mtpfs>.

- Mount a device to a directory:

`go-mtpfs {{mount_point}}`

- Mount allowing other users to access the mounted filesystem:

`go-mtpfs {{[-allow-other]}} {{mount_point}}`

- Mount a specific device when several are connected:

`go-mtpfs {{[-dev]}} {{regex}} {{mount_point}}`

- Mount only the storage areas matching a `regex`:

`go-mtpfs {{[-storage]}} {{regex}} {{mount_point}}`

- Unmount the device:

`fusermount {{[-u]}} {{mount_point}}`
