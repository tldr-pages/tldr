# pmount

> Mount arbitrary hotpluggable devices as a normal user.
> More information: <https://manned.org/pmount>.

- Mount a device below `/media/` (using device as mount point):

`pmount {{/dev/to/block/device}}`

- Mount a device with a specific filesystem type to `/media/label`:

`pmount {{[-t|--type]}} {{filesystem}} {{/dev/to/block/device}} {{label}}`

- Mount a CD-ROM (filesystem type ISO9660) in read-only mode:

`pmount {{[-t|--type]}} iso9660 {{[-r|--read-only]}} {{/dev/cdrom}}`

- Mount an NTFS-formatted disk, forcing read-write access:

`pmount {{[-t|--type]}} ntfs {{[-w|--read-write]}} {{/dev/sdX}}`

- Display all mounted removable devices:

`pmount`
