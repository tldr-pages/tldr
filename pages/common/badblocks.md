# badblocks

> Search a device for bad blocks.
> Some usages of badblocks can cause destructive actions, such as erasing all the data on a disk, including the partition table.

- Search a disk for bad blocks by using a non-destructive read-only test:

`sudo badblocks {{/dev/sda}}`

- Search an unmounted disk for bad blocks with a non-destructive read-write test:

`sudo badblocks -n {{/dev/sda}}`

- Search an unmounted disk for bad blocks with a destructive write test:

`sudo badblocks -w {{/dev/sda}}`

- Search an unmounted disk for bad blocks with a destructive write test and show verbose status:

`sudo badblocks -svw {{/dev/sda}}`

- Search an unmounted disk in desctructive mode and output found blocks to a file:

`sudo badblocks -o {{/path/to/file}} -w {{/dev/sda}}`

- Search an unmounted disk in desctructive mode with improved speed using 4K block size and 64K block count:

`sudo badblocks -w -b {{4096}} -c {{65536}} {{/dev/sda}}`
