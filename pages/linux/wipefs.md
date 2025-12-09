# wipefs

> Wipe filesystem, raid, or partition-table signatures from a device.
> More information: <https://manned.org/wipefs>.

- Display signatures for specified device:

`sudo wipefs {{/dev/sdX}}`

- Wipe all available signature types for a specific device with no recursion into partitions:

`sudo wipefs {{[-a|--all]}} {{/dev/sdX}}`

- Wipe all available signature types for the device and partitions using a glob pattern:

`sudo wipefs {{[-a|--all]}} {{/dev/sdX}}*`

- Perform dry run:

`sudo wipefs {{[-a|--all]}} {{[-n|--no-act]}} {{/dev/sdX}}`

- Force wipe, even if the filesystem is mounted:

`sudo wipefs {{[-a|--all]}} {{[-f|--force]}} {{/dev/sdX}}`
