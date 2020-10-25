# udisktctl

> A command-line program used to interact with the udisksd daemon process.
> More information: <https://manpages.ubuntu.com/manpages/focal/man1/udisksctl.1.html>.

- Show high-level information about disk drives and block devices:

`udisksctl status`

- Show detailed information about a device:

`udisksctl info --block-device {{/dev/device_name}}`

- Mount a device and prints the mount point:

`udisksctl mount --block-device {{/dev/device_name}}`

- Unmount a device:

`udisksctl unmount --block-device {{/dev/device_name}}`

- Monitor the daemon for events:

`udisksctl monitor`
