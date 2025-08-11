# umount

> Unlink a filesystem from its mount point, making it no longer accessible.
> A filesystem cannot be unmounted when it is busy.
> More information: <https://manned.org/umount.8>.

- Unmount a filesystem, by passing the path to the source it is mounted from:

`sudo umount {{path/to/device_file}}`

- Unmount a filesystem, by passing the path to the target where it is mounted:

`sudo umount {{path/to/mounted_directory}}`

- When an unmount fails, try to remount the filesystem read-only:

`sudo umount {{[-r|--read-only]}} {{path/to/mounted_directory}}`

- Recursively unmount each specified directory:

`sudo umount {{[-R|--recursive]}} {{path/to/mounted_directory}}`

- Unmount all mounted filesystems (except the `proc` filesystem):

`sudo umount {{[-a|--all]}}`
