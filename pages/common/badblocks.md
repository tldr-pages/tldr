# badblocks

> Search a device for bad blocks.

- Search a disk for bad blocks by using a non-destructive read-only test:

`sudo badblocks {{/dev/sda}}`

- Search an unmounted disk for bad blocks with a non-destcructive read-write test:

`sudo badblocks -n {{/dev/sda}}`

- Search an unmounted disk for bad blocks with a destructive write test:

`sudo badblocks -w {{/dev/sda}}`
