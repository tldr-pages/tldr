# partprobe

> Inform the operating system kernel of partition table changes.
> More information: <https://manned.org/partprobe>.

- Inform the operating system kernel of partition table changes:

`sudo partprobe`

- Inform the kernel of partition table changes and show a summary of devices and their partitions:

`sudo partprobe -s`

- Show a summary of devices and their partitions but don't inform the kernel:

`sudo partprobe -s --dry-run`
