# mtd

> Interact with Memory Technology Device partitions on OpenWrt.
> See also: `sysupgrade`, `firstboot`.
> More information: <https://openwrt.org/docs/techref/mtd>.

- Write an image to an MTD partition:

`mtd write {{path/to/image.bin}} {{partition_name}}`

- Erase an MTD partition:

`mtd erase {{partition_name}}`

- Unlock an MTD partition before writing:

`mtd unlock {{partition_name}}`

- Write an image and reboot when finished:

`mtd -r write {{path/to/image.bin}} {{partition_name}}`

- Verify a written image against a partition:

`mtd verify {{path/to/image.bin}} {{partition_name}}`

- Dump a partition to a file:

`mtd read {{partition_name}} {{path/to/output.bin}}`
