# blkdiscard

> Discards device sectors on storage devices. Useful for SSDs.
> More information: <https://manned.org/blkdiscard>.

- Discard all sectors on a device, removing all data:

`blkdiscard {{/dev/device}}`

- Securely discard all blocks on a device, removing all data:

`blkdiscard {{[-s|--secure]}} {{/dev/device}}`

- Discard the first 100 MB of a device:

`blkdiscard {{[-l|--length]}} {{100MB}} {{/dev/device}}`
