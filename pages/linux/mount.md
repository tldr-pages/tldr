# mount

> Get access to an entire filesystem in one directory.
> More information: <https://manned.org/mount.8>.

- Show all mounted filesystems:

`mount`

- Mount a device to a directory:

`mount {{path/to/device_file}} {{path/to/target_directory}}`

- Create a specific directory if it does not exist and mount a device to it:

`mount {{[-m|--mkdir]}} {{path/to/device_file}} {{path/to/target_directory}}`

- Mount a device to a directory for a specific user:

`mount {{[-o|--options]}} uid={{user_id}},gid={{group_id}} {{path/to/device_file}} {{path/to/target_directory}}`

- Mount a CD-ROM device (with the filetype ISO9660) to `/cdrom` (readonly):

`mount {{[-t|--types]}} iso9660 {{[-o|--options]}} ro {{/dev/cdrom}} /cdrom`

- Mount all the filesystems defined in `/etc/fstab`:

`mount {{[-a|--all]}}`

- Mount a specific filesystem described in `/etc/fstab` (e.g. `/dev/sda1 /path/to/mount_point ext2 defaults 0 2`):

`mount {{path/to/mount_point}}`

- Mount a directory to another directory:

`mount {{[-B|--bind]}} {{path/to/old_directory}} {{path/to/new_directory}}`
