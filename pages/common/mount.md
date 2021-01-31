# mount

> Provides access to an entire filesystem in one directory.

- Show all mounted filesystems:

`mount`

- Mount a device to a directory:

`mount -t {{filesystem_type}} {{path/to/device_file}} {{path/to/target_directory}}`

- Mount a CD-ROM device (with the filetype ISO9660) to `/cdrom` (readonly):

`mount -t {{iso9660}} -o ro {{/dev/cdrom}} {{/cdrom}}`

- Mount all the filesystem defined in `/etc/fstab`:

`mount -a`

- Mount a specific filesystem described in `/etc/fstab` (e.g. `/dev/sda1 /my_drive ext2 defaults 0 2`):

`mount {{/my_drive}}`

- Mount a directory to another directory:

`mount --bind {{path/to/old_dir}} {{path/to/new_dir}}`
