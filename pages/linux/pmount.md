# pmount

> Mount arbitrary hotpluggable devices as normal user.
> More information: <https://linux.die.net/man/1/pmount>.

- Mount a device below /media/ (using device as mount point):

`pmount {{path/to/device}}`

- Mount a device with a specific filesystem type to `/media/label`:

`pmount --type {{filesystem}} {{path/to/device}} {{label}}`

- Display all mounted removable devices:

`pmount`
