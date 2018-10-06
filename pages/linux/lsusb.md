# lsusb

> Display info about connected USB devices.

- List all the USB ports available:

`lsusb`

- Hierarchy view, with each device's supported speed:

`lsusb -t`

- Get detailed info of a USB device:

`lsusb -D {{device}}`

- Show only devices with the specified vendor and product ID:

`lsusb -d {{vendor}}:{{product}}`

- List all mass storages:

`lsusb -v | grep -Ei '(idVendor|Mass Storage)'`
