# usb-creator

> Create verified bootable USB installers for Linux and BSD systems.
> Downloads are checksum and GPG verified, and disks backing the running system are never writable.
> More information: <https://github.com/Reventlow/usb-creator>.

- Start the interactive wizard (choose desktop/server, a system, and a target device):

`usb-creator`

- List candidate USB devices:

`usb-creator list`

- List all supported systems:

`usb-creator distros`

- Display what "latest" resolves to for a system, including how it will be verified:

`usb-creator info {{arch}}`

- Download and verify an image into the cache without writing it:

`usb-creator download {{fedora}}`

- Write the latest release of a system to a USB device:

`usb-creator write --distro {{debian}} --device {{/dev/sdb}}`

- Write a local image file to a USB device:

`usb-creator write --iso {{path/to/image.iso}} --device {{/dev/sdb}}`

- Update the tool itself (delegates to the package manager where applicable):

`usb-creator update`
