# lsusb

> Display information about USB buses and devices connected to them.
> More information: <https://manned.org/lsusb>.

- List all the USB devices available:

`lsusb`

- List the USB hierarchy as a tree:

`lsusb {{[-t|--tree]}}`

- List verbose information about USB devices:

`lsusb {{[-V|--verbose]}}`

- List detailed information about a USB device:

`lsusb {{[-V|--verbose]}} -s {{bus}}:{{device number}}`

- List devices with a specified vendor and product ID only:

`lsusb -d {{vendor}}:{{product}}`
