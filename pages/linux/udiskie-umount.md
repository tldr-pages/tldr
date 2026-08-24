# udiskie-umount

> Manually unmount devices using udiskie.
> See also: `udiskie`, `udiskie-mount`.
> More information: <https://github.com/coldfix/udiskie/wiki/Usage>.

- Unmount a mounted device:

`udiskie-umount {{path/to/mount}}`

- Unmount and power down a USB device:

`udiskie-umount --detach {{path/to/mount}}`

- Eject an optical drive:

`udiskie-umount --eject {{path/to/mount}}`

- Display help:

`udiskie-umount --help`
