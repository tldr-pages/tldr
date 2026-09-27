# lvmdiskscan

> Scan for devices that may be used as physical volumes by LVM.
> Note: This command is deprecated, use `pvs` instead.
> More information: <https://manned.org/lvmdiskscan>.

- Scan all devices:

`lvmdiskscan`

- Show only physical volumes (PVs):

`lvmdiskscan {{[-l|--lvmpartition]}}`

- Increase verbosity (repeat for more detail):

`lvmdiskscan {{[-v|--verbose]}}`
