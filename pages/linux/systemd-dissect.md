# systemd-dissect

> Introspect and interact with file system OS disk images, specifically Discoverable Disk Images (DDIs).
> More information: <https://www.freedesktop.org/software/systemd/man/latest/systemd-dissect.html>.

- Show general image information about the OS image:

`systemd-dissect {{path/to/image.raw}}`

- Mount an OS image:

`systemd-dissect --mount {{path/to/image.raw}} {{/mnt/image}}`

- Unmount an OS image:

`systemd-dissect --umount {{/mnt/image}}`

- List files in an image:

`systemd-dissect --list {{path/to/image.raw}}`

- Attach an OS image to an automatically allocated loopback block device and print its path:

`systemd-dissect --attach {{path/to/image.raw}}`

- Detach an OS image from a loopback block device:

`systemd-dissect --detach {{path/to/device}}`
