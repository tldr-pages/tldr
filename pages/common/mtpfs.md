# mtpfs

> Mount MTP devices (like MP3 players, digital cameras and Android phones) as a filesystem using FUSE.
> More information: <https://manned.org/mtpfs>.

- Mount an MTP device to a directory:

`mtpfs {{mount_point}}`

- Mount with FUSE options (e.g. allow other users to access the mounted filesystem):

`mtpfs {{mount_point}} {{[-o|--option]}} {{allow_other}}`

- Unmount the device:

`fusermount {{[-u]}} {{mount_point}}`
