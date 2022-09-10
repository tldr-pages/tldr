# wipefs

> Wipe filesystem, raid, or partition-table signatures from a device.
> More information: <https://manned.org/wipefs>.

- Display signatures for specified device:

`sudo wipefs {{/dev/sdX}}`

- Wipe all available signatures for specified device level (no recursion to sub-level block layers):

`sudo wipefs --all {{/dev/sdX}}`

- Wipd all available signatures for the specified device at all block levels using a glob pattern:

`sudo wipefs --all {{/dev/sdX*}}`

- Perform dry run:

`sudo wipefs --all --no-act {{/dev/sdX}}`

- Force wipe, even if the filesystem is mounted:

`sudo wipefs --all --force {{/dev/sdX}}`
