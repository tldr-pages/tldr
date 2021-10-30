# udisksctl

> A command-line program used to interact with the udisksd daemon process.
> More information: <http://storaged.org/doc/udisks2-api/latest/udisksctl.1.html>.

- Show high-level information about disk drives and block devices:

`udisksctl status`

- Show detailed information about a device:

`udisksctl info --block-device {{/dev/sdX}}`

- Show detailed information about a device partition:

`udisksctl info --block-device {{/dev/sdXN}}`

- Mount a device partition and prints the mount point:

`udisksctl mount --block-device {{/dev/sdXN}}`

- Unmount a device partition:

`udisksctl unmount --block-device {{/dev/sdXN}}`

- Monitor the daemon for events:

`udisksctl monitor`
