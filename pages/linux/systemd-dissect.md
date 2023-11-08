# systemd-dissect
> Tool for introspecting and interacting with file system OS disk images, specifically Discoverable Disk Images (DDIs).
> More information: <https://www.freedesktop.org/software/systemd/man/latest/systemd-dissect.html>.

- Show general image information about the OS image:

`systemd-dissect {{path/to/image.raw}}`

- Mount an OS image:

`systemd-dissect --mount {{myimage.raw}} {{/mnt/myimage}}`

- Unmount an OS Image:

`systemd-dissect --umount {{/mnt/myimage}}`

- List Files in an Image:

`systemd-dissect --list {{myimage.raw}}`

- Attach an OS Image:

`systemd-dissect --attach {{myimage.raw}}`
