# woeusb

> Windows media creation tool.
> More information: <https://github.com/WoeUSB/WoeUSB>.

- Format a USB then create a bootable Windows installation drive:

`woeusb --device {{path/to/windows.iso}} {{/dev/sdX}}`

- Copy Windows files to an existing partition of a USB storage device and make it bootable, without erasing the current data:

`woeusb --partition {{path/to/windows.iso}} {{/dev/sdXN}}`
