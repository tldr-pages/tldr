# pixiecore

> Tool to manage the network booting of machines.
> More information: <https://github.com/danderson/netboot/tree/master/pixiecore>.

- Start a PXE boot server which provides a `netboot.xyz` boot image:

`pixiecore {{quick}} xyz --dhcp-no-bind`

- Start a new PXE boot server which provides an Ubuntu boot image:

`pixiecore {{quick}} ubuntu --dhcp-no-bind`

- Get a list of all available boot images for quick mode:

`pixiecore quick --help`
