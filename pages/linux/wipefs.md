# wipefs

> Wipe filesystem, raid, or partition-table signatures from a device.

- Display signatures for specified device:

`sudo wipefs {{/dev/sda}}`

- Wipe all available signatures for specified device:

`sudo wipefs --all {{/dev/sda}}`

- Perform dry run:

`sudo wipefs --all --no-act {{/dev/sda}}`

- Force wipe, even if the filesystem is mounted:

`sudo wipefs --all --force {{/dev/sda}}`
