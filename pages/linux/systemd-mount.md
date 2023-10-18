# systemd-mount

> Establish and destroy transient mount or auto-mount points.
> More information: <https://www.freedesktop.org/software/systemd/man/systemd-mount.html>.

- Mount a file system (image or block device) at `/run/media/system/LABEL` where LABEL is the filesystem label or the device name if there is no label:

`systemd-mount {{path/to/file_or_device}}`

- Mount a file system (image or block device) at a specific location:

`systemd-mount {{path/to/file_or_device}} {{path/to/mount_point}}`

- Show a list of all local, known block devices with file systems that may be mounted:

`systemd-mount --list`

- Create an automount point that mounts the actual file system at the time of first access:

`systemd-mount --automount=yes {{path/to/file_or_device}}`

- Unmount one or more devices:

`systemd-mount --umount {{path/to/mount_point_or_device1}} {{path/to/mount_point_or_device2}}`

- Mount a file system (image or block device) with a specific file system type:

`systemd-mount --type={{file_system_type}} {{path/to/file_or_device}} {{path/to/mount_point}}`

- Mount a file system (image or block device) with additional mount options:

`systemd-mount --options={{mount_options}} {{path/to/file_or_device}} {{path/to/mount_point}}`
