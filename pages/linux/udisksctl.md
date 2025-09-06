# udisksctl

> Interact with `udisksd` to query and manipulate storage devices.
> More information: <https://storaged.org/doc/udisks2-api/latest/udisksctl.1.html>.

- Show high-level information about disk drives and block devices:

`udisksctl status`

- Show detailed information about a device:

`udisksctl info {{[-b|--block-device]}} {{/dev/sdX}}`

- Show detailed information about a device partition:

`udisksctl info {{[-b|--block-device]}} {{/dev/sdXN}}`

- Mount a device partition and prints the mount point:

`udisksctl mount {{[-b|--block-device]}} {{/dev/sdXN}}`

- Unmount a device partition:

`udisksctl unmount {{[-b|--block-device]}} {{/dev/sdXN}}`

- Power off a device to safely remove it:

`udisksctl power-off {{[-b|--block-device]}} {{/dev/sdX}}`

- Monitor the daemon for events:

`udisksctl monitor`
