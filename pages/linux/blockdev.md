# blockdev

> Call block device ioctls from the command line.
> More information: <https://manned.org/man/blockdev>.

- Print a report for all devices:

`blockdev --report`

- Print a report for a specific device:

`blockdev --report {{/dev/sdXY}}`

- Get the size of a device in 512-byte sectors:

`blockdev --getsz {{/dev/sdXY}}`

- Set read-only:

`blockdev --setro {{/dev/sdXY}}`

- Set read-write:

`blockdev --setrw {{/dev/sdXY}}`

- Flush buffers:

`blockdev --flushbufs {{/dev/sdXY}}`

- Get the physical block size:

`blockdev --getpbsz {{/dev/sdXY}}`

- Set the read-ahead value to 128 sectors:

`blockdev --setra 128 {{/dev/sdXY}}`
