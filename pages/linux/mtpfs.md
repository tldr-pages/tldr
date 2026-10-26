# mtpfs

> Mount the first detected MTP device (such as an Android phone) as a FUSE filesystem.
> The program always opens raw device 0 after it lists the devices it found.
> See also: `fusermount`, `simple-mtpfs`, `go-mtpfs`.
> More information: <https://github.com/cjd/mtpfs>.

- List detected devices and mount the first one:

`mtpfs {{path/to/mount_point}}`

- Mount the device so other users can access it:

`mtpfs -o allow_other {{path/to/mount_point}}`

- Unmount the filesystem:

`fusermount -u {{path/to/mount_point}}`
