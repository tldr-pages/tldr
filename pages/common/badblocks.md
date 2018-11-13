# badblocks

> Search a device for bad blocks.
> Some usages of badblocks can cause destructive actions, such as erasing all the data on a disk, including the partition table.

- Search a disk for bad blocks by using a non-destructive read-only test:

`sudo badblocks {{/dev/sda}}`

- Search an unmounted disk for bad blocks with a non-destructive read-write test:

`sudo badblocks -n {{/dev/sda}}`

- Search an unmounted disk for bad blocks with a destructive write test:

`sudo badblocks -w {{/dev/sda}}`
