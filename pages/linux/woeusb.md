# WoeUSB

> Microsoft Windows® USB installation media creator for GNU+Linux.
> More information: <https://github.com/WoeUSB/WoeUSB>.

- Completely WIPE the entire USB storage device, then build a bootable Windows USB device from scratch:

`woeusb --device {{source media path}} {{device}}`

- Copy Windows files to an existing partition of a USB storage device and make it bootable. This allows files to coexist as long as no filename conflict exists:

`woeusb --partition {{source media path}} {{partition}}`
