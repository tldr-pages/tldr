# systemd-dissect

> Tool for introspecting and interacting with file system OS disk images, specifically Discoverable Disk Images (DDIs).
> More information: <https://www.freedesktop.org/software/systemd/man/latest/systemd-dissect.html>.

- Show general image information about the OS image:

`systemd-dissect {{path/to/image.raw}}`

- Mount an OS image:

`systemd-dissect --mount {{path/to/image.raw}} {{/mnt/image}}`

- Unmount an OS image:

`systemd-dissect --umount {{/mnt/image}}`

- List files in an image:

`systemd-dissect --list {{myimage.raw}}`

- Attach an OS image:

`systemd-dissect --attach {{path/to/image.raw}}`
