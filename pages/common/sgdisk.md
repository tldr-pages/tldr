# sgdisk

> GPT partition table manipulator, part of the GPT fdisk suite.
> Useful for scripting and advanced partitioning tasks.
> More information: <https://linux.die.net/man/8/sgdisk>.

- Display the partition table of a device:

`sgdisk -p {{/dev/sdX}}`

- Create a new partition:

`sgdisk -n {{1}}:{{2048}}:{{4095}} -t {{1}}:{{8300}} -c {{1}}:"{{Linux root}}" {{/dev/sdX}}`

- Delete a partition:

`sgdisk -d {{1}} {{/dev/sdX}}`

- Change the partition type:

`sgdisk -t {{1}}:{{ef00}} {{/dev/sdX}}`

- Set a partition name:

`sgdisk -c {{1}}:"{{EFI System Partition}}" {{/dev/sdX}}`

- Wipe all GPT and MBR data from a device:

`sgdisk -Z {{/dev/sdX}}`
