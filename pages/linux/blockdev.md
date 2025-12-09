# blockdev

> Manage, query, and manipulate block devices.
> More information: <https://manned.org/blockdev>.

- Print a report for all devices:

`sudo blockdev --report`

- Print a report for a specific device:

`sudo blockdev --report {{/dev/sdXY}}`

- Get the size of a device in 512-byte sectors:

`sudo blockdev --getsz {{/dev/sdXY}}`

- Set read-only:

`sudo blockdev --setro {{/dev/sdXY}}`

- Set read-write:

`sudo blockdev --setrw {{/dev/sdXY}}`

- Flush buffers:

`sudo blockdev --flushbufs {{/dev/sdXY}}`

- Get the physical block size:

`sudo blockdev --getpbsz {{/dev/sdXY}}`

- Set the read-ahead value to 128 sectors:

`sudo blockdev --setra 128 {{/dev/sdXY}}`
