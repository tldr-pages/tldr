# go-mtpfs

> Mount an Android device as an MTP filesystem with FUSE.
> See also: `fusermount`, `simple-mtpfs`.
> More information: <https://github.com/hanwen/go-mtpfs>.

- Mount a device:

`go-mtpfs {{path/to/mount_point}}`

- Allow users other than the owner to access the mount:

`go-mtpfs -allow-other {{path/to/mount_point}}`

- Mount a device whose ID matches a `regex`:

`go-mtpfs -dev "{{regex}}" {{path/to/mount_point}}`

- Mount only storage areas whose names match a `regex`:

`go-mtpfs -storage "{{regex}}" {{path/to/mount_point}}`

- Disable Android MTP extensions (needed on some devices that advertise them but do not implement them):

`go-mtpfs -android=0 {{path/to/mount_point}}`

- Unmount the filesystem:

`fusermount -u {{path/to/mount_point}}`

- Display help:

`go-mtpfs -h`
