# pmount

> Mount arbitrary hotpluggable devices as normal user.

- Mount a device below /media/ (using device as mount point):

`pmount {{path/to/device}}`

- Mount a device with specified file system type to /media/label:

`pmount -t {{filesystem}} {{path/to/device}} {{label}}`

- Show all mounted removable devices:

`pmount`
