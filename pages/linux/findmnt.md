# findmnt

> Find your filesystem.
> More information: <https://manned.org/findmnt>.

- List all mounted filesystems:

`findmnt`

- Search for a device:

`findmnt {{/dev/sdb1}}`

- Search for a mountpoint:

`findmnt {{/}}`

- Find filesystems in specific type:

`findmnt -t {{ext4}}`

- Find filesystems with specific label:

`findmnt LABEL={{BigStorage}}`
