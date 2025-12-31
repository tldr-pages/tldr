# mkinitfs

> Generate an initramfs on Alpine Linux.
> More information: <https://manned.org/mkinitfs>.

- Generate an initramfs with the features specified in `/etc/mkinitfs/mkinitfs.conf`:

`mkinitfs`

- Use a different configuration file:

`mkinitfs -c {{path/to/config}}`

- Compress the initramfs using the specified compression algorithm (default: gzip):

`mkinitfs -C {{gzip|xz|zstd|lz4|none}}`

- List files that will be included in the initramfs image:

`mkinitfs -l`

- List all available features:

`mkinitfs -L`
