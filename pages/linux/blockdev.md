# blockdev

> Call block device ioctls from the command line.
> More information: <https://manned.org/man/blockdev>.

- Print a report for all devices:

`blockdev --report`

- Print a report for a specific device:

`blockdev --report /dev/sdX`

- Get the size of a device in 512-byte sectors:

`blockdev --getsz /dev/sdX`

- Set read-only:

`blockdev --setro /dev/sdX`

- Set read-write:

`blockdev --setrw /dev/sdX`

- Flush buffers:

`blockdev --flushbufs /dev/sdX`

- Get the physical block size:

`blockdev --getpbsz /dev/sdX`

- Set the read-ahead value to 128 sectors:

`blockdev --setra 128 /dev/sdX`
