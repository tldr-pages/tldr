# aft-mtp-mount

> Mount MTP (Media Transfer Protocol) devices to the local filesystem using FUSE.
> More information: <https://manned.org/aft-mtp-mount>.

- Mount an MTP device to a directory:

`aft-mtp-mount {{path/to/mount_point}}`

- Mount a specific device to a directory:

`aft-mtp-mount -D {{device_name}} {{path/to/mount_point}}`

- Reset the device before mounting:

`aft-mtp-mount -R {{path/to/mount_point}}`

- Mount a device without claiming the USB interface:

`aft-mtp-mount -C {{path/to/mount_point}}`

- Mount a device and display debug output:

`aft-mtp-mount -d {{path/to/mount_point}}`

- Display help:

`aft-mtp-mount {{[-h|--help]}}`
