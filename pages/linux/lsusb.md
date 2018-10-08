# lsusb

> Display information about USB buses and devices connected to them.

- List all the USB devices available:

`lsusb`

- List the USB hierarchy as a tree:

`lsusb -t`

- List detailed information about a USB device:

`lsusb -D {{device}}`

- List devices with a specified vendor and product id only:

`lsusb -d {{vendor}}:{{product}}`

- List verbose information about connected mass storage devices:

`lsusb -v | grep -Ei '(idVendor|Mass Storage)'`
