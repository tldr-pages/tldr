# badblocks

> Search a device for bad blocks.

- Search a disk for bad blocks by using a non-destructive read-only test:

`sudo badblocks {{/dev/sda}}`

- Search an unmounted disk for bad blocks with a non-descructive read-write test:

`sudo badblocks -n {{/dev/sda}}`

- Search an unmounted disk fo r bad blocks with a DESTRUCTIVE write test:

`sudo badblocks -w {{/dev/sda}}`
