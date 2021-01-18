# partx 

> Parse a partition table and tell ther kernel about it.

- List the partitions on a block device or disk image:

`sudo partx --list {{path/to/device_or_disk_image}}`

- Add all the paritions found in a given block device to the kernel:

`sudo partx --add --verbose {{path/to/device_or_disk_image}}`

- Delete all the partitions found from the kernel (does not alter partitions on disk):

`sudo partx --delete {{path/to/device_or_disk_image}}`
