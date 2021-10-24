# badblocks

> Search a device for bad blocks.
> Some usages of badblocks can cause destructive actions, such as erasing all data on a disk, including the partition table.
> More information: <https://manned.org/badblocks>.

- Search a disk for bad blocks by using a non-destructive read-only test:

`sudo badblocks {{/dev/sdX}}`

- Search an unmounted disk for bad blocks with a non-destructive read-write test:

`sudo badblocks -n {{/dev/sdX}}`

- Search an unmounted disk for bad blocks with a destructive write test:

`sudo badblocks -w {{/dev/sdX}}`

- Search an unmounted disk for bad blocks with a destructive write test and show verbose status:

`sudo badblocks -svw {{/dev/sdX}}`

- Search an unmounted disk in destructive mode and output found blocks to a file:

`sudo badblocks -o {{path/to/file}} -w {{/dev/sdX}}`

- Search an unmounted disk in destructive mode with improved speed using 4K block size and 64K block count:

`sudo badblocks -w -b {{4096}} -c {{65536}} {{/dev/sdX}}`
