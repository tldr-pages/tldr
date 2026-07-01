# aft-mtp-mount

> Mount MTP devices using FUSE.
> More information: <https://manned.org/aft-mtp-mount>.

- Mount an MTP device to a directory:

`aft-mtp-mount {{path/to/mountpoint}}`

- Mount a specific device to a directory:

`aft-mtp-mount -D {{device_name}} {{path/to/mountpoint}}`

- Display debug output:

`aft-mtp-mount {{[-d|-o debug]}}`

- Reset the device before mounting:

`aft-mtp-mount -R {{path/to/mountpoint}}`

- Do not claim the USB interface:

`aft-mtp-mount -C {{path/to/mountpoint}}`

- Enable verbose output:

`aft-mtp-mount -v`

- Display help:

`aft-mtp-mount -h`
