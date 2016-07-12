# umount

> Revokes access to an entire filesystem mounted to a directory.
> A filesystem cannot be unmounted when it is busy.

- Unmount a filesystem:

`umount {{path/to/device_file}}`

- OR:

`umount {{path/to/mounted_directory}}`

- Unmount all mounted filesystems (dangerous!):

`umount -a`
