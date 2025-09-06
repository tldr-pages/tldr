# badblocks

> Search a device for bad blocks.
> Some usages of badblocks can cause destructive actions, such as erasing all data on a disk, including the partition table.
> More information: <https://manned.org/badblocks>.

- Search a disk for bad blocks by using a non-destructive read-only test:

`sudo badblocks {{/dev/sdX}}`

- Search an unmounted disk for bad blocks with a [n]on-destructive read-write test:

`sudo badblocks -n {{/dev/sdX}}`

- Search an unmounted disk for bad blocks with a destructive [w]rite test:

`sudo badblocks -w {{/dev/sdX}}`

- Use the destructive [w]rite test and [s]how [v]erbose progress:

`sudo badblocks -svw {{/dev/sdX}}`

- In destructive mode, [o]utput found blocks to a file:

`sudo badblocks -o {{path/to/file}} -w {{/dev/sdX}}`

- Use the destructive mode with improved speed using 4K [b]lock size and 64K block [c]ount:

`sudo badblocks -w -b {{4096}} -c {{65536}} {{/dev/sdX}}`
