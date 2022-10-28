# wipefs

> Wipe filesystem, raid, or partition-table signatures from a device.
> More information: <https://manned.org/wipefs>.

- Display signatures for specified device:

`sudo wipefs {{/dev/sdX}}`

- Wipe all available signature types for a specific device with no recursion into partitions:

`sudo wipefs --all {{/dev/sdX}}`

- Wipe all available signature types for the device and partitions using a glob pattern:

`sudo wipefs --all {{/dev/sdX}}*`

- Perform dry run:

`sudo wipefs --all --no-act {{/dev/sdX}}`

- Force wipe, even if the filesystem is mounted:

`sudo wipefs --all --force {{/dev/sdX}}`
