# partx

> Parse a partition table and tell the kernel about it.
> More information: <https://manned.org/partx>.

- List the partitions on a block device or disk image:

`sudo partx {{[-l|--list]}} {{path/to/device_or_disk_image}}`

- Add all the partitions found in a given block device to the kernel:

`sudo partx {{[-a|--add]}} {{[-v|--verbose]}} {{path/to/device_or_disk_image}}`

- Delete all the partitions found from the kernel (does not alter partitions on disk):

`sudo partx {{[-d|--delete]}} {{path/to/device_or_disk_image}}`
