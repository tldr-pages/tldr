# udiskie-umount

> Manually unmount devices using udiskie.
> See also: `udiskie`, `udiskie-mount`
> More information: <https://github.com/coldfix/udiskie/wiki/Usage>.

- Unmount a mounted device:

`udiskie-umount {{/media/username/device}}`

- Unmount and power down a USB device:

`udiskie-umount --detach {{/media/username/device}}`

- Eject an optical drive:

`udiskie-umount --eject {{/media/username/cdrom}}`

- Show help message:

`udiskie-umount --help`
