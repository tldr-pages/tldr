# woeusb

> Windows media creation tool.
> More information: <https://manned.org/woeusb>.

- Format a USB then create a bootable Windows installation drive:

`woeusb {{[-d|--device]}} {{path/to/windows.iso}} {{/dev/sdX}}`

- Copy Windows files to an existing partition of a USB storage device and make it bootable, without erasing the current data:

`woeusb {{[-p|--partition]}} {{path/to/windows.iso}} {{/dev/sdXN}}`
